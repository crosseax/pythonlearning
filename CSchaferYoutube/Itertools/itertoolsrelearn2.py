# itertools relearn ii

import itertools

le1 = []
l1 = ['a','b','c','d','e']
l2 = [1,2,3,4,5]

resc = itertools.combinations(l1,4) # order no matter
for i in resc:
    le1.append(''.join(i))
print(le1)

le2 = []
l2s = []
for i in l2:
    l2s.append(str(i))
print (l2s, type(l2s))

l3s = [str(i) for i in l2]
print (l3s)

resp = itertools.permutations(l2s, 2) # order do
for i in resp: 
    le2.append(''.join(i))
    #print (i)
print (le2)



num = [0,1,2,3]
nums = ['0','1','2','3','4','5']
numst = [str(i) for i in num]
print (numst, type(numst))

ps = itertools.product(numst, numst,numst)

print ('test',list(''.join(i) for i in ps))


ps1 = itertools.combinations_with_replacement(num,3)
print (list(ps1))

