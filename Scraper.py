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