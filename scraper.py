import requests
from bs4 import BeautifulSoup
import re

def scrapeTOI(newslist):

    data = []

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
            # print(text_array)
            data.append(text_array)

    return data

def scrapeHindu(newslist):

    data = []

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
            # print(text_array)
            data.append(text_array)

        else:
            print('couldnt fetch')

    return data

def scrapeNDTV(newslist):

    data = []

    for link in newslist.values():
        link = re.sub(r'[{\'\'}]', '', link)

        r = requests.get(link)

        print(r)

        soup = BeautifulSoup(r.content, 'html.parser')

        content_div = soup.find('div',class_='sp-cn ins_storybody')

        if content_div:
            text_inside_div = content_div.get_text(separator=".").replace('\n', '.').replace('..', '.')
            
            text_array = [segment.strip() for segment in text_inside_div.split('.') if segment.strip()]

            text_array = ''.join(text_array)

            text_array = re.sub(r'(This story has not been edited by NDTV staff and is auto-generated from a syndicated feed)', '', text_array)
            text_array = re.sub(r'(Except for the headline, this story has not been edited by NDTV staff and is published from a syndicated feed)', '', text_array)

            # print(text_array)
            data.append(text_array)

    return data

def scrapeOnion(newslist):

    data = []

    for link in newslist.values():
        link = re.sub(r'[{\'\'}]', '', link)

        r = requests.get(link)

        print(r)

        soup = BeautifulSoup(r.content, 'html.parser')

        content_div = soup.find('div',class_='sc-r43lxo-1 cwnrYD')

        if content_div:
            text_inside_div = content_div.get_text(separator=".").replace('\n', '.').replace('..', '.')
            
            text_array = [segment.strip() for segment in text_inside_div.split('.') if segment.strip()]

            text_array = ''.join(text_array)
            # print(text_array)
            data.append(text_array)

    return data

def scrapePunk(newslist):

    data = []

    for link in newslist.values():
        link = re.sub(r'[{\'\'}]', '', link)

        r = requests.get(link)

        print(r)

        soup = BeautifulSoup(r.content, 'html.parser')

        content_div = soup.find('div',class_='post-content')

        if content_div:
            text_inside_div = content_div.get_text(separator=".").replace('\n', '.').replace('..', '.')
            
            text_array = [segment.strip() for segment in text_inside_div.split('.') if segment.strip()]

            text_array = ''.join(text_array)
            # print(text_array)
            data.append(text_array)

    return data