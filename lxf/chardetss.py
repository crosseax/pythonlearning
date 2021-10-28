# chardet

# to the unknown codes, if you want to decode it to the readable string
# first thing you need to do is to guess its encoding method

# this is why chardet

# read more at https://www.liaoxuefeng.com/wiki/1016959663602400/1183255880134144

import chardet 

decode1 = chardet.detect (b'Hello, world') 

print (decode1) # {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}

data = '离离原上草，一岁一枯荣'.encode('gbk')

decode2 = chardet.detect(data)

print (decode2) # {'encoding': 'GB2312', 'confidence': 0.7407407407407407, 'language': 'Chinese'}

data2 = '最新の主要ニュース'.encode('euc-jp')

decode3 = chardet.detect(data2) 

print (decode3) # {'encoding': 'EUC-JP', 'confidence': 0.99, 'language': 'Japanese'}

import requests

r = requests.get('https://www.liaoxuefeng.com/wiki/1016959663602400/1183255880134144')

print (r.content.decode('ascii'))
