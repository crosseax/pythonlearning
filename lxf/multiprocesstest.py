
from multiprocessing import Process
import os


print('再测试一次')

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

