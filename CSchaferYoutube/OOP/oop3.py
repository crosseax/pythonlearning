# Object-Oriented Programming 3

"""
Summary:
In this video, Corey distinguishes between 
a regular method, class method, and a static method.

Firstly, a regular method is the type of method 
that we are used to seeing since the start of OOP tutorials. 
It is accessible through both the class and the instance, 
which means that we can call for the method in both

Employee.method()
and
emp_1.method()

they automatically have the instance as the first positional argument, as self.

Secondly, class methods are the type of method used 
when a method is not really about an instance of a class, 
but the class itself. To create a class method, 
just add '@classmethod' a line before creating the class method. 
The class is automatically the first argument to be passed in, 
and is represented as 'cls' instead of 'class'. 
This is because 'class' is already assigned to be something else in Python. 
There are 2 ways of using the class method as far as Corey has shown.

First is modifying the class variable. 
Corey modified the 'raise_amount' class variable using a class method. 
Just remember that to access a class variable, 
we have to write 'cls.' before specifying the actual name. 
For example, as 'cls.raise_amount' as in the video.


Second is making an alternative constructor. 
Sometimes people have information of their specific instances 
of the class available in a specific format. 
Corey shows an example of this 
where first and last names and pay are separated by a hyphen. 
Corey creates a class method that returns the class 
with the specific values passed in that are obtained 
by using split() method to the string passed in. 
User of the script can now automatically create a new instance 
without having to parse the string at '-'.


Corey then moves on to cover static methods. 
Static methods are different from regular methods and class methods 
in that it doesn't have a class or instance 
that is automatically passed in as a firs positional argument. 
They can be created by adding '@staticmethod' a line 
before defining the method. 
These are methods that have a logical connection to the Class, 
but does not need a class or instance as an argument. 

Corey says that it is better to make sure 
we create a static method rather then class or regular method 
when we are sure that we don't make use of the class or instance 
within the method.
"""

# https://www.youtube.com/watch?v=rq8cL2XMM5M&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=42

# classes methods and static methods



class Employee(): 

    num_of_emps = 0
    raise_amount = 1.04 

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1 

    def fullname(self): 
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self): 
        self.pay = int(self.pay * self.raise_amount)

    @classmethod # turns method below into class method
    def set_raise_amt(cls, amount): # cannot use class as variable name
        cls.raise_amount = amount

    @classmethod
    def from_str(cls, empstr): # classmethod also pass in first arg cls automatically
        first, last, pay = empstr.split('-')
        return cls(first, last, pay)


    @staticmethod 
    # if you dont access the instance or the class within the method
    # then it should be a staticmethod
    def is_workday(day): # staticmethod pass no arg automatically
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee('Corey', 'Schafer', 50000) 
emp2 = Employee('Test', 'User', 60000)

import datetime

myDate = datetime.date(2017, 7, 29)
print (Employee.is_workday(myDate))













"""
# use classmethods as alternative constructors
# what they mean is 
# to use classmethods in order to provide
# multiple ways to create our objects

empStr1 = 'John-Doe-75000'
empStr2 = 'Steven-Smith-30000'
empStr3 = 'Jane-Doe-90000'

newEmp1 = Employee.from_str(empStr1) # this is a alternative constructor
print (newEmp1.email)

"""







"""
operating classmethods

Employee.set_raise_amt(1.06) # cls was passed in automatically
Employee.raise_amount = 10 # same as above
emp1.set_raise_amt(1.08) # can also works for instance, but nobody does that cuz it makes no not that much sense


print (Employee.raise_amount)
print (emp1.raise_amount)
print (emp2.raise_amount)

"""