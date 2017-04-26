#!/usr/bin/env python3
# -*- coding: utf8 -*-
'template style'

import random, time,queue
from multiprocessing.managers import BaseManager

#发送任务
task_queue = queue.Queue()

#接受结果队列
result_queue = queue.Queue()


class QueueManager(BaseManager):
    pass

#注册两个queue到网络，callable参数关联Queue对象：
QueueManager.register('get_task_queue', callable=lambda :task_queue)
QueueManager.register('get_result_queue', callable=lambda :result_queue)

#绑定端口5000
manager = QueueManager(address=('',5000), authkey=b'abc')

#启动queue
manager.start();

task = manager.get_task_queue()
result = manager.get_result_queue()

#添加任务
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d' % n)
    task.put(n)

print('Try get Result...')

for j in range(10):
    r = result.get(timeout=10)
    print('Result : %s' %r)

manager.shutdown()
print('master shutdown')