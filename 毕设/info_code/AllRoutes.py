# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
def GetRoutes(url):
    retStations = []
    try:
        r = requests.get(url,headers={'User-Agent':'Mozilla/5.0'})
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text,'html.parser')
        # print(r.text)
        RouteWeb = soup.find_all('a',title = re.compile('北京.+?公交线路'))
        # print(RouteWeb)
        for web in RouteWeb:
            retStations.append(web.string)
    except:
        pass
    return ' '.join(retStations)

if __name__ == '__main__':
    url = 'https://bus.mapbar.com/beijing/xianlu'
    ret = GetRoutes(url)
    print(ret)