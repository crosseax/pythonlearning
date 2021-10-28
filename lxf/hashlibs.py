# hashlib

# yeah, hash functions

# read https://www.liaoxuefeng.com/wiki/1016959663602400/1017686752491744

import hashlib

md5 = hashlib.md5()
md5.update('How to use hashlib in python?'.encode('utf-8'))
print (md5.hexdigest())

"""
you can also do
"""

md5 = hashlib.md5()
md5.update('How to use hashlib '.encode('utf-8'))
md5.update('in python?'.encode('utf-8'))
print(md5.hexdigest())

"""
if you miss even by one letter,
the result will be hella different
thats just hash function
"""

md5 = hashlib.md5()
md5.update('How to use hashlib in python'.encode('utf-8')) # removed ? comparing above
print (md5.hexdigest())


# SHA1 (Security Hash Algorithm)

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
# 2c76b57293ce30acef38d98f6046927161b46a44
# the result is usually represented in 40 hex digits



# hw 1, for passwords

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    
    md5=hashlib.md5()
    md5.update(password.encode('utf-8'))
    
    if md5.hexdigest()==db[user]:
      return True
    else:
      return False

##################
# to prevent hacking using reverse md5 list
##################

db = {}

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')
    # the-Salt acts like a public key
    # the reverse work won't work unless knowing the-Salt



# hw2 

import hashlib, random

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)
        
db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}            
    
    
def login(username, password):
    user = db[username]
    return user.password == get_md5(password+user.salt)

assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')