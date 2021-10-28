# things that can be used to loop/iterate
# list, tuple, dict, set, str, etc
# generators and functions
# for, interable
# also can use isinstance() to see if something is iterable or not

from collections.abc import Iterable
print (isinstance([], Iterable))
print (isinstance({}, Iterable))
print (isinstance('abc', Iterable))
print (isinstance((x for x in range(10)), Iterable))
print (isinstance(100, Iterable))

print ('\n')
# iterator is different
from collections.abc import Iterator
print (isinstance((x for x in range(10)), Iterator))
print (isinstance([], Iterator))
print (isinstance({}, Iterator))
print (isinstance('abc', Iterator))

print ('\n')
# to change those non-interator to iterator you can use iter()
print (isinstance(iter([]), Iterator))
print (isinstance(iter({}), Iterator))
print (isinstance(iter('abc'), Iterator))


# iterator is for a data stream, so they can be used upon next()
# until StopIteration Error
