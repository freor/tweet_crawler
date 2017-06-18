'''
https://twitter.com/search?q=%EB%AC%B8%EC%9E%AC%EC%9D%B8
since%3A2017-06-01%20until%3A2017-06-06&src=typd
'''

'''
https://twitter.com/search?l=&q=%EB%AC%B8%EC%9E%AC%EC%9D%B8
%20until%3A2017-06-08&src=typd&lang=ko
'''

import urllib.request as ur
from bs4 import BeautifulSoup
from datetime import datetime
import json

tweet = {}

epoch = 15

headers = {}
headers['User-Agent'] = "chrome/5.0"
#url = "https://twitter.com/search?q=%EB%AC%B8%EC%9E%AC%EC%9D%B8&src=typd&lang=ko"
_url = "https://twitter.com/search?l=&q=%EB%AC%B8%EC%9E%AC%EC%9D%B8%20until%3A"
dat = "2017-05-30"
url_end = "&src=typd&lang=ko"

#url = _url + dat + url_end

# URL INFO

n= 2

while(n):
    n = n-1
    url = _url + dat + url_end
    print(n)

    req = ur.Request(url, headers = headers)

    fp = ur.urlopen(req)
    # (js-tweet-text / 2) 갯수 세면 된다.

    #print(fp.read())

    # TODO
    '''
    https://twitter.com/
    search?q=%EB%AC%B8%EC%9E%AC%EC%9D%B8&src=typd&
    lang=ko
    '''
    soup = BeautifulSoup(fp, 'html.parser')
    #print(soup.prettify())
    #print(soup.find_all("js-tweet-text-container"))
    myDiv = soup.find_all("div", { "class" : "js-tweet-text-container"})
    #print(soup.find_all("div"))

    print(soup.findAll(lambda tag: tag.has_attr('data-time')))

    #print(myDiv)

    #print(myDiv[0])

    p = soup.find_all("div", { "class" : "tweet" })


    print("HEREREREREEREREREERERE")
    aaa = p[0].find(lambda tag: tag.has_attr('data-time'))['data-time']

    tweet[aaa] = 0

    print("KJLFJDALFJADKLFJDLKFJ")
    print(tweet)

    ppp = p[0]["data-reply-to-users-json"]

    ppp = json.loads(ppp)[0]
    
    print(ppp["screen_name"])
    print(ppp)
    

    p = p[0:epoch]

    # TIME
    k = soup.find_all("div", { "class": "stream-item-header"})
    t = k[0].find("a",{"class": "tweet-timestamp"})['title']
    if(t[0:2] == "오후"):
        m = t.replace("오후", "PM")
    else:
        m = t.replace("오전", "AM")

    m = datetime.strptime(m, "%p %I:%M - %Y년 %m월 %d일")
    mx = m

    print(m)

    for i in k:
        u = i.find("a", {"class": "tweet-timestamp"})
    
        if(u is not None):
            tmp = u['title']
            if(tmp[0:2] == "오후"):
                tmp = u['title'].replace("오후", "PM")
            elif(tmp[0:2] == "오전"):
                tmp = u['title'].replace("오전", "AM")
            print(tmp)
            tmp = datetime.strptime(tmp, "%p %I:%M - %Y년 %m월 %d일")
        
            if(m > tmp):
                m = tmp
            if(mx < tmp):
                mx = tmp

    tt = m.timetuple()
    next_date_url = str(tt.tm_year) + "-" + str(tt.tm_mon) + "-" + str(tt.tm_mday)
    print("MINIMUM")
    print(m)
    print(next_date_url)
    dat = next_date_url

    print(mx)

    # TEXT
    #q = soup.find("div", { "class" : "stream-item-footer" })

    total_retweet = 0
    for i in p:
        tmp = i.find("button", {"class" : "js-actionRetweet"})
        if(tmp == None):
            continue
        #print(tmp)
        t = tmp.find("span", {"class": "ProfileTweet-actionCountForPresentation"})
        a = t.text
        if(a == ''):
            continue
        a = a.replace(',', '')
        total_retweet += int(a)

    print("SUM")
    print(total_retweet)

    total_reply = 0
    for i in p:
        tmp = i.find("button", {"class" : "js-actionReply"})
        if(tmp == None):
            continue
        t = tmp.find("span", {"class": "ProfileTweet-actionCountForPresentation"})
        a = t.text
        if(a == ''):
            continue
        a = a.replace(',', '')
        total_reply += int(a)

    print("SUM")
    print(total_reply)

    total_fav = 0
    for i in p:
        tmp = i.find("button", {"class" : "js-actionFavorite"})
        if(tmp == None):
            continue
        t = tmp.find("span", {"class": "ProfileTweet-actionCountForPresentation"})
        a = t.text
        if(a == ''):
            continue
        a = a.replace(',', '')
        total_fav += int(a)

    print("SUM")
    print(total_fav)
