# requests module
# install anaconda first
# for more read https://www.liaoxuefeng.com/wiki/1016959663602400/1183249464292448

import requests, json

r = requests.get('https://www.baidu.com/')

# print (r.status_code)

# print (r.text)



# params, parameters



headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}



r = requests.get('https://www.douban.com/search', params={
                'q': 'python',
                'cat':'1001'
                }, 
                headers=headers)


"""
print (r.url) # https://www.douban.com/search?q=python&cat=1001

print (r.encoding)

print (r.content.decode('utf-8'))

"""


"""

r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})

print (r.text)

"""

r = requests.post('https://accounts.douban.com/login', 
                    data={
                    'form_email': 'abc@example.com',
                    'form_password': '123456'
                    })



url = ('https://accounts.douban.com/login')

re = requests.get(url, headers=headers)

print ('re',re)
#print(re.content.decode('utf-8'))


params = {
        'form_email': 'abc@example.com',
        'form_password': '123456'
}

rp = requests.post(url, json=params)

print (rp)

print (re.headers)
print (re.headers['Content-Type'])
print (re.cookies)

"""Output of above
{
    'Date': 'Fri, 27 Aug 2021 03:14:48 GMT', 
    'Content-Type': 'text/html; charset=utf-8', 
    'Transfer-Encoding': 'chunked', 
    'Connection': 'keep-alive', 
    'Keep-Alive': 'timeout=30', 
    'Vary': 'Accept-Encoding, Accept-Encoding', 
    'X-Xss-Protection': '1; mode=block', 
    'X-Douban-Mobileapp': '0', 
    'Expires': 'Sun, 1 Jan 2006 01:00:00 GMT', 
    'Pragma': 'no-cache', 
    'Cache-Control': 'must-revalidate, no-cache, private', 
    'X-Frame-Options': 'SAMEORIGIN', 
    'X-DAE-App': 'accounts', 
    'X-DAE-Instance': 'default', 
    'Server': 'dae', 
    'Strict-Transport-Security': 'max-age=15552000', 
    'X-Content-Type-Options': 'nosniff', 
    'Content-Encoding': 'br'
    }
"""





"""

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

url = 'https://www.douban.com'

r = requests.get(url, headers=headers)

print (r.encoding)
rd = r.content.decode('utf-8')
print (r.content)
#print (r.json())

"""

