# advanced functions or higher-order function

# for example abs
print (abs(-18))
print (abs) #built-in function

x = abs (-10)
print (x)
f = abs
print (f)
print (f(x))

# but if you let abs = 10 (variable), then you're fucked

def add(x,y,f):
    return f(x) + f(y)

def mul(x,y,f):
    return f(x) * f(y)

print (add (-5,6,abs))
print (mul (-9,6,abs))
