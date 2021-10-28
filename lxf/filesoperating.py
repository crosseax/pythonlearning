# operating files and paths in python

import os 

os.name 

print (os.name) # nt

# for above, windows: nt, Linux or Unix or MacOSX: posix

try:
    print (os.uname()) # this does not run on windows
except:
    pass


print (os.environ.get('PATH')) # to get more environmental variables

p = os.path.abspath('.')
print (os.path.abspath('.')) # to see the path of this file

os.path.join(p, 'testdir') # to create a testdir path under path p

os.mkdir('/users/qq417/Desktop/Python/Python2021/testdir') # make the path

os.rmdir('/users/qq417/Desktop/Python/Python2021/testdir') # remove the path

'''
for more of below, check on youtube

os.path.join() 

os.path.split()
ep:
    os.path.split('/file/example.txt') ==output==> ('/file','example.txt')

os.path.splitext()
ep:
    os.path.splitext('/example.txt') ==output==> ('example', '.txt')
'''

try:
    """code below dont run but you get the idea
    """
    os.rename('test.txt', 'test2.txt')
    os.remove('test2.txt')
except:
    pass


"""lets see how to filter files using python
"""

Lf = [x for x in os.listdir('.') if os.path.isdir(x)] # to show all the paths
print (Lf)

Lp = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'] # to show all the .py files 
print (Lp)

"""
hw
"""

def filePath(path, key):
    
    files = [x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x)) and os.path.splitext(x)[1]==key]
    
    for f in files:
        print('[p]', path, '\t[f]', f)
        
    return

def findFile(path, key):

    filePath(path, key)
    dirs = [x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]

    for d in dirs:
        d = os.path.join(path, d)
        findFile(d, key)

    return

findFile('.', '.py')




