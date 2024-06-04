# EXERCISE 3 : select all the fun facts containing word "is" 

import requests
from bs4 import BeautifulSoup as bs
import re

r = requests.get("https://keithgalli.github.io/web-scraping/webpage.html")
webpage = bs(r.content,features="html.parser")

facts = webpage.select("ul.fun-facts li")
ans = [fact.find(string=re.compile("is")) for fact in facts]
print(ans)