import requests
import re
from bs4 import BeautifulSoup
url = 'https://www.amazon.in/s?k=ring&ref=nb_sb_noss'
data = requests.get(url)
soupObj = BeautifulSoup(data.content, "html.parser")
brand = re.findall(r'<span class="a-size-base-plus a-color-base">(.*?)</span>', str(soupObj))
print('Brand:', brand)
price = re.findall(r'<span class="a-price-whole">(.*?)</span>', str(soupObj))
print('Price :', price)
