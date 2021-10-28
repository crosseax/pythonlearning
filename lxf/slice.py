# from now on the real stuff begin
# advanced but simple thinking process is constantly required

# slice

L = ['Michael','Tommy','Sam','Stuart','Huang','Pepe']

# get the first element
# way one
print ([L[0],L[1],L[2]])

# way two
r = []
n = 3
for i in range(n): # range(n) means from 0 to n-1
    #print (n, i, L[i], r)
    r.append(L[i]) # n=0, get L[0], put into r, then loop
    #print (r)
print (r)

# now using slice
print (L[0:3]) # getting from pos 0 to 3 (not include 3)
print (L[:3]) # works too
print (L[1:3]) # pos 1 to 3, also not including 3

print (L[-2:-1]) # second last to the last
print (L[-2:]) # or this

# now lets see
P = list(range(100))

print (P)
print (P[::2]) # every other one
print (P[::3]) # every third one, you get the idea

# works on str too

S = 'ABCDEFGHIJKLMN'
T = S[::3]
print (S)
print (T)

print ('\n')

#hw
STR = '         ASDBAASDFASDGAG    '

def trim (x):
    while x [:1] ==' ':
        x = x[1:]
    while x [-1:] == ' ':
        x = x [:-1]
    return x 

print (trim (STR))