# communication between multi processes

from multiprocessing import Process, Queue 
import os, time, random

def write(q):
    print ('Process to write: %s' % os.getpid())
    for value in ['A','B','C']:
        print ('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())
        
def read(q):
    print ('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print ('Get %s from queue.' % value)
        
if __name__ == '__main__':
    q = Queue() # parent process creating Queue, give it to child process
    pw = Process (target=write, args = (q,)) 
    pr = Process (target=read, args = (q,))
    pw.start()
    pr.start()
    pw.join() # waiting for pw to end
    pr.terminate()  # cuz pw wont end, we gonna terminate, 
                    # otherwise we're in the infinite loop
