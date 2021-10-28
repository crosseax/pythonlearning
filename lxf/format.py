
# use % Sign
print ('Hello, %s, person' % 'You are nice')

print('Hi, %s, you have $%d.' % ('Michael', 1000000))

# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数

print ('%2d-%02d' % (3,1))
print ('%3d-%05d' % (3,1))
print ('%2d-%05d' % (3,1))
print ('%.2f' % 3.1415926)
print ('%.5f' % 3.1415926)


print ('%1d-%05d' % (3,1))

#如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：

print( 'Age: %f. Gender: %d' % (25, True))
print( 'Age: %s. Gender: %s' % (25, True))

print('growth rate: %d%%' % 7)

#use format()

print ('Hello, {0}, I have gained {1:.2f}%'.format('Tim',18.3678))

print ('\n')



#use f-string

r = 2.5
s = 3.14159265 * r ** 2
print (f'The area of a circle with radius {r} is {s:.3f}')

print ('\n')

s1 = 72
s2 = 85 
rate = (s2 / s1 - s2 // s1)*100
print ('%.2f%%' % rate)
print ('Hello, %% Sign, your grade has raised by %.2f %%' % rate)
print ('Hello, Format, your grade has raised by {0:.2f} %'.format(rate))
print (f'Hello, f-string, your grade has raised by {rate:.2f}%')