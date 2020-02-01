#!/usr/bin/env python3

import socket
import requests
from ipwhois import IPWhois 


def getIP(url): 
  try: 
    ip = socket.gethostbyname(url)
    print("IP Address: ", ip)
  except Exception as e: 
    print("Couldn't resolve url to ip address")
    exit()  

def hostStatus(url):
    url2 = "http://" + url
    code = requests.head(url2)
    print("Website status code is: ", code)
    
def whois(url): 
    ip = socket.gethostbyname(url)
    w = IPWhois(ip)
    results = w.lookup_whois()
    print ('NIR: ', str(results['nir']))
    print ('ASN Registry: ', str(results['asn_registry']))
    print ('ASN: ', str(results['asn']))
    print ('ASN CIDR: ', str(results['asn_cidr']))
    print ('Country: ', str(results['asn_country_code']))
    print ('ASN Date: ', str(results['asn_date']))
    print ('ASN Description: ', str(results['query']))
    print ('Query: ', str(results['asn_registry']))
    for k, v in results['nets'][0].items(): 
      print ('{} : ' .format(str(k)) + str(v))


def main(): 
  url = input("Enter the website url: ")
  print("Target is ", url)
  getIP(url)
  whois(url)
main()
  

