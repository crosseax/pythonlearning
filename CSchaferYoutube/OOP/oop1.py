# Object-Oriented Programming 1

# https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=40

# Creating and Instanciating classes

# Method - is a function associated with class

class Employee(): # this is a class
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    # names, emails, pay are the Attributes of the class

    def fullname(self): # this is a method
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('Corey', 'Schafer', 50000) # this is a instance variable
emp2 = Employee('Test', 'User', 60000)

# print (emp1)
# print (emp2)


print (emp1.email)
print (emp2.email)
# need no parentheses because it is a attribute

print (emp1.fullname()) 
print (emp2.fullname())
# we need the parentheses here because it is a method not a attribute

print (Employee.fullname(emp1))
print (Employee.fullname(emp2))



emp3 = Employee('Chen', 'Yan', '70000')
# these two lines does the same thing
# line 1 did instance.method(), so no need to put int instance
# line 2 did class.method(instance), and instance gets passed in as self
print (emp3.fullname()) 
print (Employee.fullname(emp3))


"""
emp1.first = 'Corey'
emp1.last = 'Schafer'
emp1.email = 'Corey.Schafer@company.com'
emp1.pay = 50000

emp2.first = 'Test'
emp2.last = 'User'
emp2.email = 'Test.User@company.com'
emp2.pay = 60000
"""