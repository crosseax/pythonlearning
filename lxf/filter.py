# filter functions

def is_odd(n):
    return n % 2 == 1

L = range(1,21)
Y = filter (is_odd,L)
T = list(filter(is_odd,L))
print (Y)
print (T)


def not_empty(s):
    return s and s.strip()

Ls = ['A','B','','C',None,'TE','   '] # no int
NE = list (filter(not_empty,Ls))
print (NE)

print('\n')
# so to use filter to get prime numbers using the Sieve of Eratosthenes
# say, a number series that is odd starting from 1

def threeodd_iter(): # odd numbers generators
    n = 1
    while True:
        n = n + 2
        yield n
print (type(threeodd_iter()))

def ndiv (n): # if a number x is not divisible by n, return that x
    return lambda x : x % n > 0

#in other words, if filter(ndiv), means wipe out all the number x divisible by n

def primes():
    yield 2 
    num = threeodd_iter() # starting list (as a generator)
    while True:
        n = next (num) # back to the first numb in the list
        yield n
        num = filter (ndiv(n),num) # get a new number to do

Pri = []

for n in primes():
    if n < 1000:
        Pri.append(n)
    else:
        break 

print (Pri)

print('\n')
# palindromes, so a number reads the same frontward or backward like 13431

def is_palin(n):
    sn = str(n)
    return sn == sn [::-1]
        
PALI = list (filter (is_palin, range (1,201)))
print (PALI)
