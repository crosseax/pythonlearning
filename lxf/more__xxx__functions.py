# more __xxx__ functions
# such usually comes with special usecase

### __str__

class Student(object):
    def __init__ (self, name):
        self.name = name
    
print (Student('Michael')) # <__main__.Student object at 0x00000186413F1D60>

class Student (object):
    def __init__ (self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name 

print (Student('Michael')) # Student object (name: Michael)

# __str__() is different from __repr__(), 
# __str__() is for users,
# __repr__() is for developers

# if run without print()
s = Student('Jane')
s # returns __repr__()

# despite that most of time,
# __str__() and __repr__() has the same codem
# so there's a way to be lazy
# which dont work here for some reason, maybe versions?

class Student(object):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'Student object (name: %s)' % self.name 

    __repr__ = __str__




### __iter__

class Fib(object):
    
    def __init__(self):
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self # instance is itself the iteration object, so return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # to calculate the next number
        if self.a > 100000: # when to exit the iteration
            raise StopIteration()
        return self.a 

for n in Fib():
    print (n)

print ('\n')
# but you cannot use Fib instance as list, tho it looks alike
# Fib()[5] # TypeError: 'Fib' object is not subscriptable

# so

class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

f = Fib()
print (f[50])

print ('\n')
# to use slice

class Fib(object):
    def __getitem__(self, n):
        
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib()
print (f[0:5]) # [1, 1, 2, 3, 5]
print (f[:10]) # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print (f[30]) # 1346269
print (f[9:20]) # [55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]




### __getattr__
# to call the non-existed properties, to avoid error

class Student(object):
     def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

s = Student()
print (s.age()) # 25
# print (s.score), AttributeError: 'Student' object has no attribute 'score'


# whats the purpose
# to fit into different dynamic situations
# read more at the comment of https://www.liaoxuefeng.com/wiki/1016959663602400/1017590712115904

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print (
    Chain().status.user.timeline.list
) # /status/user/timeline/list

######

class Chain(object):
    def __init__(self, path=''):
       self.__path = path

    def __getattr__(self, path):
       return Chain('%s/%s' % (self.__path, path))

    def __call__(self, path):
       return Chain('%s/%s' % (self.__path, path))

    def __str__(self):
       return self.__path

    __repr__ = __str__

print(
    Chain().users('michael').repos
    ) # /users/michael/repos

######



print ('\n')


### __call__

class Student(object):

    def __init__(self, name):
        self.name = name

    def __call__(self):
        print ('My name is %s' % self.name)

s = Student('Jack')
s() # My name is Jack

# what are callables

print (
    callable (Student('j')), # True
    callable (max), # True
    callable ([12,3,4,5]), # False
    callable (None), # False
    callable ('str') # False
)







