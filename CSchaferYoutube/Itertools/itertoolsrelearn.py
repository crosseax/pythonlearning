# itertools relearm

import itertools

Counter = itertools.count()

"""
print (next(Counter)) # 0
print (next(Counter)) # 1
print (next(Counter)) # 2
print (next(Counter)) # 3
print (next(Counter)) # 4
print (next(itertools.count())) # 0
print (next(itertools.count())) # 0
print (next(itertools.count())) # 0
print (next(Counter)) # 5
print (next(Counter)) # 6
print (next(Counter)) # 7
"""

data1 = ['a', 'b', 'c', 'd']

data1Count = zip(itertools.count(start=10,step=-2.5), data1) # by default start 0, step1

print (type(data1Count))
print (data1Count)

data2 = range(10)
#data2Count = list(itertools.zip_longest(range(10), data1))

countcycle = itertools.cycle(('a','b'))
print (next(countcycle))
print (next(countcycle))
print (next(countcycle))
print (next(countcycle))
print (next(countcycle))
print (next(countcycle))


def tri(n):
    return n ** 3

squares = map(tri, range(10))
print (list(squares))

def tii (n,m):
    try:
        return n**m
    except:
        pass
some = map(tii, range(10), range(11))
print (list (some))

sq = itertools.starmap(tii, [(3,5),(5,2),(11,3)])
print (list (sq))



