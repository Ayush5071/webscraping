# Exercise 2 - scrape/extract the information of the table 

import requests
from bs4 import BeautifulSoup as bs 
import pandas as pd

r = requests.get("https://keithgalli.github.io/web-scraping/webpage.html")
webpage = bs(r.content,features="html.parser")

table = webpage.select("table")[0]
columns = table.find("thead").find_all("th")
column_names = [c.string for c in columns]

table_rows = table.find("tbody").find_all("tr")

l = []

for tr in table_rows:
    td = tr.find_all('td')
    row = [str(tr.get_text()).strip() for tr in td] # here some of the td are nested elements so, .string not used -> get_text()
    l.append(row)

# Now creating pandas dataframe

df = pd.DataFrame(l,columns=column_names,)
print(df)
