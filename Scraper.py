import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time

def data_scraping():
    url = "https://www.cnn.com/business/tech"
    response = requests.get(url)
    if (response.status_code == 200):
        content = response.text
    else:
        print("Failed to retreive page, maybe it's down?")

    soup = BeautifulSoup(content, "html.parser")
    hl = soup.find_all("span", class_="container__headline-text")
    print("Scraping headlines...")
    
    sd = pd.DataFrame(hl, columns=["Headlines"])
    sd.index = sd.index.map(lambda x:"|index " + str(x))
    sd.iloc[:,0] = sd.iloc[:,0].apply(lambda x:"| " + str(x))
    sd.to_csv("CNN_Headlines.csv", sep=" ", header=None, index=False)

data_scraping()

schedule.every().day.at("12:00").do(data_scraping)

while True:
    schedule.run_pending()
    time.sleep(60)