#List Comprehensions, to generate list

L1 = [1,2,3,4,5,6,7,8,9,10]
L2 = list(range(1,11)) 
print (L1, L2)

# ways creating list with calculations
L3 = [1*1, 2*2, 3*3, 4*4, 5*5]
L4 = []
for x in range(1,6):
    L4.append (x*x)

L5 = [x*x for x in range (1,6)] #or throw condition in there 
print (L3,L4,L5)
print ('\n')

# with more condition, say, picking odd numbers

L6 = [x*x for x in range (1,21) if x % 2 == 0]
print (L6)
print ('\n')

# you can also line two or more loops up
L7 = [x+y for x in 'abcd' for y in '567']
L8 = [m+n+p for m in 'ABC' for n in 'XYZ' for p in '123']
print (L7)
print (L8)

print ('\n')
#so its super useful for listing menu etc, we'll worry about os later
import os 
k = [d for d in os.listdir('.')]
print (k)

# can also loop among multiple typles of variables
d = {'x':'A','y':'B','z':'C'} #this is dictionary
print (d.items())
for k,v in d.items():
    print (k, '=', v)
t = [k+'='+v for k,v in d.items()] # so to throw'em in the list
print (t)
print ('\n')

T1 = ['Hellow', 'World', 'IBM', 'Apple']
t1 = [s.lower() for s in T1] #s.lower for turning s into lower case
print (t1)
print ('\n')




# now, for if ... else

A1 = [x*x for x in range(1,11) if x % 2 == 0] 
# you CANNOT add else above
# you also CANNOT put if before for
print (A1)

# to do below
A2 = [x if x % 2 == 0 else -x for x in range (1,11)]
print (A2)
# read above: from range(1,11) add x if even, -x if odd
# so multiple condition, if else before for


print ('\n')

#hw

#tips, use isinstance to see if something is something

A10 = ['Hello', 'World', 18, 'Apple', None]

#break it down
Ans1 = []
for x in A10:
    if isinstance(x, str) == True:
        Ans1.append(x.lower())
    else:
        Ans1.append(x)
print (Ans1)

#or 

Ans2 = [x.lower() if isinstance(x, str) else x for x in A10]
print (Ans2)

Ans3 = [x.lower() for x in A10 if isinstance(x, str)]
print (Ans3)


