# list
classmates = ['Michael', 'Bob', 'Tracy', 'Steve']
print(classmates)
print(len(classmates))

# list start with 0, -1 means first to the last
print (classmates[0], classmates[1], classmates[2], classmates[3])
print (classmates[-1], classmates[-2], classmates[-3], classmates[0])

#list.append, add
classmates.append ('Adam')
print (classmates)

# list.insert(#, 'object') to insert
classmates.insert (1,'Jim')
print (classmates)

# .pop() to delete the last one in the list
classmates.pop()
print (classmates)
#Adam gone, fuck you adam we all hate you

# .pop(i) for the order delete
classmates.pop(2) #good bye bob
print (classmates)

#list.[i] = xxx to overwrite
classmates[1] = 'Pam' #Jim replaced by Pam
print (classmates)

#some ways lists can combine and include, or empty
A = ['apple', 123, True]
B = ['python, java', 'c++', A, 'AK47']
C = []
print (A, len(A))
print (B, len(B))
print (C, len(C))

print (B[2][1]) # = print A[1]

print('\n')

#tuple
#tuple is list with unchangeable direction, safer, elements of the list within tuple can be changed
t1 = (1,2,3)
t2 = ()
t3 = (4,5,B,7)
t4 = (10,)
print (t1, len(t1))
print (t2, len(t2))
print (t3, len(t3))
print (t4, len(t4))

print ('careful below')
print (t3)

A.insert(2, 'ok')
B.append('tuple')

print (t3, len(t3))
