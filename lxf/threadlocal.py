# thread local
# under multi threading, every thread has its individual local variables
# which is hard to use, for function

# read this mtf https://www.liaoxuefeng.com/wiki/1016959663602400/1017630786314240

"""for example Method 1

def process_student(name):
    std = Student(name)
    # std是局部变量，但是每个函数都要用它，因此必须传进去：
    do_task1(std)
    do_task2(std)
    
def do_task1(std):
    do_subtask1(std)
    do_subtask2(std)
    
def do_task2(std):
    do_subtask2(std)
    do_subtask2(std)

每个函数一层一层调用都这么传参数那还得了？用全局变量？也不行，因为每个线程处理不同的Student对象，不能共享。

如果用一个全局dict存放所有的Student对象，然后以thread自身作为key获得线程对应的Student对象如何？

"""

"""Method 2

global_dict = {}

def std_thread(name):
    std = Student(name)
    # 把std放到全局变量global_dict中：
    global_dict[threading.current_thread()] = std
    do_task_1()
    do_task_2()

def do_task_1():
    # 不传入std，而是根据当前线程查找：
    std = global_dict[threading.current_thread()]
    ...

def do_task_2():
    # 任何函数都可以查找出当前线程的std变量：
    std = global_dict[threading.current_thread()]
    ...



这种方式理论上是可行的，它最大的优点是消除了std对象在每层函数中的传递问题，但是，每个函数获取std的代码有点丑。

有没有更简单的方式？

""" 


"""
Thats why we have threadlocal
"""

import threading

local_school = threading.local() # creating global threadlocal subject

def process_student():
    std = local_school.student # acquire local related student
    print ('Hello, %s (in %s)' % (std, threading.current_thread().name))
    
def process_thread(name):
    local_school.student = name # link threadlocal's student
    process_student()
    
t1 = threading.Thread(target= process_thread, args=('Alice',), name = 'Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name = 'Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

# process vs thread

# read this mtf https://www.liaoxuefeng.com/wiki/1016959663602400/1017631469467456#0

    




