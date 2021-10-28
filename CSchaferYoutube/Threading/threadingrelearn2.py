# threading relearn 2

# using pool from concurrent module

import concurrent.futures
import time


print ('start')

start = time.perf_counter()

def do_something(seconds):
    print (f'Sleeping {seconds} second(s)...')
    time.sleep (seconds)
    return f'Done Sleeping... after {seconds} second(s)'


with concurrent.futures.ThreadPoolExecutor () as executor:
    secs = [5 ,4 ,3 ,2 ,1] 
    results = [executor.submit(do_something, sec) for sec in secs] # list comprehension
    for f in concurrent.futures.as_completed(results):
        print (f.result())

"""    
    f1 = executor.submit(do_something, 1)
    f2 = executor.submit(do_something, 1)
    print (f1.result())
    print (f2.result())
"""


finish = time.perf_counter()

print (f'Finished in {round(finish-start, 2)} second(s)')


