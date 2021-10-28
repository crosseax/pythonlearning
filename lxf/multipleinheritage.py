# multiple inheritance

# read https://www.liaoxuefeng.com/wiki/1016959663602400/1017502939956896
# for more Useful readings: https://www.jianshu.com/p/c9a0b055947b

# Dog and bat is mammal, parrot and ostrich is bird
# Dog and ostrich can run, parrot and Bat can fly

class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

# to add runnable and flyable

class Runnable (object):
    def run(self):
        print ('can run')

class Flyable (object):
    def fly(self):
        print ('can fly')

# to put those animals into those catagories

class Dog(Mammal, Runnable):
    pass

class Bat(Mammal, Flyable):
    pass

class Ostrich(Bird, Runnable):
    pass

class Parrot(Bird, Flyable):
    pass

d = Dog()
d.run()
# d.fly(), AttributeError

# the thing above is called MixIn
# a class can have multiple MixIn
# adding MixIn is for the code to be easier to read
# also kinda distinguish the main subclass and others

# for example 
class RunnableMixIn(object):
    def run(self):
        print ('can run')

class Dog(Mammal, RunnableMixIn):
    pass



