#define functions
def my_grade(x):
    if x <=100 and x >= 60:
        return ('passed')
    elif x < 60 and x >= 0:
        return ('failed')
    elif x < 0 or x > 100:
        return ('wrong grade') # put return none or return, will return none

print (my_grade(60))
print (my_grade(59))
print (my_grade(100))
print (my_grade(0))
print (my_grade(-1))
print (my_grade(101))

# you can import functions using 'import'

#null function
def nop():
    pass # can also be used in conditional codes
print (nop())

#isinstance worry later
#def myabs(x):
#    if not isinstance(x(int,float)):
#        raise TypeError ('bad operand type')
#    if x >= 0:
#        return x
#    else:
#        return -x

#print (myabs('abd'))
#print (myabs(41))
#print (myabs(-5))

#return multiple values
import math
def move (x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move (100, 100, 60, math.pi / 6)
print (x, y)
r = move (100, 100, 60, math.pi / 6)
print (r) #return as a tuple

print ('\n')

#quadratic formula hw
def quad (a,b,c):
    y = b ** 2 - 4 * a * c
    if y < 0:
        return ('(Complex answer)')
    elif a == 0:
        xx = - c / b
        return xx, 'a = 0, there\'s only one solution'
    else:
        x1 = (- b + math.sqrt(y)) / (2 * a) 
        x2 = (- b - math.sqrt(y)) / (2 * a) 
        return x1, x2


r1 = quad (1,1,1)
r2 = quad (4,18,2)

print (quad(0,2,2))
print (quad(2,2,2))
print (r1, type(r1))
print (r2, type(r2))
print (r1,r2)



