from urllib import request

li_url='https://www.facebook.com/people/Xin-Li/100017024803439'
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
         'Cookie':'datr=uRJbXnRpQFvX9TvoTo0wNd0A; sb=BIBbXtKqkkwcmHN6O843vyTS; dpr=2; c_user=100025453117937; xs=20%3Av1cJBmXV7q_QOg%3A2%3A1584789280%3A-1%3A-1; fr=0nhlYjkwaKXYXCeEv.AWW_htK6GJUE8D-StcgQYlRJuOc.BeV9jA.7s.AAA.0.0.Bedfcg.AWVPze95; spin=r.1001876243_b.trunk_t.1584789281_s.1_v.2_; presence=EDvF3EtimeF1584789294EuserFA21B25453117937A2EstateFDutF1584789294676CEchF_7bCC; act=1584789317712%2F0; wd=831x905'}

req=request.Request(li_url,headers=headers)

response=request.urlopen(req)

print(response.read().decode('utf-8'))