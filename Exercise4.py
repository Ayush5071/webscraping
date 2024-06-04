# grab and download an image 

import requests
from bs4 import BeautifulSoup as bs

url = "https://keithgalli.github.io/web-scraping/"
r = requests.get(url + "webpage.html")
webpage = bs(r.content,features="html.parser")

images = webpage.select("div.row div.column img")
image_url = images[0]['src']

full_url = url + image_url

img_data = requests.get(full_url).content
with open('lake_como.jpg','wb') as handler:
    handler.write(img_data)
