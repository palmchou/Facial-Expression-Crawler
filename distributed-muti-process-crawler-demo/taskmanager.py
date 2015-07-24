# taskmanager.py
#!/usr/bin/python 
# -*- coding:utf-8 -*-

import json
import random, time, Queue
from multiprocessing.managers import BaseManager

task_queue = Queue.Queue()


class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue', callable=lambda: task_queue)

manager = QueueManager(address=('', 5000), authkey='abc')
manager.start()
task = manager.get_task_queue()


KeywordList = json.load(open("./baiduKeyWordList.json"))

for i in KeywordList:
    print('Put task ...' + i)
    task.put(i)


while task.qsize() != 0:
    if i != task.qsize():
        print 'task quantity : ' + str(task.qsize())
        i = task.qsize()
    time.sleep(5)
    

manager.shutdown()