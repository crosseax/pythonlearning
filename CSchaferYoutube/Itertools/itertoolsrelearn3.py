# itertools relearn 3

import itertools

l1 = ['time', 'place', 'height']
l2 = [1,2,3,4,5,6]
l3 = ['a','b','c','d']

res1 = itertools.chain (l1, l2, l3)
print (list(res1))



combined = list(itertools.chain (l1, l2, l3))
print (combined)


res2 = itertools.islice(combined, 1, 8, 2) # stuff, start, end, step
print (list(res2))


select = [True, True, False, True, False, True, True]

ress = itertools.compress(combined, select)

print (list (ress))

#compress() takes boolean value, filter use functions to define boolean

def lt5(n):
    if n < 5:
        return n

numl = range(-2, 10)

print (numl)

n5 = filter(lt5, numl)
print (n5)

"""
n6 = itertools.dropwhile(lt5, numl) 
print(list(n6))

print (bool(1))
print (bool(0))
print (bool(-1))
print (0<5)

"""

"""
ln = range (10)

ac = itertools.accumulate(ln)

for i in ac:
    print (i)

"""
"""
import operator

def iq_test(numbers):
    prod = 1
    n = 0
    for n in numbers:
        prod = prod * n
    if prod % 2 == 0:
        for i in numbers:
            n = n + 1
            if i % 2 == 0:
                return n
    else:
        for i in numbers:
            n = n + 1
            if i % 2 == 1:
                return n
    return 


print (iq_test ([1,1,2,1,1]))
"""

ls1 = ("2 4 7 8 10")
ls2 = ("1 2 2 6")


def iq_test(numbers):
    nls = numbers.split()
    nl = []
    for n in nls: 
        nl.append(int(n))
    print (nl)
    ev = []
    od = []
    for x in nl:
        if x % 2 == 1:
            od.append(x)
        else:
            ev.append(x)
    if len(ev) == 1:
        return nl.index(ev[0]) + 1
    else:
        return nl.index(od[0]) + 1

iq_test(ls1)
iq_test(ls2)