#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta
import urllib.request as ur
import json



url1 = "https://twitter.com/i/search/timeline?f=tweets&vertical=default&q=%EB%AC%B8%EC%9E%AC%EC%9D%B8%20since%3A"
date1 = "2017-05-09"
url2 = "%20until%3A"
date2 = "2017-05-10"
url3 = "&src=typd&include_available_features=1&include_entities=1&lang=ko&max_position=TWEET-"
num1 = "868616452256837634"
#-
num2 = "868617814784880640"
url4 = "-BD1UO2FFu9QAAAAAAAAETAAAAAcAAAASAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA&oldest_unread_id=0&reset_error_state=false"

tweet = {}

headers = {}
headers['User-Agent'] = "chrome/5.0"
count = 0

#n = 100
init_date = datetime(2017, 5, 9)

while(1):
    #n = n - 1
    url = url1 + date1 + url2 + date2 + url3 + num1 + '-' + num2 + url4
    
    req = ur.Request(url, headers = headers)
    fp = ur.urlopen(req)
    soup = BeautifulSoup(fp, "lxml")
    p = soup.find("p")
    q = p.text
    count += q.count("js-tweet-text-container") # count # of tweets
    num1 = q[23:41]
    num2 = q[42:60]
    print("num1: "+num1)
    print("num2: "+num2)
    print("count: "+str(count))
    print("index")
    #print(q.find('class=\"tweet-timestamp js-permalink js-nav js-tooltip\" title='))
    #  js-permalink js-nav js-tooltip\" title=\" : LEN(40)
    # js-permalink js-nav js-tooltip\" title=\"\uc624\ud6c4 4:48 - 2017\ub144 6\uc6d4 13\uc77c\"  dat : LEN(67)
    '''
    idx = q.find('tweet-timestamp')
    print(idx) # 2724
    '''
    idx = q.rfind('tweet-timestamp') # find LAST occurence of "tweet-timestamp"
    print(idx)
    cand = q[idx+57:idx+115]
    i = cand.find('"')
    time = cand[0:i-1]
    # using json to encode and decode "utf-8"
    tmp = '{"a":"'+time+'"}'
    tmp = json.loads(tmp)
    time = tmp["a"]

    #print(time.encode('utf-8').decode('utf-8'))
    time = time.replace("오후", "PM")
    time = time.replace("오전", "AM")
    new_time = datetime.strptime(time, "%p %I:%M - %Y년 %m월 %d일")
    new_time = datetime(new_time.year, new_time.month, new_time.day)
    if(init_date != new_time):
        break

    print(new_time)

    '''
    # DEBUG
    print("IDX:"+str(cand.find('"')))
    print(cand[0:i])
    print(q.find('tweet-timestamp'))
    print(q.find("min"))
    '''


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
