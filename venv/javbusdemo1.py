from urllib import request

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.149 Safari/537.36 '
}

url = 'https://www.javbus.com/ajax/uncledatoolsbyajax.php?gid=42780987747&lang=zh&img=https://pics.javbus.com/cover/7kvb_b.jpg&uc=0&floor=832'
req = request.Request(url, headers=headers)
res = request.urlopen(req)

print(res.read().decode('utf-8'))
