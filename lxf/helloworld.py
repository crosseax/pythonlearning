# basic shit
print('Hello World')
print('What is your name?')

# input value codes
name = input('Please enter your name here: ')
print('Hello',name )

print ('\n')
# more basic shit
print(r'''hello,\n # new line, \t = tab, and \\ is \, and \' is '
world''')
print ('\n')
print ('''line1
line2
line3''')

print('I\'m ok')
 
print ('\n')
# Conditional gay
if name == 'zjhm':
    print ('you are gay')
else: print ('your mom gay')


# Booleans True or False
# if 25 > 20
#    print ('yes')

print(3>2) # True
3<2 # False


print ('\n')
#numbers, strings, and yadayadayada
a = 123 #number
print (a)
a = 'abc' #str
print (a)

# Dividing, round down, remainder
# 10/3 = 3.3333333333333335 
# 10//3 = 3
# 11//3 = 3
# 13//3 = 4
# 10%3 = 1
# 14%3 = 2

# ord & chr, ord('A') = 65, chr(65) = A

# encode and decode 
# 'ABC'.encode('ascii) => b'ABC'
# b'ABC'.decode('ascii') => 'ABC'
# b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8') => '中文'
##### b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore') => '中'


#len() for check length of the str
print (len('abc'))
print (len(b'\xe4\xb8\xad\xe6\x96\x87' # => '中文'
))

