from bs4 import BeautifulSoup
from datetime import date
from datetime import timedelta
import urllib.request as ur
import json

url1 = "https://twitter.com/i/search/timeline?f=tweets&vertical=default&q=%EB%AC%B8%EC%9E%AC%EC%9D%B8%20since%3A"
date1 = "2017-05-27"
url2 = "%20until%3A"
date2 = "2017-05-28"
url3 = "&src=typd&include_available_features=1&include_entities=1&lang=ko&max_position=TWEET-"
num1 = "868616452256837634"
#-
num2 = "868617814784880640"
url4 = "-BD1UO2FFu9QAAAAAAAAETAAAAAcAAAASAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA&oldest_unread_id=0&reset_error_state=false"

tweet = {}

headers = {}
headers['User-Agent'] = "chrome/5.0"

n = 100

while(n):
    n = n - 1
    url = url1 + date1 + url2 + date2 + url3 + num1 + '-' + num2 + url4
    
    req = ur.Request(url, headers = headers)
    fp = ur.urlopen(req)
    soup = BeautifulSoup(fp, "lxml")
    p = soup.find("p")
    q = p.text
    count = q.count("js-tweet-text-container") # count # of tweets
    num1 = q[23:41]
    num2 = q[42:60]
    print("num1: "+num1)
    print("num2: "+num2)
    print(count)

'''
url = url1 + date1 + url2 + date2 + url3 + num1 + '-' + num2 + url4

req = ur.Request(url, headers = headers)

fp = ur.urlopen(req)

soup = BeautifulSoup(fp,"lxml")

p = soup.find("p")
q = p.text

print(q[23:41])
print(q[42:60])
'''


#q = json.loads(p.text)

#print(p.text)
#print(p.text[1250:1264])
#print(q[0])
#print(q["min_position"])
#print(json.loads(p.text))
#print(json.loads(p.text)["min_position"])
