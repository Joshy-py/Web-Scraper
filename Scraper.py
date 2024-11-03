import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time

url = "https://www.cnn.com/business/tech"
response = requests.get(url)

if (response.status_code == 200):
    content = response.text
else:
    print("Failed to retreive page, maybe it's down?")

soup = BeautifulSoup(content, "html.parser")
hl = soup.find_all("span", class_="container__headline-text")
for i in range(len(hl)):
    print(hl[i].text)
