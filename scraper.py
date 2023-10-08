import requests
from bs4 import BeautifulSoup
import re

def scrapeTOI(newslist):

    for link in newslist.values():
        link = re.sub(r'[{\'\'}]', '', link)

        r = requests.get(link)

        print(r)

        soup = BeautifulSoup(r.content, 'html.parser')

        content_div = soup.find('div',class_='_s30J clearfix')

        if content_div:
            text_inside_div = content_div.get_text(separator=".").replace('\n', '.').replace('..', '.')
            
            text_array = [segment.strip() for segment in text_inside_div.split('.') if segment.strip()]

            text_array = ''.join(text_array)
            print(text_array)

def scrapeHindu(newslist):

    for link in newslist.values():
        link = re.sub(r'[{\'\'}]', '', link)

        r = requests.get(link)

        print(r)

        soup = BeautifulSoup(r.content, 'html.parser')

        content_div = soup.find(name='div',class_='articlebodycontent col-xl-9 col-lg-12 col-md-12 col-sm-12 col-12')    

        if content_div:
            children = content_div.find_all('p', text = True, recursive=False)

            text_array = []

            for s in children:
                text_array.append(s.text)

            text_array = ''.join(text_array)
            print(text_array)

        else:
            print('couldnt fetch')