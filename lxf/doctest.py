# word tests

# also bro, read https://www.liaoxuefeng.com/wiki/1016959663602400/1017605739507840

# JUST READ THE FUCKING LINK

import re
m = re.search('(?<=abc)def', 'abcdef')
print (m.group(0))


def abs(n):
    '''
    Function to get absolute value of number.
    
    Example:
    
    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''
    return n if n >= 0 else (-n)

print (abs(17))

