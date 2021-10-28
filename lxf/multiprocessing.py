# multiple process
"""
Process is when a single task is operated
When playing a movie, playing scenes is a process, playing sound is another process
so multi-process
"""

"""
In Unix/Linus, fork() can be used to execute child-process
child-process using getppid() to retrive the ID for the parent-process
"""

# import os 

# print ('Process (%s) Start... This is the first line' % os.getpid())

"""
Below only works on Unix/Linus/Mac

pid = os.fork()
if pid == 0:
    print ('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print ('I (%s) just created a child process (%s).' % (os.getpid(), pid))

Result:
    Process (876) start...
    I (876) just created a child process (877).
    I am child process (877) and my parent is 876.

"""
# in python



from multiprocessing import Process
import os

def run_proc(name):
    """function to output child-process id

    Args:
        name (child-process): a child process
    """
    print ('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
    print ('Parent process %s' % os.getpid())
    p = Process(target=run_proc, args = ('test',))
    print ('Child process will start.')
    p.start()
    p.join()
    print ('Child process end')





# if had great amount of child processes
# can use Pool

from multiprocessing import Process, Pool
import os, time, random

def lont_time_task(name):
    """function to calculate the running time of process

    Args:
        name (process name): process name, with imformative outputs
    """
    print ('Run task %s (%s)...' % (name, os.getpid())) # for task #, get its parent process ID
    start = time.time() # variable starting time
    time.sleep(random.random() * 3) # wait for random()*3 time, random() is between 0 and 1
    end = time.time() # variable ending time
    print ('Task %s runs %0.3f seconds.' % (name, (end - start))) # output the running time of task#(pid), to third decimal
    
if __name__ == '__main__': # if the initialized process is the main process
    print ('Parent process %s.' % os.getpid()) # outpur the pprocess ID
    p = Pool(4) # Pool of 4 processes at the same time
    for i in range(5): 
        p.apply_async(lont_time_task, args=(i,)) # running the calculating time process
    print ('Waiting for all subprocesses to be done...')
    p.close() # close the pool
    p.join() # join the pool (must be after the .close())
    print ('All subprocesses done.')

# to control the input/output of the child process

import subprocess

print ('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print ('Exit code:', r)

"""Result:

$ nslookup www.python.org
Server:		192.168.19.4
Address:	192.168.19.4#53

Non-authoritative answer:
www.python.org	canonical name = python.map.fastly.net.
Name:	python.map.fastly.net
Address: 199.27.79.223

Exit code: 0 # 0 means its child process

"""

# if the child process needs more input, use communicate()

import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)

"""
process above is like executing nslookup, then handfully input the following

set q=mx
python.org
exit
"""


"""Result

$ nslookup
Server:		192.168.19.4
Address:	192.168.19.4#53

Non-authoritative answer:
python.org	mail exchanger = 50 mail.python.org.

Authoritative answers can be found from:
mail.python.org	internet address = 82.94.164.166
mail.python.org	has AAAA address 2001:888:2000:d::a6


Exit code: 0

"""

# communications between processes

















