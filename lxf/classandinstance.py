# class and instance
# example as student again
class Student(object):
    pass

bart = Student()
print (bart) # <__main__.Student object at 0x0000027AB748A730>
print (Student) # <class '__main__.Student'>

# now we can give the instance 'bart' a properties, which could be a variable

bart.name = 'Bart Simpson'
print (bart.name) # Bart Simpson

# cuz the class can be used as module, 
# we can give it must-have properties when creating it
class Student(object):
    def __init__(self, name, score): # here, name and score are must-have properties, self is the instance itself
        self.name = name
        self.score = score

bart = Student('Bart Simpson', 60) # since the instance has two must-have properties, when creating instance, such properties must be included
print (bart.name) # Bart Simpson
print (bart.score) # 60

# data encapsulation
# without encapsulation, 
# the data is called through function
def print_score(std):
    print ('%s: %s' % (std.name, std.score))
print_score(bart) # Bart Simpson: 60

# with encapsulation, we can just use method to call the data, 
# which is linked to class Student
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # function below is defined inside the class, which is encapsulated
    def print_score(self):
        print ('%s: %s' % (self.name, self.score))

    # another benefit of encapsulation is that 
    # we can just add new method to the class here in the class
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        elif self.score >= 70:
            return 'C'
        elif self.score >= 60:
            return 'D'
        else:
            return 'F'

bart = Student('Bart Simpson', 75)
bart.print_score() # Bart Simpson: 75
print (bart.get_grade()) # C

smith = Student('Smith Smith', 95)
smith.print_score() # 95
print (smith.get_grade) # <bound method Student.get_grade of <__main__.Student object at 0x0000028D40321F70>>
print (smith.get_grade()) # A