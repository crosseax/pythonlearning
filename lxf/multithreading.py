# multi threading 

"""
Also bruh, just read https://www.liaoxuefeng.com/wiki/1016959663602400/1017629247922688
read the comment for better understandings
recommend watching:
https://www.youtube.com/watch?v=7ENFeb-J75k

"""

import time, threading



def loop():
    """
    current_thread() always return to the main thread, 
    which in this case, is the .py when running
    """
    print ('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print ('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(0)
    print ('thread %s is ended.' % threading.current_thread().name)
    
print ('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name = 'LoopThread')
t.start()
t.join()
print ('thread %s ended.' %threading.current_thread().name)

"""
In multiprocessing, 
    all the variables are individually stored in itself that does not affect each other 
In multithreading however,
    a single variable can be changed in each individual thread
    so below is how you prevent that chaos
"""

import time, threading

bal = 0 # bank balance, which you for sure dont want others to change

def change_bal(n):
    global bal  # global means the change inside the function applies to the variable 
                # even outside
                # it turns local variable into global
    bal = bal + n
    bal = bal - n

def run_thread1(n):
    for i in range (2000000):
        change_bal(n)

t1 = threading.Thread(target=run_thread1, args = (5,))
t2 = threading.Thread(target=run_thread1, args = (8,))
t1.start()
t2.start()
t1.join()
t2.join()

print ('without locksafe:', bal) 

"""
the result above could vary and even be negative
because the threading starting together then end together that is messing with the variable
therefore, if we want to make sure the result dont fail, 
we need to lock the function change_bal
"""

bal = 0
lock = threading.Lock()

def run_thread(n):
    for i in range (100000):
        lock.acquire() # acquiring the lock (idk why you even need the comments)
        try:
            change_bal(n)
        finally:
            lock.release() # THIS IS MUST


t1 = threading.Thread(target=run_thread, args = (5,))
t2 = threading.Thread(target=run_thread, args = (8,))
t1.start()
t2.start()
t1.join()
t2.join()

print ('with locksafe:', bal)



"""
Use a death loop below to destroy your CPU

Ctrl + Alt + M to force stop



import threading, multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()
    
    


But, such thing above in python is only gonna destroy one CPU core
in C++ or Java, you can destroy them all

"""