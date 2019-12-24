#!/usr/bin/env python

#import libraries
import csv
import urllib2
from bs4 import BeautifulSoup
from datetime import datetime

#url to fine #'s
url = 'https://www.yellowbook.com/s/seafood-restaurants/charleston-sc/'

#query website and reutrn html to page
page = urllib2.urlopen(url)

#parse html with beautiful soup & store in soup variable
soup = BeautifulSoup(page, 'html.parser')

#find ,div> tags that have phone-number class
phoneNums = soup.find_all('div', attrs={'class':'phone-number'})
restaurantName = soup.find_all('info', attrs={'data-omclick': 'a'})
print(restaurantName)
#for phoneNum in phoneNums:
#	nums = phoneNum.contents[0]
#	print(nums)

