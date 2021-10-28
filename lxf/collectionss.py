# collections module 
# for more read https://docs.python.org/3/library/collections.html

import collections


#namedtuple 

from collections import namedtuple

"""
namedtuple to create customized tuple object
namedtuple('name', [properties list])
"""

Point = namedtuple('Point', ['x','y'])
p = Point(1,2)
print (p.x, p.y)
print (isinstance(p, Point))

Circle = namedtuple('Circle', ['x', 'y', 'r']) 


# deque

from collections import deque

"""
deque is to efficiently insert and delete the elements in lists
"""

q = deque(['a','b','c'])
q.append('x')
print (q)
q.appendleft('y')
print (q)



# defaultdict

from collections import defaultdict

"""
when using dict, if Key does not exist, therefore KeyError
if want to return a default value when Key no exist, use defaultdict
"""

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print (dd['key1'],
       dd['Key2'], sep = '\n')



# OrderedDict

from collections import OrderedDict

"""
when using dict, Keys are orderless
if want to order the Keys for iteration
use OrderedDict
"""

lis = [('a', 1), ('b', 2), ('c', 3)]
d = dict(lis)
print (d)
od = OrderedDict(lis)
print (od)

od2 = OrderedDict()
od2['x'] = 1
od2['y'] = 2
od2['z'] = 3
print (od2)

odl = list(od2.keys()) # return keys by inserting order
print (odl)

l = odl 

odlr = l.reverse()
print (type(odl),type(l),odlr) # questionable, reverse list didnt work as expected

"""
to create a FIFO dict with OrderedDict


class LastUpdatedOrderedDict (OrderedDict):
    super(LastUpdatedOrderedDict, self).__init__()
    self._capacity = capacity
    
def __setitem__ (self, key, value):
    containsKey = 1 if key in self else 0
    
    if len(self) - containKey >= self._capacity:
        last = self.popitem(last = False)
        print('remove:', last)
        
    if containsKey:
        del self[key]
        print('set:', (key, value))
    else:
        print ('add:' (key, value))
    OrderedDict.__setitem__(self, key, value)
    
"""



# ChainMap

from collections import ChainMap

"""
ChainMap is logicalize dict
"""

import os, argparse

# 构造缺省参数:
defaults = {
    'color': 'red',
    'user': 'guest'
}

# 构造命令行参数:
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = { k: v for k, v in vars(namespace).items() if v }

# 组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])


"""
当传入命令行参数时，优先使用命令行参数：

$ python3 use_chainmap.py -u bob
color=red
user=bob
"""


# Counter

from collections import Counter

"""
Counter is yeah, a counter
"""

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print ('this is c', c) # Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})

c.update('hello world') # adding more things to count
print (c) # Counter({'r': 3, 'o': 3, 'l': 3, 'g': 2, 'm': 2, 'p': 1, 'a': 1, 'i': 1, 'n': 1, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'd': 1})
    
dc = dict(c)
kl = []
vl = []
for key, value in dc.items():
    kl.append(key)
    vl.append(value)

print (kl,vl)

print (max(vl))
"""
text = 'abbcc'
c2 = Counter()
for ch in text:
    c2[ch] = c2[ch] + 1
print (c2)
dc2 = dict(c2)
print (dc2)
kl = []
vl = []
for key, value in dc2:
    kl.append(key)
    vl.append(value)
print (vl)
print (max(vl))




"""

