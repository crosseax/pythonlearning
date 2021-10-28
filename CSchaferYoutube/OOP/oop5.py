# Object Oriented Programming 5

# https://www.youtube.com/watch?v=3ohzBxoFHAY&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=44

# special methods / magic methods

# for more dunder methods (like __init__, __add__, __repr__...) read below 
# https://docs.python.org/3/reference/datamodel.html#special-method-names

class Employee:
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

    def __repr__(self): # unambiguous representation of the object
        return "Employee('{}','{}',{})".format(self.first, self.last, self.pay)
        # {} is called a placeholder
    # first be sure to have repr method, 
    # that way str method can fall back to it if not defined

    def __str__(self): # readable representation of the object
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp1 = Employee('Corey', 'Schafer', 60000)
emp2 = Employee('Test', 'User', 70000)

# print (emp1)

print (repr(emp1)) # Employee('Corey','Schafer',60000)
print (str(emp1)) # Corey Schafer - Corey.Schafer@company.com

print (emp1.__repr__()) # Employee('Corey','Schafer',60000)
print (emp1.__str__()) # Corey Schafer - Corey.Schafer@company.com

print (emp1 + emp2) # from __add__


print (len('test'))
print ('test'.__len__())

print (len(emp1)) # from __len__
