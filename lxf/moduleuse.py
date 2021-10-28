# module
# and how to use module

'a test module'

__author__ = 'Shuren Zhou' 

# __xxx__ is a special case variable
# _xxx, or __xxx is a private variable

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print ('Hello World')
    elif len(args) == 2:
        print ('Hello, %s!' % args[1])
    else:
        print ('Too many arguments!')

if __name__ == '__main__':
    test()

# run with 
# python moduleuse.py name


# private variable usecase

def _private_1 (name):
    return 'Hello, %s' % name
def _private_2 (name):
    return 'Hi, %s' % name
def greeting(name):
    if len(name) > 3:
        return _private_1
    else:
        return _private_2

N = ['a','b','c','d']
print(greeting(N))

print('\n')

# third-party module installing

# use pip (for windows)

# even better, use Anacoda

# for more info, check https://www.liaoxuefeng.com/wiki/1016959663602400/1017493741106496





