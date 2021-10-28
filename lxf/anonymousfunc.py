# anonymous function
numL = range(1,10)
L = list(map(lambda x: x*x, numL))
print (L)

# so in this case
# lambda x: x*x is actually below
def f(x):
    return x*x
print (f(5))
# so anonymous function has no return
# and it also has no name to cause conflict with others

g = lambda x : x * x
print (g)
print (g(10))

# you can also return the anonymous functions
def build(x,y):
    return lambda: x*x + y*y
print (build(50,30))
print (build(50,30)())

print ('\n')
#hw
def is_odd(n):
    return n % 2 == 1

P = list(filter(is_odd, range(1,20)))
print (P)

r = list(filter(lambda x:x%2==1, range (1,20)))
print (r)