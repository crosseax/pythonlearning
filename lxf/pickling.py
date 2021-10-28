# pickling in python is the process to transfer variable from ram into storable info

d = dict(name = 'Bob', age = 20, score = 88)
# everytime you run, after changing, lets say, name Bob to Bill, 
# next time you run, it'll get initialized back into name = Bob
# so to store it
"""use pickle
"""
import pickle 

d = dict(name = 'Bob', age = 20, score = 88)

t = pickle.dumps(d)

print (t) 
# b'\x80\x04\x95$\x00\x00\x00\x00\x00\x00\x00}\x94
# (\x8c\x04name\x94\x8c\x03Bob\x94\x8c\x03age\x94K\x14\x8c\x05score\x94KXu.'

"""so pickle.dumps() turns a thing into bytes, then write it
"""

f = open('dump.txt', 'wb')
pickle.dump(d,f)
f.close()
# now the dump.txt is a total mess, python internal info

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close
print (d) # {'name': 'Bob', 'age': 20, 'score': 88}

"""
pickling files into JSON for easy transfer,
cuz JSON is a list of bytes, which is easy to read and write and send across neighbors wifi

JSON                    Python
{}                      dict
[]                      list
"string"                str
1234.56                 int or float
true/false              True/False
null                    None

"""

import json
d = dict (name = 'Jason', age = 20, score = 90)
j = json.dumps(d) # returns a str
print (j) # {"name": "Jason", "age": 20, "score": 90}

json_str = '{"name": "Jason", "age": 20, "score": 90}'
js = json.loads(json_str)
print (js) # {'name': 'Jason', 'age': 20, 'score': 90}



"""
Advanced JSON
"""
# import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        
s = Student('Chris', 25, 95)

# print (json.dumps(s)), 
# TypeError: Object of type Student is not JSON serializable

"""

for more, read https://www.liaoxuefeng.com/wiki/1016959663602400/1017624706151424
yeah just read bruh

so basically now we write a transfer function, to transfer Student(class) into dict

"""

def student2dict(std):
    return{
        'name':std.name,
        'age':std.age,
        'score':std.score
    }

print (json.dumps(s, default = student2dict))
# {"name": "Chris", "age": 25, "score": 95}

# to work easier
print (json.dumps(s, default = lambda obj: obj.__dict__))
# {"name": "Chris", "age": 25, "score": 95}

def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

json_str = '{"name": "Chris", "age": 25, "score": 95}'
print (json.loads(json_str, object_hook=dict2student))
# <__main__.Student object at 0x00000204A82A6B50> # the number can change everytime 



"""

hw

"""

obj = dict(name='小明', age=20)
shw = json.dumps(obj, ensure_ascii=True)
print (shw)


"""
Below is from youtube 
with a bit of use case of json
to help understand
"""
print ('\nBelow is from youtube')

with open ('./companies.json', 'r') as f:
    fr = f.read()
    print (fr)
    f.seek(0)
    jl = json.loads(f.read())
    print (jl)
    
    