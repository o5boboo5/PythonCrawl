from urllib import request
from urllib import parse

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
}
# url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
# https://www.javbus.com/ajax/uncledatoolsbyajax.php?gid=42780987747&lang=zh&img=https://pics.javbus.com/cover/7kvb_b.jpg&uc=0&floor=832

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

data = {
    'first': 'true',
    'pn': 1,
    'kd': 'python'
}

req = request.Request(url, headers=headers, data=parse.urlencode(data).encode('utf-8'), method='POST')


response = request.urlopen(req)
print(response.read().decode('utf-8'))
