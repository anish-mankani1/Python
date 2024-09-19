import requests
from bs4 import BeautifulSoup
with open ("z.html","r") as f:
    h=f.read()

soup=BeautifulSoup(h,'html.parser')
print(soup.prettify()v.html
)