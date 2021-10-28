# itertools
# yeah, for iteration
# read https://www.liaoxuefeng.com/wiki/1016959663602400/1017783145987360

import itertools

natuals = itertools.count(1) # count(start, step)

for n in natuals:
    if n <= 5:
        print (n)
    else:
        break


cs = itertools.cycle('abcdef') # cycling

"""
infinite loop

for c in cs:
    print (c) # a b c d e f a b c .....
"""

ns = itertools.repeat('A',3) # repeat 3 times
for n in ns:
    print (n)


nats = itertools.count(1)
na = itertools.takewhile(lambda x : x<=10, nats)
nl = list(na)
print (nl)


for c in itertools.chain('abc','def','xyz'):
    print (c)


for key, group in itertools.groupby('AaaBbCCccDEee', lambda c: c.upper()):
    print(key, list(group))

# hw 

def pi(N):
    # calculating pi
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...    
    odd = itertools.count(start=1, step=2)

    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    ns = itertools.takewhile(lambda x: x <= 2 * N - 1, odd)
    oddlist = list(ns)

    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    for i in range(N):
        if i % 2 == 0:
            oddlist[i] = 4 / oddlist[i]
        else:
            oddlist[i] = -4 / oddlist[i]

    # step 4: 求和:
    sum = 0
    for i in oddlist:
        sum+=i
    return sum


print (pi(10),
       pi(100),
       pi(1000),
       pi(10000),sep = '\n'
       )
