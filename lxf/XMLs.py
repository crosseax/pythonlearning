# XML

# read https://www.liaoxuefeng.com/wiki/1016959663602400/1017784095418144

"""
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

"""
"""
L = []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append(encode('some & data'))
L.append(r'</root>')
print (''.join(L))
"""



# hw

from xml.parsers.expat import ParserCreate            # 引入xml解析模块
from urllib import request                            # 引入URL请求模块

class WeatherSaxHandler(object):                      # 定义一个天气事件处理器

    weather ={'city':1,'cityname':[], 'forecast':[]}               # 初始化城市city和预报信息forecast

    def start_element(self, name, attrs):             # 定义开始标签处理事件
        if name=='beijing':
            self.weather['city']='北京'
        if name == 'city':               # 获取location信息
            self.weather['cityname'].append(attrs['cityname'])          #获取地区名
            # 获取forecast信息
            self.weather['forecast'].append({
                'state':attrs['stateDetailed'], 
                'high':attrs['tem2'], 
                'low':attrs['tem1']
            })

def parseXml(xml_str):                                # 定义xml解析器

    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.Parse(xml_str)                             # 解析xml文本
    print('City'+handler.weather['city'])
    for (x,y) in zip(handler.weather['cityname'],handler.weather['forecast']):             # 打印天气信息
        print('Region:'+x)
        print(y)
    
    return handler.weather
    

# 测试:
URL = 'http://flash.weather.com.cn/wmaps/xml/beijing.xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))


