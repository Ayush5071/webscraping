# SOCIAL LINKS SCRAPING =========
import requests
from bs4 import BeautifulSoup as bs

r = requests.get("https://keithgalli.github.io/web-scraping/webpage.html")
webpage = bs(r.content,features="html.parser")

### Task-1 : Grab all of the social links from the webpage
## Method 1 :
list1 = []
links = webpage.select("li.social a")
for link in links:
    list1.append(link['href'])

## Method 2 :

links2 = webpage.find("ul",attrs={"class":"socials"})
link_list = links2.find_all("a")
actual_links = [link['href'] for link in link_list]


## Method 3 : One liner 

links3 = webpage.select("li.social a")



