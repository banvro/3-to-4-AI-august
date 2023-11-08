from bs4 import BeautifulSoup
import requests


url = "https://www.merriam-webster.com/dictionary/excellence"
# url = "https://www.amazon.in/s?k=toys&crid=1QV9O6FS0AXYD&sprefix=toy%2Caps%2C252&ref=nb_sb_noss_1"

data = requests.get(url)

resp = data.text

soup = BeautifulSoup(resp, 'html.parser')

zx = soup.find_all("a")

# print(zx, "xxxxx")

for i in zx:
    print(i.get("href"))

    
