#import what we need
from urllib import request
from requests_html import HTMLSession
from requests_testadapter import Resp
import os
import requests
import scraper

class LocalFileAdapter(requests.adapters.HTTPAdapter):
    def build_response_from_file(self, request):
        file_path = request.url[7:]
        with open(file_path, 'rb') as file:
            buff = bytearray(os.path.getsize(file_path))
            file.readinto(buff)
            resp = Resp(buff)
            r = self.build_response(request, resp)

            return r

    def send(self, request, stream=False, timeout=None,
             verify=True, cert=None, proxies=None):

        return self.build_response_from_file(request)

def getTOI():
    session = HTMLSession()
    session.mount('file://', LocalFileAdapter())

    rt = session.get('file://rssPages\TOI.html')
    articles = rt.html.find('div div.entry-title-wrapper-dummy')

    newslist = {}

    for item in articles:
        try:
            newsitem = item.find('a', first=True)
            title = newsitem.text
            link = str(item.absolute_links)
            newslist[title] = link
        except:
            pass

    return scraper.scrapeTOI(newslist)

def getHindu():
    session = HTMLSession()
    session.mount('file://', LocalFileAdapter())

    rh = session.get('file://rssPages\Hindu.html')
    articles = rh.html.find('div div.entry-title-wrapper-dummy')

    newslist = {}

    for item in articles:
        try:
            newsitem = item.find('a', first=True)
            title = newsitem.text
            link = str(item.absolute_links)
            newslist[title] = link
        except:
            pass

    return scraper.scrapeHindu(newslist)

def getNDTV():
    session = HTMLSession()
    session.mount('file://', LocalFileAdapter())

    rh = session.get('file://rssPages\\ndtv.html')
    articles = rh.html.find('div div.entry-title-wrapper-dummy')

    newslist = {}

    for item in articles:
        try:
            newsitem = item.find('a', first=True)
            title = newsitem.text
            link = str(item.absolute_links)
            newslist[title] = link
        except:
            pass

    return scraper.scrapeNDTV(newslist)

def getOnion():
    session = HTMLSession()
    session.mount('file://', LocalFileAdapter())

    rh = session.get('file://rssPages\\onion.html')
    articles = rh.html.find('div div.entry-title-wrapper-dummy')

    newslist = {}

    for item in articles:
        try:
            newsitem = item.find('a', first=True)
            title = newsitem.text
            link = str(item.absolute_links)
            newslist[title] = link
        except:
            pass

    return scraper.scrapeOnion(newslist)

def getPunk():
    session = HTMLSession()
    session.mount('file://', LocalFileAdapter())

    rh = session.get('file://rssPages\\punk.html')
    articles = rh.html.find('div div.entry-title-wrapper-dummy')

    newslist = {}

    for item in articles:
        try:
            newsitem = item.find('a', first=True)
            title = newsitem.text
            link = str(item.absolute_links)
            newslist[title] = link
        except:
            pass

    return scraper.scrapePunk(newslist)