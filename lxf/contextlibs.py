# contextlib

# read this https://www.liaoxuefeng.com/wiki/1016959663602400/1115615597164000

# once open files in python, it must be closed correctly after using

try:
    f = open('./hellotext.txt', 'r')
    f.read()
finally:
    if f:
        f.close()

# or you can do below to save hussle

with open ('./hellotext.txt', 'r') as f:
    f.read()

"""
Actually, you can do many things with with
if you get the context correct
"""

class Query(object):
    def __init__(self,name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print ('Query info about %s' % self.name)


"""
now we can use with to our own resource
"""

with Query('Bob') as q:
    q.query()


# contextmanager
# even easier

from contextlib import contextmanager

class Query2(object):
    def __init__(self, name):
        self.name = name

    def query2(self):
        print ('Query info about %s' % self.name)

@contextmanager
def create_query2(name):
    print('Begin')
    q = Query2(name)
    yield q
    print ('End')

with create_query2('Steven') as q:
    q.query2()


# more if we want to autorun some specific codes bf/af our code

@contextmanager # if not this, AttributeError: __enter__
def tag(name): 
    print('<%s>' % name)
    yield 
    print('</%s>' % name)

with tag('h1'):
    print ('hello')
    print ('world')


@contextmanager
def adding(a,b):
    print ('Im going to add those two inputs')
    print (a, b)
    yield 
    a = a+b
    print (a)
    print('Now done')

with adding(10,5):
    n = 0
    while n < 5:
        n = n + 1 
        print ('with line:', n)

"""
output:

Im going to add those two inputs
10 5
with line: 1
with line: 2
with line: 3
with line: 4
with line: 5
15
Now done
"""

# @closing

# @closing is a generator decorated by contextmanager

from contextlib import closing
from urllib.request import urlopen

#with closing(urlopen('http://www.python.org')) as page:
#    for line in page:
#        print (line)

with closing(urlopen('https://www.baidu.com')) as page:
    for line in page:
        print (line)

# its just like below

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()







