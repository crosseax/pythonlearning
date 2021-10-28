print ('hello world')

names = ['Smith','Michael','Steve','Lisa']
scores = [95,92,82,71]

d = {'Smith':95, 'Michael':92, 'Steve':82, 'Lisa':71} #{} for dictionary
print (d['Steve'])

print (d)

#one key for one value

d['Adam'] = 67
print (d['Adam'])

d['Adam'] = 76
print (d['Adam'], 'this time')

print (d)


#check if key in the list
print ('Is Thomas in d')
print ('Thomas' in d)

#use 'get' to retrieve value
print (d.get('Thomas')) #if no key, returns None
print (d.get('Thomas', -5)) #retrieve determined value if no key exist

#use "pop" to delete key
d.pop('Smith')
print (d)

#dic vs list
#key in the dic is inalterable

#set
s = set([1,2,3,4])
print (s)

s.add (4)
print (s)

s.add (5)
print (s)

#weird stuff with '&'
s.add (6 & 7)
print (s)

s.add (7 & 8 & 9)
print (s)

for i in s:
    print (i, type(i))
#weird stuff with '&'

print('\n')

#remove to remove
s.remove(0)
print (s)

#sets act like sets in math
print ('sets act like in math')
s1 = set([1,2,3])
s2 = set([2,3,4,5])
print (s1 & s2)
print (s1 | s2)

print('\n')

#str is inalterable, but list is
a = ['c','v','a','b','f'] 
a.sort()
print ('a', a)

#but for inaterable str
a = 'abc'
print (a.replace('a','A')) #replaced
print (a, type(a)) #back again
#therefore
b = a.replace('a','A')
print (b, type(b)) #its a str, b is newly created, while a is still 'abc'

