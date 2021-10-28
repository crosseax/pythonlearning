# Object-Oriented Programming 2

"""
Summary:
In this video, Corey taught as how to differentiate 
between a Class variable and instance variable, 
how they are related to each, other, 
and when each of them is more useful over the other.

Class variables are variables that we set inside a class, 
and are shared among all instances. 
Corey gave a good example where the number of total employs 
should be the same to every employ, 
no matter which employee we are referring to. Therefore,

emp_1.num_of_employ = emp_2.num_of_employ = Employee.num_of_employ

Instance variables are variables that are different from each instance. 
For example, the names and the pay for each employee. 
They have to be different.


Corey also shows that class variables and instance variables are closely related, 
and that class variables are kind of 'inherited' to the 'self' variables.
To illustrate this, Corey shows an example of 'annual raise of pay'. 
He initially creates the class variable to show a case 
where annual raise is equal among all the employees. 
This variable of 1.04 was accessible through each instance, 
and also through the class itself(obiviously). 
That is,

print(Employee.annual_raise)
print(emp_1.annual_raise)
print(emp_2.anual_rais)
all printed out 1.04.


However, using the ._dict__  thing, Corey shows that the intances, 
emp_1 and emp_2 does not contain the annual_raise value. 
Corey explains that if a variable is not found 
within an instance and programmers try to access the variable, 
python automatically looks in in the variable of the instance's class, 
and then the more classes that the instance's class inherits from.


Furthermore, if we access the class variable through an instance 
and then change it, python creates the variable within the instance. 
We can check it by using the ._dict_ thing. 
Corey shows that annual_raise key was created 
when he manually changed the annual_raise value as 1.05 
in the following way.

emp_1.annual_raise = 1.05

however, we know that the class variable remained the same at 1.04, 
when printing the class variable.
print(Employee.annual_raise)

==> 1.04
"""

# https://www.youtube.com/watch?v=BJ-VvGyQxho&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=41

# classes variables

# class variables are the variables shared among all instances in the class
# instances variables can be unique
# class variables are same for each instances

class Employee(): # this is a class

    raise_amount = 1.04 # this is a class variable
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    # names, emails, pay are the Attributes of the class
        Employee.num_of_emps += 1 # if use self, it wont work

    def fullname(self): # this is a method
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self): 
        self.pay = int(self.pay * self.raise_amount)



print (Employee.num_of_emps)

emp1 = Employee('Corey', 'Schafer', 50000) # this is a instance variable
emp2 = Employee('Test', 'User', 60000)

Employee.raise_amount = 1.05

# i can access this class variable by either the class itself
# or the instances within the class
print (Employee.raise_amount)
print (emp1.raise_amount)
print (emp2.raise_amount)

print (emp2.__dict__) # does not contains raise_amount
# print (Employee.__dict__) # contains raise_amount


# when making this assignment, 
# it actually created the attribute raise_amount in the emp2
emp2.raise_amount = 1.06

print (emp1.__dict__)
print (emp2.__dict__) # now has 'raise_amount' attribute


print (Employee.num_of_emps)






"""
print (emp1.pay)
emp1.apply_raise()
print (emp1.pay)
"""
