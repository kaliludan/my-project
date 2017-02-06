# coding:utf-8
import re
import requests

r = requests.get('http://www.163.com')

link_list =re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')" ,data)
for url in link_list:
    f = open('/Users/kaliludan1/Downloads/crawl/163.txt', 'a+')
    print url
    f.write(url+'\n')