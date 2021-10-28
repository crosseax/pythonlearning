# Object Oriented Programming 4

"""
Corey talks about inheritance of classes in this video.


1. What is inheritence?

It is a method that allows us to create a new class 
that shares the same attributes and method with the original function, 
and add some extra functionality to the new class. 
It also does not disturb the original class.


2. How to make a class inherit from another class?

class Developer(Employee):


3. Structure of classes and subclasses.

When we input a function to a subclass, python follows the 
'method resolution order', which is the chain of classes 
that it goes through to find what the method is. 
All classes have the built-in group of methods 
and attributes as their primary order.


4. How to initiate the subclass so that it can 
handle more information than its original class can?

There are 2 ways.
first, using the super method as follows and 
pass in the arguments in interest.
super.__init__()

Second, call the parent's init method explicitly and 
pass in the arguments in interest.
Employee.init(self, first, last, )


5. Useful tools when exploring the inheritance system.
.isinstance(instance, class)
This method returns the boolean value of 
whether an instance belongs to a calss
.issubclass(subclass, class)
This method returns the boolean value of 
whether a class has inherited from the second class.


6. Example of class inheritance
Whisky library 

++ when setting a default value for an ungiven argument, 
avoid using an empty mutable data type. 
That's a topic for another video.
"""

# https://www.youtube.com/watch?v=RSl87lqOXDE&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=43

# inheritance


class Employee(): # this is a class
    raise_amount = 1.04 

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self): 
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self): 
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee): 
    # if have no attribute, python will go along the chain to find the attribute
    # this chain is called method resolution order
    raise_amount = 1.2
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # can also do Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp (self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp (self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps (self):
        for emp in self.employees:
            print ('-->', emp.fullname())


emp1 = Employee('Chen','Khan', 40000)

dev1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev2 = Developer('Test', 'User', 60000, 'JavaScript')

print (dev1.pay)
dev1.apply_raise()
print (dev1.pay)

print (dev1.email)
print (dev1.prog_lang)


mgr1 = Manager('Sue', 'Smith', 90000, [dev1])

print (mgr1.fullname())
print (mgr1.email)

mgr1.add_emp(emp1)
mgr1.print_emps()
print ('\n')
mgr1.remove_emp(dev1)
mgr1.print_emps()

print (isinstance(mgr1, Manager))
print (isinstance(mgr1, Employee))
print (isinstance(mgr1, Developer))

print (issubclass(Manager, Employee))
print (issubclass(Manager, Developer))



# print (help(Developer))

