# hmac, Keyed-Hashing for Message Authentication
# so its basically converting salt from hashlib.py as a key
# to further simplify it
# read https://www.liaoxuefeng.com/wiki/1016959663602400/1183198304823296#0

import hmac, random

text = 'Hello, World!'
message = b'Hello, World!'

#different ways to convert str to bytes, review
message1 = bytes(text, 'utf-8')
message2 = text.encode('utf-8')

print (message,
       message1, 
       message2, sep = '\n')

key = b'secret'

h = hmac.new(key,message,digestmod='MD5')

print (h)
print (h.hexdigest())

for i in range(3):
    t = chr(random.randint(48,122))
    print(t)

for i in range (5):
    t = [chr(random.randint(48, 122)) for i in range(10)]
    print (t)

# hw

import hmac, random

def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)


assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
