# Object Oriented Programing
# or, OOP

# for example, the regular below
std1 = {'name': 'Michael', 'Score': 98}
std2 = { 'name': 'Bob', 'score': 81 }

def print_score(std):
    print ('%s: %s' % std['name'], std['score'])


# or OOP
# thinking student as a object, which contains two properties: name and score
# we first create student object, then send it a print_score command, to let the object run it themselves

class Student(object):

    def __init__ (self, name, score): # __init__ is to initialize the properties, to make them default
        self.name = name
        self.score = score

    def print_score (self):
        print ('%s, %s' % (self.name, self.score))

# to send object the command is the same as using its related function, which is called method

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

bart.print_score()
lisa.print_score()

# Abstract idea like Student is a Class
# according to Class we create Instance, which here is bart and lisa

# A very good example below, comment at https://www.liaoxuefeng.com/wiki/1016959663602400/1017495723838528#0

# Say God is creating human (Class), Adam (Instance), which has height, weight, and age (properties)
# __init__ is to initialize the properties, to make them default

class Human(object):
    # so to initialize the properties
    def __init__(self, height, weight, age):
        self.height = height
        self.weight = weight
        self.age = age

    # to define the skills of human
    def domath(self):
        print ('You have abilities to do math')
    def eat(self):
        print ('You can eat')

# now to create instance
Adam = Human(170,60,20)
Eva = Human(160,55,18)

# now the instance to use skills
Adam.domath()
Eva.eat()