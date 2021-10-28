# sorted, as sorting algorithm

N = [-13,53,21,1,-599,0,0,5,8,77]
sN = sorted(N) # number sort from small to big
print (sN)

# it takes keys cuz it higher-order function
sabsN = sorted(N, key = abs) # number sort from whose absolute value from small to big
print (sabsN)

# so like this
# => [5, 9,  12,  21, 36] sort abs first
#    |   |   |    |    | 
# => [5, 9, -12, -21, 36] then result
# 

w = ['bob', 'about', 'Zoo', 'Credit'] # ASCII, A<Z<a<z
s1 = sorted (w)
print (s1)

s2 = sorted (w, key = str.lower) # lower first then sort
print (s2)

s3 = sorted (w, key = str.lower, reverse = True) # add reverse
print (s3)

print ('\n')
# hw

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print (L[1])

def byname(lst):
    return lst[0] 

def byscore(lst):
    return -lst[1]

Ln = sorted (L, key = byname)
Ls = sorted (L, key = byscore)

print (Ln)
print (Ls)




