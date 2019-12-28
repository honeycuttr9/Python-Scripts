#!/usr/bin/env python

#import libraries
import csv
import urllib3
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
from requests import get

# Declaring lists to store data
names = []
addresses = []
numbers = []

  
def findInfo(what, city, state):
  # add user input to generic url to search
  url = 'https://www.yellowbook.com/s/' + what + '/' + city + '-' + state + '/'
  response = get(url)

  # Parse content of the request with BeautifulSoup
  html_soup = BeautifulSoup(response.text, 'html.parser')

  # Select all containers from a single page
  restaurant_containers = html_soup.find_all('div', class_ = 'listing-info')

  for container in restaurant_containers:
    #check if resaurant has name then extract
    if container.find('div', class_ = 'address c') is not None:
      #Restaurant name
      name = container.h2.a.text
      names.append(name)
    
      address = container.find('div', class_ = 'address c').text
      addresses.append(address)

      number = container.find('div', class_ = 'phone-number').text
      numbers.append(number)
  
  display_results = pd.DataFrame({what: names, 
  'address': addresses, 
  'number': numbers
  })

  print(display_results)

# get user input
while True:
  what = input("Enter what you want to search for ")
  city = input("Enter the city you want to search ")
  state = input("Enter the state of the city in abbreviated format (ex: NC = North Carolina)") 
  
  if len(state) > 2 or len(state) < 2:
    print("State abbreviation can only be 2 characters")
    break
  elif state.isdigit():
    print("State cannot be a digit")
    break
  else: 
    findInfo(what, city, state)
