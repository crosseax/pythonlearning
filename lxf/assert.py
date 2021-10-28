# assertion
# a primal way to locate the problem
try:
    def foo(s):
        n = int(s)
        print ('>>> n = %d' % n)
        return 10 / n

    def main():
        foo('0')

    main()

except:
    pass

# second way, assertion
try:
    def foo(s):
        n = int(s)
        assert n != 0, 'n is a zero'
        return 10/n

    def main():
        foo('0')

    main()

except:
    pass

# when run .py, use -0 python err.py to close the assertions

# third way, use logging to record the error

try:
    import logging
    logging.basicConfig(level=logging.INFO)

    s = '0'
    n = int(s)
    logging.info ('n = %d' % n)
    print (10/n)
except:
    pass

# for more information: 
# visit https://www.liaoxuefeng.com/wiki/1016959663602400/1017602696742912

# fourth way
# use pdb
# use python -m pdb pdb.py
# see pdb.py
# use q to exit()




# pdb.set_trace()
import pdb

s = '0'
n = int(s)
print (10/n)








