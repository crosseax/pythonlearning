# private variables
# and the restriction to alter

# so for the case below

class Student(object):
    def __init__(self, name, score):
        name = self.name
        score = self.score

# this is still public variable and class that everyone can visit
# to create private variable, use __properties, like below

class Student (object):
    def __init__ (self, name, score):
        self.__name = name
        self.__score = score
        # code above turns the variables into private variables
    
    def print_score (self):
        print ('%s: %s' % (self.__name, self.__score))

# now, for external code, nothing pretty much changed
# but now you cannot visit property.__name

bart = Student('Bart Simpson', 75)
# bart.__name # AttributeError: 'Student' object has no attribute '__name'
# but you can do single _ to check
print ('use singcle _ to check private variables,', bart._Student__name)
print (
    'but such thing above is not reccomended, \n' 
    'cuz for different version of python, \n'
    'problem might occur'
    '\n'
)



# now to method the data, you can do below

class Student (object):
    def __init__ (self, name, score):
        self.__name = name
        self.__score = score

    def print_score (self):
        print ('%s: %s' % (self.__name, self.__score))
    # same as above so far

    # below is where the magic is
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    
    # by using method above
    # even you can change the private variables by using code: bart.score = 99
    # you can check the parameter to avoid invalid parameters

    def set_score(self, score):
        if () <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
    
    # if you want to be able to check the data outside add below
    # def set_score(self):
        # self.__score = score

bart = Student('Bart Simpson', 75)
print (bart.get_name())

# hm

class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_name(self):
        return self.__name
    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender in ['male', 'female']:
            self.__gender = gender
        else:
            raise ValueError ('Invalid gender, please input \'female\' or \'male\' ')
        
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('hw test failed')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('hw test failed')
    else:
        print('hw test successed')

print (bart.get_gender())


