# base64 is using 64 characteres(letters) to represent a binary data

# read https://www.liaoxuefeng.com/wiki/1016959663602400/1017684507717184

import base64

code1 = base64.b64encode(b'binary\x00string')

code2 =base64.b64decode(b'YmluYXJ5AHN0cmluZw==')

print (code1,
       code2, sep = '\n')

code3 = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')

code4 = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')

code5 = base64.urlsafe_b64decode('abcd--__')

print (code3,
       code4,
       code5, sep = '\n')


# hw

def safe_base64_decode(s):

    if (n:=len(s)%4):
        s=s+'='*(4-n)

    return base64.b64decode(s)
