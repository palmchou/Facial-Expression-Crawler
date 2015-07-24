# taskworker.py
# -*- coding:utf-8 -*-

import time, sys, Queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


QueueManager.register('get_task_queue')
#QueueManager.register('get_result_queue')

server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)

m = QueueManager(address=(server_addr, 5000), authkey='abc')

m.connect()

task = m.get_task_queue()
#result = m.get_result_queue()

for i in range(20):
    try:
        n = task.get(timeout=1)
        print('run task ' + n.encode('utf-8'))
        time.sleep(3)
        #result.put(r)
    except Queue.Empty:
        print('task queue is empty.')

print('worker exit.')


