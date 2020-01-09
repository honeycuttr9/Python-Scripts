#! /usr/bin/python

# Importing required modules
import requests
import subprocess
import sys
import os 
from bs4 import BeautifulSoup
import urlparse #urlparse is renamed to urllib.parse in Python
# Get the page with the requests
response = requests.get('https://www.hackingarticles.in/overthewire-natas-walkthrough-0-11/')

# Parse the page with BeautifulSoup
parse = BeautifulSoup(response.text)

# Get all image tags
image_tags = parse.find_all('img')

# Get urls to the images
images = [ url.get('src') for url in image_tags]

# If no images found in the page
if not images:
 sys.exit("Found No Images")

# Convert relative urls to absolute urls if any
images = [urlparse.urljoin(response.url, url) for url in images]
print 'Found %s images' % len(images)

# Download images to downloaded folder
for url in images:
 r = requests.get(url)
 #enter path that you're running script form and that pics will get downloaded tocd 
 f = open("/home/honeycutt/Documents/Python Scripts/pictures/%s" % url.split('/')[-1], 'w')
 f.write(r.content)
 f.close()
 print 'Downloaded %s' % url

print '\nFinished Downloading all %s images' % len(images)
