# map() and reduce()
def f(x):
    return x * x
r = map (f, range(1,10)) #r is a iterator here
print (list (r))

L = []
for n in range(1,20):
    L.append(f(n))
print (L)

m = list(map(str,(range(1,10)))) #to change everything into str
print (m)

print('\n')
# now reduce

print ('reduce(f,[x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)')

from functools import reduce
def add (x,y):
    return x+y
k = reduce (add,[1,3,5,7,9])
print(k)

def fn (x,y):
    return x*10+y
d = reduce (fn,[1,3,5,7,9])
print (d)

digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


#hw
print ('\n')
def normalize (x):
    y = x[0].upper()+ x[1:].lower()
    return y
print (normalize('abcde'))

nl = ['adam','LISA','barT']
Name = map(normalize,nl)
print (list(Name))

def prod(x,y):
    return x * y
numl = range(10,14)
np = reduce(prod,numl)
print (np)

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print (reduce(fn, map(char2num, '1351279')))


#def str2float(s):
    #for i in s:
        #if i == '.':
            #print(i)
            #pass
        #else:
            #digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
            #return digits[s]

#print reduce (fn, map(str2float,'12345'))


def str2float(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    lft = s[:s.index(".")]
    rgt = s[(s.index(".") + 1):]
    s = lft + rgt
    def ft(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(ft, map(char2num,lft)) + reduce(ft, map(char2num,rgt)) / 10 ** len(rgt)

print (str2float('123.55787'))
