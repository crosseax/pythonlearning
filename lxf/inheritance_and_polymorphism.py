# inheritance and polymorphism
# inheritance
# Subclass, Base class, and Super class

print ('Inheritance first')
class Animal(object):
    def run(self):
        print ('Animal is running')

class Dog(Animal): # in this case, Animal is Dog's Base class, Dog is Subclass
    pass

# good thing in inheritance is that Subclass has all the functions in Base class
# in this case, Dog has all the functions of Animal

dog = Dog()
dog.run() # Animal is running

# we can also add some functions

class Dog(Animal):
    def eat(self):
        print ('Dog is eating')

dog2 = Dog()
dog2.run() # Animal is running, it can use Base class functions
dog2.eat() # Dog is eating, it can also use its own subclass functions

print ('\n')
print ('Now, for Polymorphism')
# polymorphism

class Dog(Animal):
    def run(self): #this function is in the Base class, now in the subclass, it has been polymorphed
        print ('Dog is running')
    def eat(self):
        print ('Dog is eating')

dog3 = Dog()
dog3.run() # Dog is running
# when polymorphed, subclass object has priority to do Subclass functions first
# to further illustrate

a = list()
b = Animal()
c = Dog()

# isinstance to check its type
isinstance(a, list) # True
isinstance(b, Animal) # True
isinstance(c, Dog) # True
print (isinstance(c, Animal)) # True, Subclass is Base class
print (isinstance(b, Dog)) # False, Base class is not Subclass

# to understand the benefit of polymorphism
def run_twice(animal2):
    animal2.run()
    animal2.run()

run_twice(Animal())
# Animal is running
# Animal is running

run_twice(Dog())
# Dog is running
# Dog is running

class Horse(Animal):
    def run(self):
        print ('Horse is running, also')

run_twice(Horse())
# Horse is running, also
# Horse is running, also

# so adding a new Subclass, 
# there's no need to do any change to the Base class,
# there's also no need to do any change to run_twice function,
# which is not defined inside the Base class, Animal

# also, Subclass can have Subclass

class Husky(Dog):
    def smile(self):
        print ('Husky is smiling')

chuichui = Husky()
chuichui.smile() # Husky is smiling
chuichui.eat() # Dog is eating
chuichui.run() # Dog is running

# Static vs Dynamic Programming Language
# for more, check https://www.liaoxuefeng.com/wiki/1016959663602400/1017497232674368
# anyway, Python is static, JavaScript is dynamic
# static is lazier and easier










