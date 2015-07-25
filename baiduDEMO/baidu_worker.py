#!/usr/bin/python
# -*- coding:utf-8 -*-

import time, sys, Queue
from multiprocessing.managers import BaseManager
import re
import urllib
import urllib2
import os
import json
import socket
# import string

print sys.getdefaultencoding()


def getHtml(keyword, start):
    req_header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 360SE'}
    url = 'http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result' \
          '&queryWord=' + keyword + '&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0' \
                                    '&word=' + keyword + '&s=0&se=&tab=&width=&height=&face=1&istype=2&qc=&nc=&fr=%26fr%3D&pn=' + str(
        start) + '&rn=60&1433936881420='
    # url='http://cn.bing.com/images/async?q='+keyword+'&async=content&first='+str(start)+'&count=35&IID=images.1&IG=06fd0edefcfa4c9a8be876677b2cd340&CW=1693&CH=312&dgsrr=false&qft=+filterui:face-face&form=R5IR30'
    req = urllib2.Request(url, None, req_header)
    response = urllib2.urlopen(req)
    html = response.read()
    time.sleep(0.5)
    response.close()
    return html


def decoder(url_src):
    dict = {'w': 'a', 'k': 'b', 'v': 'c', '1': 'd', 'j': 'e',
            'u': 'f', '2': 'g', 'i': 'h', 't': 'i', '3': 'j',
            'h': 'k', 's': 'l', '4': 'm', 'g': 'n', '5': 'o',
            'r': 'p', 'q': 'q', '6': 'r', 'f': 's', 'p': 't',
            '7': 'u', 'e': 'v', 'o': 'w', '8': '1', 'd': '2',
            'n': '3', '9': '4', 'c': '5', 'm': '6', '0': '7',
            'b': '8', 'l': '9', 'a': '0'
            }

    url_src = url_src.replace('_z2C$q', ':')
    url_src = url_src.replace('_z&e3B', '.')
    url_src = url_src.replace('AzdH3F', '/')
    url_list = []
    for i in range(0, len(url_src)):
        key = url_src[i]
        if dict.has_key(key):
            t = dict[key]
        else:
            t = key
        url_list.append(t)
    url = ''.join(url_list)
    return url


def getImg(html, start, imgpath, Info):
    cot = start
    t1 = 'source: '
    t2 = ' dst '
    t3 = ' success'
    t4 = ' fail'
    t5 = ' exist'

    reg = r'objURL":"(.+?)",'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)

    success = 0

    for url in imglist:
        imgurl = decoder(url)
        tt = imgurl.split('/')
        image_name = tt[-1]
        type = image_name.split('.')[-1]
        if type != 'jpg' and type != 'png' and type != 'JPG' and type != 'PNG':
            type = 'jpg'
            name = imgpath + '/' + image_name + '_' + str(cot) + '.' + type
        else:
            name = imgpath + '/' + image_name[0:len(image_name) - len(type) - 1] + '_' + str(cot) + '.' + type

        try:
            urllib.urlretrieve(imgurl, name)
            tag = 1
        except:
            tag = 0
            pass
        if (tag == 1):
            str_print = t1 + imgurl + t2 + name + t3
            success += 1
        else:
            str_print = t1 + imgurl + t2 + name + t4
        print str_print
        print >> Info, str_print
        cot += 1
    return success


socket.setdefaulttimeout(10)



step = 60
settings = json.load(open("./local_settings.json"))
auth_key = settings["auth_key"]
port_num = settings["port"]
path = str(settings["path"]) + "/baidu"
# 保存图片路径
img_path = path + "/img"
# 保存爬取图片的信息路径
txt_path = path + "/log"


class QueueManager(BaseManager):
    pass


QueueManager.register('get_task_queue')
QueueManager.register('get_feedback_queue')

server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)

m = QueueManager(address=(server_addr, port_num), authkey=auth_key)

m.connect()

task = m.get_task_queue()
feedback = m.get_feedback_queue()



while True:
    try:
        n = task.get(timeout=1)
        kw = n['kw'].encode('gb2312')
        start_at = n['start_at']
        print kw

        # 图像保存地址imgnewpath
        imgnewpath = os.path.join(img_path, kw)
        if not os.path.isdir(imgnewpath):
            os.makedirs(imgnewpath)
        # 信息保存地址txtnewpath
        txtnewpath = os.path.join(txt_path, kw)
        if not os.path.isdir(txtnewpath):
            os.makedirs(txtnewpath)

        for start in range(start_at, 1000, step):
            r = []
            print kw, 'start from ', str(start), ' to ', str(start + step - 1)
            html = getHtml(kw, start)  # 获取源代码
            savename = txtnewpath + '/' + str(start) + '.txt'
            print savename
            Info = open(savename, 'w')
            success_num = getImg(html, start, imgnewpath, Info)  # 获取图像
            Info.close()

            r.append(n['kw'])
            rr={'aviliable': True, 'last_acquare': start+60, 'success': success_num,
                'update': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}
            r.append(rr)
            feedback.put(r)
    except Queue.Empty:
        print('task queue is empty.')

print('worker exit.')

