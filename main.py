from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import sys

import unittest, time, re

from bs4 import BeautifulSoup # for HTML parsing
from datetime import date
from datetime import timedelta



class Sel(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

        # DATA SET
        self.data = {} # FORMAT: { "date": "number" }
        self.tweet_num = 0
        self.retweet_num = 0
        self.reply_num = 0
        self.fav_num = 0

        # URL
        self.base_url = "https://twitter.com"
        self.search_url = "/search?f=tweets&vertical=default&q="
        self.search_word = "%EB%AC%B8%EC%9E%AC%EC%9D%B8"
        self.until = "%20until%3A"
        self.date_url = "2017-05-30" # TODO
        self.end_url = "&src=typd"

        self.verificationErrors = []
        self.accept_next_alert = True

    def test_sel(self):
        driver = self.driver
        #driver.get(self.base_url + "/search?q=%EB%AC%B8%EC%9E%AC%EC%9D%B8&src=typd")
        driver.get(self.base_url + self.search_url + self.search_word + self.until + self.date_url + self.end_url)
        #driver.find_element_by_link_text("All").click()
        while(1):
            #driver.get(self.base_url + self.search_url + self.search_word + self.date_url + self.end_url)
            print("working")
 
            sor = driver.page_source
            soup = BeautifulSoup(sor, 'html.parser')
            #min_date = 999999999999999 # date
            brk = False # for while break

            tweet = soup.find_all("div", {"class": "tweet"})

            # examine if it should stop finding
            blocks = soup.find_all(lambda tag: tag.has_attr('data-time'))
            init_date = str(self.timest_to_date(int(blocks[0]['data-time'])))
            naive_min_date = blocks[-1]['data-time']
            min_date = str(self.timest_to_date(int(naive_min_date)))

            print(len(blocks))


            if(init_date != min_date):
                brk = True

            # calculate!!
            if(brk):
                tweet_num = len(blocks)
                self.data[min_date] = tweet_num
                self.date_url = min_date
                print("FINISH")
                # TODO
                print(tweet_num)
                # count
                count_soup = soup.find_all("button", { "class" : "js-actionRetweet" })
                self.retweet_num = 0
                for i in count_soup:
                    tmp = i.find("span", { "class": "ProfileTweet-actionCountForPresentation" })
                    text = tmp.text.replace(',', '')
                    print(text+ " this")
                    if(text != ""):
                        self.retweet_num += int(text)

                count_soup = soup.find_all("button", { "class" : "js-actionReply" })
                self.reply_num = 0
                for i in count_soup:
                    tmp = i.find("span", { "class": "ProfileTweet-actionCountForPresentation" })
                    text = tmp.text.replace(',', '')
                    if(text != ""):
                        self.retweet_num += int(text)

                count_soup = soup.find_all("button", { "class" : "js-actionFavorite" })
                self.fav_num = 0
                for i in count_soup:
                    tmp = i.find("span", { "class": "ProfileTweet-actionCountForPresentation" })
                    text = tmp.text.replace(',', '')
                    if(text != ""):
                        self.retweet_num += int(text)

                self.date_url = min_date
                #self.date_url = str(self.timest_to_date(int(naive_min_date)) - timedelta(days=1))

                driver.get(self.base_url + self.search_url + self.search_word + self.until + self.date_url + self.end_url)
                #driver.find_element_by_link_text("All").click()
                driver.manage().timeouts().implicitlyWait()
       
                continue

            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
        html_source = driver.page_source
        data = html_source.encode('utf-8')

    def timest_to_date(self, st):
        std_day = date(1970,1,1)
        return (std_day + timedelta(seconds=st))


if __name__ == "__main__":
    unittest.main()

