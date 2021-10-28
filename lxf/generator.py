# generator
# List and generator, [] and ()
L = [x*x for x in range(10)] # list
print (L)
g = (x*x for x in range(10)) # generator
print (g)

# generator can save you shit tons of space, comparing to list

# use next() to print value out of generator, but each time the result is, next
# so 
print (next(g)) # g value 1
print (next(g)) # g value 2 
print (next(g)) # g value 3
print (next(g)) # and so on
print (next(g))
print (next(g))

print ('\n')
# for short
g = (x*x for x in range(10))
print (g)
for n in g:
    print (n)

print ('\n')
# fibonacci, for example, not using generator
def fib (max):
    n,a,b = 0, 0, 1
    while n < max:
        print ('f',b)
        a, b = b, a + b
        n = n + 1
    return 'now n = %d done' % (max)

print (fib(10))

# using generator, using yield 
def fibg (max):
    n,a,b = 0, 0, 1
    while n < max:
        yield b # change print(b) to this making shit into generator
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fibg(10) # this is a generator now
print ('fib generator here below')
print (f) # f = (1,1,2,3,5,8,...) no including done

for i in f:
    print ('fg', i)

print ('\n')
# to see how it works
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
o = odd()
print (next(o))
print (next(o))
print (next(o))

for i in odd():
    print ('this',i) # i dont get this part

print ('\n')
for n in fibg(10):
    print (n)


g = fibg(10)
while True:
    try:
        x = next (g)
        print ('g:', x)
    except StopIteration as e:
        print ('Generator return value:', e.value)
        break


print ('\n')
#hw, pascal triangle
#without using generator
def triangles(x):
    list=[1] 
    for i in range(x): 
        print(list) 
        newlist=[] 
        newlist.append(list[0]) 
        for i in range(len(list)-1): 
            newlist.append(list[i]+list[i+1]) 
        newlist.append(list[-1]) 
        list = newlist

T = triangles(10)
