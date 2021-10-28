# use type() to check the type of the code

print (type (123)) # <class 'int'>
print (type ('123')) # <class 'str'>
print (type (None)) # <class 'NoneType'>
print (type (abs)) # <class 'builtin_function_or_method'>
# print (type (a)) # NameError: name 'a' is not defined
class Animal(object):
    pass
a = Animal()
print (type (a)) # <class '__main__.Animal'>



# to use such in conditional codes
print(
    type(123) == type(456), # True
    type(123) == int, # True
    type('abc') == type('123'), # True
    type('abc') == str, # True
    type('abc') == type(123), # False
    '\n'
)


def fn():
    pass
print (type(fn))

# to check if it is functions in conditional codes
import types

print (
    type(fn) == types.FunctionType, # True
    type(abs) == types.BuiltinFunctionType, # True
    type(lambda x: x) == types.LambdaType, # True
    type((x for x in range(10))) == types.GeneratorType, # True
    '\n'
)

# use isinstance to check class type to save hassle

class Car(object):
    pass
class Toyota(Car):
    pass
class Tacoma(Toyota):
    pass

a = Car()
b = Toyota()
c = Tacoma()

print (
    isinstance (a, Car), # True
    isinstance (b, Toyota), # True
    isinstance (c, Tacoma), # True
    isinstance (b, Car) and isinstance(c, Car), # True
    isinstance (b, Tacoma), # False
    isinstance (a, Toyota) or isinstance (b, Toyota), # True, b is even a is not, its basic logic if you dont understand go fucking eat a cock and die
    '\n'
)

# more you can check
print (
    isinstance('a', str), # True
    isinstance(123, int), # True
    isinstance(b'a', bytes), # True
    isinstance([1, 2, 3], (list, tuple)), # True
    isinstance((1, 2, 3), (list, tuple)), # True
    '\n' 
)

# use dir(), to retrive all the types of a thing

print (dir ('abc'), '\n')
print (dir (a), '\n')

# in python, __xxx__ has some unique use case
# for example

print (
    len('ABC'),
    'ABC'.__len__()
)
# the two above is equal
# to len the class
class MyDog(object):
    def __len__(self):
        return 100
dog = MyDog()
print (len(dog))

# and some regular and often ones

print (
    'ABC'.lower(), # abc
    'abc'.upper(), # ABC
    '\n'
)



# use getattr(), setattr(), hasattr()
# to alter an object's attribute

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()
print (
    hasattr(obj, 'x'), # True, has attribute 'x'?
    obj.x, # 9
    hasattr(obj, 'y'), # False, has attrubute 'y'?
)

setattr(obj, 'y', 19) # set an attribute 'y' that equals 19

print (
    hasattr(obj, 'y'), # True, has an attribute 'y'
    getattr(obj, 'y'), # 19, get the attribute y
    obj.y # 19 
)

# getattr (obj, 'z'), AttributeError
# so we can input a defaul attribute
print (getattr (obj, 'z', 404)) # if no attribute 'z', return 404

# also works for method
print (
    hasattr(obj, 'power'), # True, has property 'power'?
    getattr(obj, 'power'), # <bound method MyObject.power of <__main__.MyObject object at 0x000001BC99D54BB0>>
)
fn = getattr(obj, 'power') 
print (fn) # <bound method MyObject.power of <__main__.MyObject object at 0x000001BC99D54BB0>>

print (fn()) # 81

# a correct example

class Image(object):
    pass

pic = Image()

def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None

print (readImage(pic))


