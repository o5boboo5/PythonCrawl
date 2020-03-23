# Urllib

## request

### usage

```python
from urllib import request
```

### Function

#### urlopen(url)
```python
request.urlopen('http://www.baidu.com')
```
该函数返回一个对象，该对象上有如下
- geturl()  
得到真实的网页地址，可以判定是否重定向等问题
- info()
- getcode()  
得到状态码，200代表成功等等
- read(size)
读取siz字节大小的文件内容，如果size为空，那么读取整个文件
- readline()
读取一行内容。一些网站可能把所有代码都写在一行，因此有可能得到的内容是整个网站的源代码
- readlines()
读取整个文件，自动将文件内容分析成一个行的列表  
**上述三个都返回的是字节流，而不是字符串**

#### urlretrive(url,filename)  
将网页的源代码保存到filename文件中

## parse

### usage
```python
from urllib import parse
```

#### 

-urlparse  
解析url网址，返回结果由六部分组成，如下图所示。
```python
parse1 = parse.urlparse('http://www.baidu.com/s;dota?wd=hello')
# ParseResult(scheme='http', netloc='www.baidu.com', path='/s', params='dota', query='wd=hello', fragment='')
```
-urlsplit  
解析url网址，与urlparse类似，但是缺少params，其他几乎一样
```python
parse1 = parse.urlparse('http://www.baidu.com/s;dota?wd=hello')
# ParseResult(scheme='http', netloc='www.baidu.com', path='/s', query='wd=hello', fragment='')
```
-urlencode(query,encoding=None)  
用浏览器发送请求时，如果url中包含了中文字符或者其他特殊字符，那么浏览器会自动为我们进行编码。而如果使用代码发送请求，我们必须手动的进行编码，这时候就可以使用urlencode函数实现。urlencode可以把字典数据转换为url编码的数据。需要主要的是：urlencode的第一个参数是查询（也就是字典类型），而非网址。而且urlencode返回的数据类型是str类型，而不是byte类型。
```python
params = {'name': '呆呆', 'age': 1, 'greetings': 'Hello world'}
qs = parse.urlencode(params)
```
-parse_qs()  
将经过编码后的url参数进行解码。

### encode() 方法为字符串类型（str）提供的方法，用于将 str 类型转换成 bytes 类型，这个过程也称为“编码”。
### decode() 和 encode() 方法正好相反，decode() 方法用于将 bytes 类型的二进制数据转换为 str 类型，这个过程也称为“解码”。
##Request类

- request.Request(url,data=None,headers={},method=None)
需要主要的是，data应该为byte流，因此需要对数据进行编码(通过urlencode进行编码,然后通过encode进行编码)
```python
req = request.Request(url, headers=headers, data=parse.urlencode(data).encode('utf-8'), method='POST')
```






