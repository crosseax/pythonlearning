# real properties and class properties
# whatever the english words for this is
# for more check https://www.liaoxuefeng.com/wiki/1016959663602400/1017594591051072

class Student(object):
    def __init__(self, name):
        self.name = name 

s = Student('Bob')
s.score = 90
print (s) # <__main__.Student object at 0x0000023AB210D940>


# what if we want to link a property to Student
class Student(object):
    name = 'Student'

s = Student()
print (s.name) # Student, this is a property for class
s.name = 'Michael'
print (s.name) # Michael, this is a property for instance

print (Student.name) # Student, but the class property is not override, you can still call it out

del s.name # del for delete
print (s.name) # Student, the instance is deleted, now back to the class

# hw

class Student(object):
    count = 0
    def __init__(self,name):
        self.name = name
        Student.count = Student.count + 1
        self.count = Student.count
        
        # Student.count += 1 # this also works


if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')







