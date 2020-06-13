
# Gets today's stock price at the most recent close, for each stock you enter.
# Stock price is appended to a file and user receives a text of current stock prices
# Additional functionality is still being built and added :) 

#! /usr/bin/python3

# import libraries
import requests, time, urllib
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from twilio.rest import Client

stocks = []

while True:
    ticker_sym = input("Enter ticker symbol or company name ")
    if not ticker_sym:
        break
    else:
        stocks.append(ticker_sym)

#display all stocks to find prices of
print("Please find the price of the following stocks below", stocks)


#setup webdriver and navigate to Yahoo Finance
service = Service(r"C:\Users\rhone\Downloads\chromedriver_win32\chromedriver.exe")
service.start()
driver = webdriver.Remote(service.service_url)
driver.get('https://finance.yahoo.com/')

#Find stock info
for stock in stocks:
    #get info from yahoo finance using ticker_sym
    html = driver.execute_script('return document.body.innerHTML')
    text_area = driver.find_element_by_id('yfin-usr-qry')
    text_area.send_keys(stock)
    time.sleep(5)
    driver.find_element_by_id('header-desktop-search-button').click()
    time.sleep(1)
    url = driver.current_url
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'lxml')
    price = soup.select_one('.Trsdu\(0\.3s\)').text
    output = stock + " price at close is " + price
    print(output)
driver.quit()

# append to file

#send text message
#change variables to reflect yours for twilio and your cell phone number
account_sid = 'ACea81d5c8a1664d54803d397a7eb90930'
auth_token = '859ede92e9427647b894d4707f05f92a'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
        body = output,
        from_ = '+12565408378',
        to = '+18285572245'
)

print(message.sid)


