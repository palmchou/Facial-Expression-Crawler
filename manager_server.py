#!/usr/bin/python
# -*- coding:utf-8 -*-

import json
import time
import Queue
import datetime
import socket
import copy
import logging
from multiprocessing.managers import BaseManager


def update_with(feedback, kw_dict):
    kw = kw_dict[feedback['se']][feedback['id']]
    l_kw = keywords_local[feedback['se']][feedback['id']]
    kw['available'] = False
    kw['last_acquired'] = feedback['last_acquired']
    l_kw['last_acquired'] = feedback['last_acquired']
    kw['succ_count'] += feedback['succ_count']
    l_kw['succ_count'] = kw['succ_count']
    if kw['last_acquired'] == 1000:
        kw['last_update'] = datetime.datetime.utcnow().max
        print kw, 'finished'
    else:
        kw['last_update'] = datetime.datetime.utcnow()
        print kw, 'updated.'


class QueueManager(BaseManager):
    pass

bd_queue = Queue.Queue()
gg_queue = Queue.Queue()
fb_queue = Queue.Queue()

QueueManager.register('baidu_queue', callable=lambda: bd_queue)
QueueManager.register('google_queue', callable=lambda: gg_queue)
QueueManager.register('feedback_queue', callable=lambda: fb_queue)

socket.setdefaulttimeout(10)
tmp_fp = open("./local_settings.json")
settings = json.load(tmp_fp)
tmp_fp.close()
auth_key = settings["auth_key"]
port_num = settings["port"]
lost_diff = datetime.timedelta(minutes=10)

manager = QueueManager(address=('', port_num), authkey=auth_key)
manager.start()

baidu_queue = manager.baidu_queue()
google_queue = manager.google_queue()
feedback_queue = manager.feedback_queue()

# 获取本地保存的 关键词信息
tmp_fp = open("./keywords.json")
keywords_local = json.load(tmp_fp)
tmp_fp.close()
keywords_status = copy.deepcopy(keywords_local)

# add keywords to queue
# google
kw_google = keywords_status['google']
for (kw_id, kw) in kw_google.items():
    if kw['last_acquired'] < 1000:
        print 'Add keyword', kw['words'], 'to google queue'
        kw['id'] = kw_id
        google_queue.put(kw)
        kw['available'] = True
        kw['last_update'] = datetime.datetime.utcnow()
    else:
        kw['available'] = False
        kw['last_update'] = datetime.datetime.utcnow().max
# baidu
kw_baidu = keywords_status['baidu']
for (kw_id, kw) in kw_baidu.items():
    if kw['last_acquired'] < 1000:
        print 'Add keyword', kw['words'], 'to baidu queue'
        kw['id'] = kw_id
        baidu_queue.put(kw)
        kw['available'] = True
        kw['last_update'] = datetime.datetime.utcnow()
    else:  # finished
        kw['available'] = False
        kw['last_update'] = datetime.datetime.utcnow().max

# get feedback
i = 0
while True:
    time.sleep(120)
    i += 1
    try:
        # read feed back and update
        while feedback_queue.qsize() != 0:
            fb_info = feedback_queue.get(timeout=5)
            update_with(fb_info, keywords_status)

        # save keywords information to local disk every 10 mins
        if (i % 5) == 0:
            tmp_fp = open('keywords.update.json', 'w')
            json.dump(keywords_local, tmp_fp)
            tmp_fp.close()
        # check if worker lost connection, and put keyword back to queue
        now = datetime.datetime.utcnow()
        for (kw_id, kw) in keywords_status['google'].items():
            if not kw['available']:
                if (now - kw['last_update']) > lost_diff:
                    print 'keyword', kw, 'lost connection, put back to queue'
                    kw['available'] = True
                    google_queue.put(kw)
        for (kw_id, kw) in keywords_status['baidu'].items():
            if not kw['available']:
                if (now - kw['last_update']) > lost_diff:
                    print 'keyword', kw, 'lost connection, put back to queue'
                    kw['available'] = True
                    baidu_queue.put(kw)

        print google_queue.qsize(), 'keywords left in the queue of google'
        print baidu_queue.qsize(), 'keywords left in the queue of baidu'

        # check if all keywords done
        google_end_flag = False
        baidu_end_flag = False
        if google_queue.qsize() == 0:
            google_end_flag = True
            for (kw_id, kw) in keywords_status['google'].items():
                if kw['available']:  # which should not happen because queue is empty
                    print 'Error', kw, 'is available, but queue is empty'
                    google_end_flag = False
                    break
                if kw['last_update'] != datetime.datetime.max:
                    # this keyword is still on working
                    google_end_flag = False
                    break
        if baidu_queue.qsize() == 0:
            baidu_end_flag = True
            for (kw_id, kw) in keywords_status['baidu'].items():
                if kw['available']:  # which should not happen because queue is empty
                    print 'Error', kw, 'is available, but queue is empty'
                    baidu_end_flag = False
                    break
                if kw['last_update'] != datetime.datetime.max:
                    # this keyword is still on working
                    baidu_end_flag = False
                    break
        if google_end_flag and baidu_end_flag:  # all keywords were finished
            print 'all finished'
            manager.shutdown()
            break
    except StandardError, e:
        logging.exception(e)
tmp_fp = open('keywords.update.json', 'w')
json.dump(keywords_local, tmp_fp)
tmp_fp.close()
print 'server exit'
