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
    
    hls = []
    links = []

    soup = BeautifulSoup(content, "html.parser")
    for i in soup.find_all("span", class_="container__headline-text"):
        hl = i.get_text(strip=True)
        if hl in hls:
            pass
        else:
            hls.append(hl)
    
    for j in soup.find_all("a", class_="container__link container__link--type-article container_list-headlines__link"):
        link = j['href']
        if link.startswith('/'):
            link = "https://www.cnn.com" + link
        links.append(link)
    
    for x in soup.find_all("a", class_="container__link container__link--type-article container_lead-plus-headlines-with-images__link"):
        link = x['href']
        if link.startswith('/'):
            link = "https://www.cnn.com" + link
        if link in links:
            pass
        else:
            links.append(link)
    
    for y in soup.find_all("a", class_="container__link container__link--type-article container_vertical-strip__link"):
        link = y['href']
        if link.startswith('/'):
            link = "https://www.cnn.com" + link
        if link in links:
            pass
        else:
            links.append(link)
    
    for z in soup.find_all("a", class_="container__link container__link--type-article container_lead-plus-headlines__link"):
        link = z['href']
        if link.startswith('/'):
            link = "https://www.cnn.com" + link
        if link in links:
            pass
        else:
            links.append(link)

    print("Scraping headlines...")
    
    sd = {"Headlines" : hls, "Links": links}
    fsd = pd.DataFrame.from_dict(sd, orient="index")
    fsd = fsd.transpose()
    fsd.index = fsd.index.map(lambda x:"|index " + str(x))
    fsd.iloc[:,0] = fsd.iloc[:,0].apply(lambda x:"| " + str(x))
    fsd.to_csv("CNN_Headlines.csv", sep=" ", header=None, index=False)

data_scraping()

schedule.every().day.at("12:00").do(data_scraping)

while True:
    schedule.run_pending()
    time.sleep(60)