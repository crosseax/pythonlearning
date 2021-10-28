# threading, or multi threading, relearning

# from the video https://www.youtube.com/watch?v=IEEhzQoKtQU

import threading
import time 


print ('start')

start = time.perf_counter()

def do_something(seconds):
    print (f'Sleeping {seconds} second(s)...')
    time.sleep (seconds)
    print ('Done Sleeping...')










"""

# do_something()

t1 = threading.Thread(target=do_something) # dont use () because we dont want to execute
t2 = threading.Thread(target=do_something)

# now we start the thread
t1.start()
t2.start()
# if only use start(), the main task will skip this and continue 
# hence ending the finish time calculator in 0 secs


# therefore, if we want the thread to finish before the bottom time calculator
# use .join()
t1.join()
t2.join()

"""




threads = []

for _ in range(10): # _ variable is a throw-away variable
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()



finish = time.perf_counter()


print (f'Finished in {round(finish-start, 2)} second(s)')






