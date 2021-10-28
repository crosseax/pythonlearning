# return functions 
# so basically, you can return the function as result

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1,2,3,5,6,7)
print (f) # the result is not a quatitative sum, its a function
print (f()) # now its a quantitative result
print (lazy_sum(1,2,3,4,5,6,7,8,9,10), 'function') # function
print (lazy_sum(1,2,3,4,5,6,7,8,9,10)(), 'quantitative result')

# closure, when return lazysum return sum, the parameters and variables are stored
f1 = lazy_sum(1,2,3,4,5)
f2 = lazy_sum(1,2,3,4,5)

print (f1(), f1)
print (f2(), f2)
print (f1()==f2(), f1==f2)

# so far so good? maybe

print ('\n')

# now, for the 'closure'

def count():
    fs = []
    for i in range (1,4):
        def f():
            return i* i
        fs.append(f)
    return fs

g1, g2, g3 = count()
print (g1(),g2(),g3()) # why is it all 9?
# because we used the variable i
# when return all the functions, all the i has became 3 
# wtf does this above even mean

# in Conclusion:
# include NO loops within the Return functions
# NEVER LOOP IN RETURN FUNCTIONS
# OR ANY VARIABLE THAT WILL LATER BE CHANGED

# if you do have to
# create another function
def count2():
    def k(j):
        def l():
            return j * j
        return l
    fs = []
    for i in range (1,4):
        fs.append(k(i))
    return fs

h1, h2, h3 = count2() 
print (h1(),h2(),h3())

# hw

def createCounter():
    i = []
    def counter():
        i.append(len(i) + 1)
        return i[-1]
    return counter

c1 = createCounter()
c2 = createCounter()
print (c1(),c1(),c1(),c1(),c1(),c1())
print (c1(),c1())
print (c2(),c2(),c2(),c2(),c1(),c1())





