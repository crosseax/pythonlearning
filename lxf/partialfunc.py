# partial functions
# this is DIFFERENT from the MATHEMATICAL PARTIAL FUNCITONS

# base 10, base 2, base 16, numerical convertion
i = int ('12345')
print (i)

ib8 = int ('12345', base = 8) # what number in base 8 is 12345
print (ib8)
i8 = int ('12345', 8)
print (i8)
i16 = int ('12345', 16) # what number in base 16 is 12345
print (i16)


def int2(x, base=2):
    return int(x, base)

b21 = int2('100000')
b22 = int2('111111')
print (b21, b22)

print('\n')
print ('now lets do it partial functions style')

import functools

int3 = functools.partial(int, base = 3)
b31 = int3('12111211')
b32 = int3('1111101110111')
b33 = int3('10')
print (b31, b32, b33)


print ('\n')
# you can also use *args and **kw
int2 = functools.partial(int, base = 2)
# is the same as
kw = {'base': 2}
int ('10010', **kw)

# when doing below
max2 = functools.partial(max, 10)
m1 = max2(5,6,7)
# this is the same as
m2 = max2(5,6,7,10) # because 10 is added as an args
# so its the same as
args = (10,5,6,7)
m3 = max(*args)
print (m1, m2, m3)


