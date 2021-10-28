# decorator
# you can call the function by its variables
# honestly this chapter is messy af, if you ever gonna use it, just google some specific incidents to make it work

def now():
    print ('2020-01-27')

f = now
print ('f',f())

t = now.__name__
print ('t',t)
t1 = f.__name__
print ('t1',t1)

# now, we're going to augment now(), we wanna use now without changing the definition of now()
# this is called a decorator
# decorator is actually, higher-level of return function

def log(func):
    def wrapper(*args, **kw):
        return func(*args, **kw)
    return wrapper

# here above, log is a decorator

@log
def now():
    print ('2020-02-28')

now()
#call now():
#2020-2-28

print ('\n')
print ('Youtube time')

# ----HERE IS FROM YOUTUBE----

def g1(func):
    def wrapper():
        print ('begin')
        func()
        print ('end')
    return wrapper

def g():
    print ('hello')

g1(g)()

print (g1)
print (g1(g))
print (g1(g)())

print ('\n')
# so lets say everytime i call g, i wanna do the g1 function
g = g1(g) # set g (variable) equal to the (function) g1 with the (parameter) f pass into it
# this is called function aliasing
# this can be replaced with a nicer thing, called, DECORATOR

g() # when do so
# im actually calling g1, giving value of function g(), then act g1 

# DECORATOR
@g1
def t():
    print ('hello decorator')

t() # same result
print('same result above')

def f2(func):
    def wrapper (*args, **kwargs):
        print ('begin again')
        val = func(*args, **kwargs)
        print ('end again')
        return val
    return wrapper

@f2 
def ff(a, b = 9):
    print (a, b)

ff('hi')

print ('one more example below')
# one more example
@f2
def add(x,y):
    return x+y
    
print (add(10,15))

print('\n')

# timer example

import time
def timer(func):
    def wrapper():
        before = time.time()
        func()
        print ('function took:', time.time() - before, 'seconds')
    return wrapper

@timer 
def run():
    time.sleep(2)
run()

# ---YOUTUBE ENDS HERE---

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# or

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator



# hw 
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        t1 = time.time()*1000
        fn(*args, **kw)
        t2 = time.time() * 1000
        print('%s executed in %s ms' % (fn.__name__, t2 - t1))
        return fn(*args, **kw)
    return wrapper
