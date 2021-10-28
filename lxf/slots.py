# __slots__

class Student(object):
    pass

# to give the instance a property
s = Student()
s.name = 'Michael'
print(s.name) # 'Michael'

# to give the instance a method

def set_age(self,age):
    self.age = age

from types import MethodType

s.set_age = MethodType(set_age, s) #setting a method to the instance
s.set_age (25) # to use the method
print (s.age) # 25, to check the result

# but the other one wont work, without setting the method

# s2 = Student()
# s2.set_age(25)  # AttributeError: 'Student' object has no attribute 'set_age'

# in order to give method to every instance,
# we can give method to the class

def set_score(self, score):
    self.score = score

Student.set_score = set_score # setting a method to the class
# such thing is usually written inside the class
# but with dynamic language like python
# adding them after the class definition would also be possible

s1 = Student()
s2 = Student()
s1.set_score(100) 
s2.set_score(95) 
print (s1.score, s2.score) # 100 95

# __slots__
# to limit the properties of the instance

class Student(object):
    __slots__ = ('name','age') # using tuple to limit the properties' name

s = Student() 
s.name = 'Michael' 
print (s.name) # Michael
# s.age = 25 
# s.score = 99 # AttributeError: 'Student' object has no attribute 'score'

# __slots__ dont work for the subclass

class GradStudent(Student):
    pass

s5 = GradStudent()
s5.score = 9999
print (s5.score) # 9999


### use @property, decorator, 
### for more, check https://www.liaoxuefeng.com/wiki/1016959663602400/1017502538658208#0

class Student2(object):
    
    def get_score(self):
        return self.get_score
    
    def set_score (self, value):
        if not isinstance(value, int):
            raise ValueError('Score must be an integer!')
        if value <0 or value > 100:
            raise ValueError('Score must between 0~100!')
        self.score = value
    
s = Student2()
s.set_score (60) # doable
s.get_score () 

# s.set_score (9999) # ValueError: Score must between 0~100!

# decorator, 
# @property is to change a method into property
print ('\n')
class Student3(object):

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student3 ()
s.score = 60 # OK，实际转化为s.set_score(60)
s.score # OK，实际转化为s.get_score()

# also we can define readonly, readable, and writable

class Student4(object):
    
    @property
    def birth (self):
        return self._birth

    @birth.setter 
    def birth (self, value):
        self._birth = value

    @property
    def age (self):
        return 2021 - self._birth

# above, birth is readable and writable (with setter)
# but the age is readonly

s = Student4()
s.birth = 1995 # you can write
print (s.birth) # 1995, you can read
print (s.age) # 26, read only



# hw


class Screen(object):
    
    @property
    def width(self):
        return self._width

    @width.setter
    def width (self, value):
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter 
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height

sc = Screen()
sc.width = 1920
sc.height = 1080

print (
    sc.width,
    sc.height,
    sc.resolution
)

