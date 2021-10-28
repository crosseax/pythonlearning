# error checking and try
# how to locate the error

try:
    def foo():
        r = somefunction()
        if r == (-1):
            return (-1)
        # you should do something here
        return r

    def bar():
        r = foo()
        if r == (-1):
            print ('Error')
        else:
            pass
except:
    pass
    

# code above requires multiple checking before locating the error
# it is unefficient

# lets use a try method

# when somecode might be wrong
# use try:
# if it is wrong, the code will be skipped, running except:
# then running finally:

print ('Error Example below:')
try:
    print ('try...')
    r = 10 / 0
    print ('result:', r)
except ZeroDivisionError as e:
    print ('except:', e)
finally:
    print ('finally...')
print ('END \n')

print ('Try Example below:')
try:
    print ('try...')
    r = 10 / 0
    print ('result:', r)
except ZeroDivisionError as e:
    print ('except:', e)
finally:
    print ('finally...')
print ('END \n')

# multiple except is also allowed
# and adding else: below except, when nothing is wrong, run except

print ('Error Example below:')
try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('No error')
finally:
    print('finally...')
print('END \n')

print ('Try Example below:')
try:
    print('try...')
    r = 10 / int('10')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('No error')
finally:
    print('finally...')
print('END \n')

# errors in python is also class
# all errors are below to BaseException class

'''
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
'''

# so if below:

try:
    foo()
except Exception as e:
    print ('Error')
except ValueError as e:
    print('ValueError')
except NameError as e:
    print ('NameError')
except UnicodeError as e:
    print('UnicodeError')

# so the exception captures the total error, 
# if have sub error, the line wont be triggered

# for exception hierarchy, 
# check: https://docs.python.org/3/library/exceptions.html#exception-hierarchy

print ('\n')
# the benefit of below
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print ('Error here:', e)
    finally:
        print ('finally...')

main() # Error: division by zero
# run bar('0'), foo('0'), 10/0, is division by zero error, print e, print finally...

# so code above reduce the hassle of writing multiple try...except

# for more, check err.py, 
# or https://www.liaoxuefeng.com/wiki/1016959663602400/1017598873256736


# for more
# check below in the same folder
# err_logging.py
# err_raising.py
# err_reraise.py





# hw

try:
    from functools import reduce

    def str2num(s):
        return int(s)

    def calc(exp):
        ss = exp.split('+')
        ns = map(str2num, ss)
        return reduce(lambda acc, x: acc + x, ns)

    def main():
        r = calc('100 + 200 + 345')
        print('100 + 200 + 345 =', r)
        r = calc('99 + 88 + 7.6')
        print('99 + 88 + 7.6 =', r)

    main()

except: 
    pass

# to check the errors above


from functools import reduce


def str2num(s):
    if '.' in s:
        return float(s)
    else:
        return int(s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()
