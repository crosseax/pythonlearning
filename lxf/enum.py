# enum

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print (name, '=>', member, ',', member.value)



print ('\n')


from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(day1) # Weekday.Mon
print(Weekday.Tue) # Weekday.Tue
print(Weekday['Tue']) # Weekday.Tue
print(Weekday(3)) # Weekday.Wed
print(Weekday.Tue.value) # 2
print(day1 == Weekday.Mon) # True
print(day1 == Weekday.Tue) # False
print(Weekday(1)) # Weekday.Mon
print(day1 == Weekday(1)) # True

for name, member in Weekday.__members__.items():
    print(name, '=>', member)



print ('\n')

# hw

from enum import Enum, unique

@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
