print("Hello World")

def trig():
    L1 = [1]
    n = 0
    while n<10:
        yield L1
        L1.append ( 0 )
        L2 = list(reversed(L1))
        #print (L1,L2)
        L1 = [a+b for a,b in zip(L1,L2)]
        n = n+1
print(trig())
for i in trig():
    print (i)
    
