# -*- coding:utf-8 -*-
from selenium import webdriver
import win32api
import win32con
import time 
import requests
from selenium.webdriver.common.keys import Keys
from lxml import etree
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding':'gzip',
'Connection':'close',
'Referer':None #注意如果依然不能抓取的话，这里可以设置抓取网站的host
}
b=0
driver=webdriver.Chrome()#打开谷歌浏览器

url=''
driver.get(url)#打开网页
html=etree.HTML(driver.page_source.encode("utf-8","ignore"))	#相当于解析网页内容
result=html.xpath('//a/img/@src')	#路径
for i in result:
	try:
		with open(r'C:\\Users\\Administrator.SKY-20180119TBP\\Desktop\爬虫\\图片\\'+str(b)+str(i[-4:]),'wb') as f:
			b=b+1
			
			f.write(requests.get(i,headers=headers).content)
	except:
		continue