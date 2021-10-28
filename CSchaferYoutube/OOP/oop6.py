# Object Oriented Programming

# https://www.youtube.com/watch?v=jCzT9XFZ5bw&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=45

# Property Decorators - Getters, Setters, and Deleters

class Employee:
    def __init__(self, first, last):
        self.first = first 
        self.last = last
        # self.email = first + '.' + last + '@email.com'

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter 
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first 
        self.last = last

    @fullname.deleter 
    def fullname(self):
        print ('Delete Name')
        self.first = None
        self.last = None


emp1 = Employee('John', 'Green')

print (emp1.first)
print (emp1.email)
print (emp1.fullname)

emp1.fullname = 'Corey Schafer'

print (emp1.first)
print (emp1.email)
print (emp1.fullname)

del emp1.fullname