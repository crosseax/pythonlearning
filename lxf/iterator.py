#Iteration 

T = {'a':1, 'b':2, 'c':3}
for i in T:
    print (i)

for value in T.values():
    print (value)

# it also works on str

STR = 'abndk'
for ch in STR:
    print (ch)

print('\n')
# use collections.abd to see if a thing is iterable or not (notice for caps)
from collections.abc import Iterable
print (isinstance ('abc', Iterable))
print (isinstance([1,2,3],Iterable))
print (isinstance(123, Iterable))

print('\n')

# use enumerate to make index

for i, value in enumerate(['A','B','C']):
    print (i, value)

# for multiple variables

for x, y in [(1,2),(3,1),(3,9),(4,15),(5,5)]:
    print (x, y)

print ('\n')

#hw

LIST = [1,2,6,2,3,6,0,-3,8,12,35,612,13,34]

def findmaxandmin(L):
    if L == []:
        return None, None
    else:
        a = b = L[0] #assign the first value in L to a and b
        print ('yes',a,b) 
        for x in LIST:
            print (a,b)
            if x > a:
                a = x 
            if x < b:
                b = x
        # return ('max = %.2f, min = %.2d' % (a,b)), %f for flout, %d for number
        return (a, b)

print (findmaxandmin(LIST))


