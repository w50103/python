#!/usr/bin/env python3
# -*- coding: utf8 -*-
import random
from multiprocessing import Process
import os

import time
from multiprocessing.pool import Pool


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name,(end - start)))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())

    p = Pool()

    for i in range(50):
        p.apply_async(long_time_task,args=(i,))
    print('Waiting from all subprocesses done...')

    p.close()
    p.join()
    print('All subprocesses done.')