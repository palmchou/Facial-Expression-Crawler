# taskmanager.py
#!/usr/bin/python 
# -*- coding:utf-8 -*-

import json
import random, time, Queue
from multiprocessing.managers import BaseManager

task_queue = Queue.Queue()
feedback_queue = Queue.Queue()

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_feedback_queue', callable=lambda:feedback_queue)

settings = json.load(open("./local_settings.json"))
auth_key = settings["auth_key"]
port_num = settings["port"]

manager = QueueManager(address=('', port_num), authkey=auth_key)
manager.start()
task = manager.get_task_queue()
feedback = manager.get_feedback_queue()


KeywordList = json.load(open("./baiduKeyWordList.json"))

for i in KeywordList:
    print('Put task ...' + i)
    task.put(i)
    

while task.qsize() != 0:
    if i != task.qsize():
        print 'task quantity : ' + str(task.qsize())
        i = task.qsize()
    r = feedback.get(timeout=100)
    print('Result: '+str(r))
    

manager.shutdown()
