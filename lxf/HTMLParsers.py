# HTMLParser

# read https://www.liaoxuefeng.com/wiki/1016959663602400/1017784593019776

"""
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

"""





from urllib import request
from html.parser import HTMLParser
from html.entities import name2codepoint

class myhtmlparser(HTMLParser):
    _tag_name =''  
    _attrs_name =('',)
    _data_name =''

    def handle_starttag(self,tag,attrs):
        if len(attrs)>=1:
            if (attrs[0][0]=='class' and (attrs[0][1]=="event-title" or attrs[0][1]=="widget-title" or attrs[0][1]=="event-location" )) or attrs[0][0]=='datetime':
                self._tag_name=tag
                self._attrs_name=attrs
                print('...')

    def handle_data(self,data):
        if self._tag_name!='':
            print(data)

    def handle_endtag(self,tag):
        if tag==self._tag_name:
            self._tag_name=''
            self._attrs_name=('',)

def url2html(url):
    with request.urlopen(url) as f:
        html_get=f.read().decode(encoding='utf_8')
    return html_get

url_name='https://www.python.org/events/python-events/'
meetingpars=myhtmlparser()
htmlcontent=url2html(url_name)
meetingpars.feed(htmlcontent)