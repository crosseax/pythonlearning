#for
names = ['Mike','Bob','Tracy','Huang']
for name in names:
    print (name)


sum = 0
nums = [1,2,3,4,5,6,7,8,9,10]
for x in nums:
    sum = sum + x
    #print (x)
print (sum)


#list(range(5)) = [0,1,2,3,4]
print(list(range(10)))

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

#while
sum = 0
n = 99
while n > 0:
    sum = sum + n 
    n = n - 2
print (sum)

L = ['Bart','Lisa','Adam']
for name in L:
    print ('Hello ',name,'!',sep='')
    print ('Hello again %s!' % name)

#break
n = 1
while n < 200:
    if n > 20:
        break
    print (n)
    n = n + 1
print ('END')


#continue
n = 0
while n < 10:
    n = n + 1
    print (n)


n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    else:    
        print (n,'odd1') 
        
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print (n,'odd2',sep='')



