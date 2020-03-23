from urllib import request
from urllib import parse

# request.urlretrieve('http://www.hao123.com','hao123.xml')

# response=request.urlopen('http://www.baidu.com')
url = 'http://www.baidu.com/s'

params = {'name': '呆呆', 'age': 1, 'greetings': 'Hello world'}

qs = parse.urlencode(params)
qsencode = qs.encode('utf-8')

print(type(qs))

print(type(qsencode))

url = url + "?" + qs

response = request.urlopen(url)

result = parse.parse_qs(qs)

# print(response.read())
