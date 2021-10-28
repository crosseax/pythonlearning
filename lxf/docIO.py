# IO = Input/Output
# doc IO 
# for more, read https://www.liaoxuefeng.com/wiki/1016959663602400/1017607179232640

f = open('/Users/qq417/Desktop/Python/Python2021/hellotext.txt', 'r') 
f = open('./hellotext.txt', 'r')

# cuz in python you cant use \
# three ways to clear file locations
# 1 open('/Users/qq417/Desktop/Python/Python2021/hellotext.txt', 'r')
# 2 open(r'\Users\qq417\Desktop\Python\Python2021\hellotext.txt', 'r')
# 3 open('\\Users\\qq417\\Desktop\\Python\\Python2021\\hellotext.txt', 'r')

# if file dont exist
# FileNotFoundError: [Errno 2] No such file or directory: '/Users/michael/test.txt'

# if opened
f.read() # read the whole file

#f.close() # yeah, close it


try:
    f = open('./hellotext.txt', 'r')
    print (f.read())
finally:
    if f:
        f.close()

print ('\n')
# with 
with open('./hellotext.txt' , 'r') as f:
    print (f.read(), '\n')
    
# this is the same as try...finally above

# .read(size) to prevent ram from exploding
# .readlines() to read the specific line

with open('./hellotext.txt' , 'r') as f:
    n = 1
    for line in f.readlines():
        print (line.strip(), 'This is line %s.' % n)
        n = n + 1

print ('\n')
# to read binary files, for example, jpg

# with open('./thejpg1.jpg', 'rb') as f:
    # print (f.read())
    # for line in f.readline():
        # print (line)


# to read non UTF-8 file
# you need a encoding function to open()

with open('./hellotext.txt', 'r', encoding='gbk') as f:
    print (f.read(), '\n' ,'After encoding', '\n')

with open('./readtext.txt', 'r', encoding='gbk', errors='ignore') as f:
    print (f.read(), '\n','After ignoring the errors')

print ('\n')
# writing the files

with open('./hellotext2.txt', 'w') as f: # 'wb' for binary files
    f.write('Hello world again, this is writing from python.')
    f.close()
    
with open('./hellotext2.txt', 'r') as f:
    print (f.read(), '\n')





#hw
with open ('./iohwfile.txt','r') as f:
    s = f.read()
    st = str(s)
    print (st)

# extra reading






