#parameters (this page hard and need more work)

def power (x):
    return x * x
print (power (7))


def power (x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print (power(5,2))
print (power(7,5))

# print (power (7)), now it wont work cuz there's no parameter (positional argument) for it
# so

def power (x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print (power(5,2))
print (power(7,5))
print (power (11)) # when power(x), its like power (x,2)
print (power (11,2))
print('\n')

# why do such, reduce the input hassle

def enroll (name, gender, age = 6, city = 'Beijing'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)
print (enroll('Sam','F'))
print (enroll('Steve','M',17,'Shanghai'))
print('\n')

# regular mistakes

def addend(L=[]):
    L.append('End')
    return L

x1 = addend([1,2,3])
x2 = addend(['x','y','z'])
print (x1,x2)

x3 = addend() #gg, default parameter has been mutated
print (x3)
# L nolonger = [], L = ['END']
x4 = addend() 
print (x4) 
print (addend(),addend(),addend())
x5 = addend([4,'kooo',7])
x6 = addend()
print (x5, x6)

print ('watch this')

def addend(L=[]):
    print('step1',L)
    L.append('End')
    print('step2',L)
    return L

print (addend([1]),'\n')
print (addend(),'\n')
print (addend())

print ('\n')

print ('solution')

#Solution
def addend(L=None):
    if L is None:
        L = []
    L.append('End')
    return L

y1 = addend([1,2,3])
y2 = addend([52,'kat',8])
print (y1, y2)
y3 = addend()
y4 = addend()
print (y3, y4)
y5= addend([5])
print (y5)

print('\n')


# well now off we process

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

x1 = calc ([1,2,3,45]) #or
x2 = calc ({1,3,5,7,87})
print (x1,x2)

# x3 = calc (1,2,3,5,6,7,55), wont work, cuz variable numbers is only one
# so now we need to set the parameter to mutable paras (tuples) by adding *

def calc2 (*numbers): 
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

x1 = calc2 (1,2,3,5,6,7,55) # its now creating a tuple
x2 = calc2 (5,7,11)
x3 = calc2 () # even 0 works
print (x1,x2,x3)

# remember now the list wont work, cuz you cant add lists and list * list,
# anyway you defeat hell using hell

# if you really like lists, do below

nums = [1,4,6,8,11]
x5 = calc2 (*nums) # sort this logic out yourself you potato head
print (x5)

print ('\n')
# key words parameters (you ready for more shit)
def person (name, age, **kw):
    print ('name:',name, 'age:',age, 'other:',kw)
person ('Tim',15)

person ('Sook', 18, hobby = 'hokkey') # this is the good shit
person ('Karen', 35, job = 'clerk')

# say theres a dict

things = {'city':'Beijing','job':'Engineer'}
person ('Sadim', 25, **things)

# how to identify the keywords parameters

def person2 (name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print ('name:', name, 'age:', age, 'other:', kw)

person2 ('Jack', 24, city = 'Beijing', addr = 'Chaoyang', zipcode = 123456, job = 'staff')

# if you want to limit the kw

def person3 (name, age, *, city, job):
    print (name, age, city, job)
# anything after single * is seen as limited keywords
person3 ('Huang', 27, city = 'Shanghai', job = 'Finance')

# if add one more variable parameters
def person4 (name, age, *args, city, job):
    print (name, age, args, city, job)

person4 ('Huang', 27, city = 'Shanghai', job = 'Finance')



print('\n')
#now for the real shit

def f1(a ,b ,c = 0, *args, **kw):
    print ('a =',a ,'b =',b , 'c =',c, 'args =', args, 'kw = ', kw)
def f2(a, b, c = 0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1 (1, 2)
f1 (1, 2, c = 3)
f1 (1, 2, 3, 'a', 'b') # both 'a'  and 'b' are seen as args
f1 (1, 2, 3, 'a', 'b', x = 99) # x = 99 is seen as kw because x is given as new name
f2 (1, 2, d = 99, ext = None)
print('\n')

# and you can even work with tuples and dict
args = (1, 2, 3)
kw = {'d': 99, 'x': '#'}
f1 (args, kw) # args is seen as value for a and kw is for b
f2 (*args, **kw) # for 1,2,3 in args is given individually to a b c and kw is given to d and kw

# hw
def mul(x, *y):
    result = x
    if len(y) > 0:
        for i in y:
            result = result * i
    return result        
    

print (mul(1,2,3,4,5))

def mul2 (*args):
    if len(args) == 0:
        pass
    else:
        s = 1
        for i in args:
            s = s * i
        return s
    
a = (1,2,3)
b = [1,2,3]
print (mul2 (12,5,6,71,4))
print (mul2 (b,4))
print (mul2 ('a',3,4))