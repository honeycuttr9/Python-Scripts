"""
Scraps websites three websites for all traded equities on the NASDAQ, NYSE, and AMEX outputting their ticker symbols and company names
in two text files
"""

#! /usr/bin/python3
import requests
import time
import re
import string
from requests import get
from bs4 import BeautifulSoup
from string import ascii_uppercase

start_time = time.time()

ticker_sym  = []
company_name = []
alphabet_list = list(string.ascii_uppercase)

# retrieves stock company and ticker symbol info and adds it to their respective lists
def get_stock_info(self, url, html_soup):
    for element in html_soup.find_all(class_='ro'):
            x = [i.text for i in element('td')]
            if len(x) == 0:
                continue
            else:
                ticker_sym.append(x.pop(0))
                company_name.append(x.pop(0))

    for element in html_soup.find_all(class_='re'):
            x = [i.text for i in element('td')]
            if len(x) == 0:
                continue
            else:
                ticker_sym.append(x.pop(0))
                company_name.append(x.pop(0))

# get url and html content
def setup_env(self, url):
    response = get(url)
    html_content = requests.get(url).text
    html_soup = BeautifulSoup(response.text, 'html.parser')
    return html_soup

# gets amex stock data
def get_amex_data():
    for i in ascii_uppercase:
        url = 'http://eoddata.com/stocklist/AMEX/' + i + '.htm'
        html_soup = setup_env(url)
        get_stock_info(url, html_soup)

# gets nasdaq stock data
def get_nasdaq_data():
    for i in ascii_uppercase:
        url = 'http://eoddata.com/stocklist/NASDAQ/' + i + '.htm'
        html_soup = setup_env(url)
        get_stock_info(url, html_soup)

# gets nyse stock data
def get_nyse_data():
    for i in ascii_uppercase:
        url = 'http://eoddata.com/stocklist/NYSE/' + i + '.htm'
        html_soup = setup_env(url)
        get_stock_info(url, html_soup)
#add data to text file
def to_text_file_company_name(self, arr):
    with open(r'C:\Users\rhone\Desktop\company_names.txt', 'w+') as filehandle:
        filehandle.writelines("%s\n" % i for i in arr)

def to_text_file_ticker_sym(self, arr):
    with open(r'C:\Users\rhone\Desktop\ticker_sym.txt', 'w+') as filehandle:
        filehandle.writelines("%s\n" % i for i in arr)

def does_exist(file, string):
    line_num = 0
    with open(file, 'r') as read_obj:
        for line in read_obj:
            line_num += 1
            if re.search(string, line, flags=re.IGNORECASE):
                return True
    return False

def main():
    get_amex_data()
    get_nasdaq_data()
    get_nyse_data()

    to_text_file_company_name(company_name)
    to_text_file_ticker_sym(ticker_sym)

    #print(does_exist(r'C:\Users\rhone\Desktop\company_names.txt', "Apple"))
    #print(does_exist(r'C:\Users\rhone\Desktop\ticker_sym.txt', "ABEQ"))
    #print(ticker_sym.__contains__('YELP'))
    #print(ticker_sym.__contains__('QD'))
    #print(company_name.__contains__('Phillips'))
    #print(ticker_sym.__contains__('NACP'))

    print(company_name)
    print(ticker_sym)
    print(len(company_name))
    print(len(ticker_sym))

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()