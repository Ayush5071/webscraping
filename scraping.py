import requests
from bs4 import BeautifulSoup as bs

r = requests.get("https://keithgalli.github.io/web-scraping/example.html") # loaing web page

# Convert to a beatiful soup object

soup = bs(r.content,features="html.parser")

# print(soup.prettify()) # using prettify method  we get better code formatting 

# for grabbing specific elements
first_heading = soup.find('h1') # finds only first element.

headers = soup.find_all("h2") # we get the list of target elements

# we can also passattributes to find and find_all functions

paragraph = soup.find_all("p",attrs={"id":"paragraph-id1"})

# we can search for specific string also : 

specific_text = soup.find_all("p",string="Some bold text") 

# we can modify this , using regex library to even search for single word

import re

specific_word = soup.find_all("p",string=re.compile("Some")) ### really OP


specific_word_diff_capitalisation = soup.find_all("h2",string=re.compile("(h|H)eader"))

########### select for selecting elements based on css






