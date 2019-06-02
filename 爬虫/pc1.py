#这是静态网页图片爬取
# -*- coding:utf-8 -*-
import requests
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.103 Safari/537.36'}
i='//img.hb.aicdn.com/37e77b125b1c114d20e0c8d6915519af55661331151d06-ZOuO1u_fw658'
with open(r'C:\\Users\\Administrator.SKY-20180119TBP\\Desktop\爬虫\\图片\\'+str(10)+'.jpg','wb') as f:
	f.write(requests.get(i,headers=headers).content)
	


'''from lxml import etree
r=requests.get('')	#获取网页内容
print(r.status_code)  #查看返回是否成功
html=etree.parse()	#相当于解析网页内容
result=html.xpath('')	#路径
'''