# choose multiprocess over multithread because that is more stable
# in multiprocessing, managers module can also split processes into multiple machines

# read https://www.liaoxuefeng.com/wiki/1016959663602400/1017631559645600#0


"""
    
举个例子：如果我们已经有一个通过Queue通信的多进程程序在同一台机器上运行，现在，由于处理任务的进程任务繁重，希望把发送任务的进程和处理任务的进程分布到两台机器上。怎么用分布式进程实现？

原有的Queue可以继续使用，但是，通过managers模块把Queue通过网络暴露出去，就可以让其他机器的进程访问Queue了。

我们先看服务进程，服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务：

"""

import random, time, queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue() # task sender queue
result_queue = queue.Queue() # task receiver queue


class QueueManager(BaseManager): # 从BaseManager继承的QueueManager:
    pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)

manager = QueueManager(address=('', 5000), authkey=b'abc') # 绑定端口5000, 设置验证码'abc':
manager.start() # 启动Queue:

# 获得通过网络访问的Queue对象:
task = manager.get_task_queue()
result = manager.get_result_queue()

# 放几个任务进去:
for i in range(10):
    n = random.randint(0,10000)
    print ('Put task %d...' % n)
    task.put(n)

print('Try get results...') # 从result队列读取结果:

for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)

manager.shutdown() # 关闭:
print('master exit.')


"""
请注意，当我们在一台机器上写多进程程序时，创建的Queue可以直接拿来用，
但是，在分布式多进程环境下，添加任务到Queue不可以直接对原始的task_queue进行操作，
那样就绕过了QueueManager的封装，必须通过manager.get_task_queue()获得的Queue接口添加。

然后，在另一台机器上启动任务进程（本机上启动也可以）：

go to taskworker.py
"""

# task worker 

import time, sys, queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager): # 创建类似的QueueManager:
    pass

# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')


server_addr = '127.0.0.1' # 连接到服务器，也就是运行task_master.py的机器:
print('Connect to server %s...' % server_addr)
m = QueueManager(address=(server_addr, 5000), authkey=b'abc') # 端口和验证码注意保持与task_master.py设置的完全一致:

m.connect() # 从网络连接:

# 获取Queue的对象:
task = m.get_task_queue()
result = m.get_result_queue()

# 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')
        
# 处理结束:
print('worker exit.')

