# Gets today's stock price at the most recent close, for each stock you enter.
# Stock price is appended to a file and user receives a text of current stock prices
# Additional functionality is still being built and added :)

#! /usr/bin/python3

# import libraries
import StockList as sl
import sys
from termcolor import colored
import requests, time, urllib
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from twilio.rest import Client

#display all stocks to find prices of
def output(stock_list):
    print("Please find the price of the following stocks below", stock_list)

    #setup webdriver and navigate to Yahoo Finance
    service = Service(r"C:\path\to\chromedriver.exe")
    service.start()
    driver = webdriver.Remote(service.service_url)
    driver.get('https://finance.yahoo.com/')

    #Find stock info
    for stock in stock_list:
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
#change variables to reflect yours for twilio and your cell phone number \_(ツ)_/

def send_txt(from_num, to_num):
    account_sid = '<Enter your twilio account sid>'
    auth_token = '<Enter your twilio auth token>'
    client = Client(account_sid, auth_token)
    
    message = client.messages \
        .create(
            body = output,
            from_ = '+<Enter your twilio #>',
            to = '+<Enter cell # to send text to>'
    )
    
    print(message.sid)


def main():

    stock_list = []

    while True:
        stock = input("Enter ticker symbol or company name (Enter q or quit to get stock info)")
        if stock.lower() == 'q' or stock.lower() == 'quit':
            break
        if (sl.does_exist(r'C:\Users\rhone\Desktop\company_names.txt', stock)) or (sl.does_exist(r'C:\Users\rhone\Desktop\ticker_sym.txt', stock)):
            stock_list.append(stock)
            print(colored(stock, 'green'), "has been added to list of stocks")
        else:
            print(colored(stock, 'red'), "cannot be found in the NASDAQ, NYSE or AMEX")

    if len(stock_list) == 0:
        print("No stocks provided")
        sys.exit(0)
    else:
        output(stock_list)

if __name__ == '__main__':
    main()
