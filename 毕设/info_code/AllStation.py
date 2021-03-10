# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

def GetStationByRoute(url):
    ret = [[],[]]
    try:
        time.sleep(1)
        r = requests.get(url,headers={'User-Agent':'Mozilla/5.0'})
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text,'html.parser')
        stationList = soup.select('ul[id="scrollTr"]')
        stationList = stationList[0]
        for child in stationList.descendants:
            if child.name == 'em':
                ret[0].append(str(child.string))
    except:
        pass
    try:
        time.sleep(1)
        r = requests.get(url+'/1', headers={'User-Agent': 'Mozilla/5.0'})
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, 'html.parser')
        stationList = soup.select('ul[id="scrollTr"]')
        stationList = stationList[0]
        for child in stationList.descendants:
            if child.name == 'em':
                ret[1].append(str(child.string))
    except:
        pass
    print(ret)
    return ret

def GetRoutes(url):
    retStations = []
    index = [[],[]]
    try:
        r = requests.get(url,headers={'User-Agent':'Mozilla/5.0'})
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text,'html.parser')
        # print(r.text)
        RouteWeb = soup.find_all('a',title = re.compile('北京.+?公交线路'))
        # print(RouteWeb)
        for web in RouteWeb:
            print(web['href'])
            index[0].append(str(web.string))
            index[0].append(str(web.string))
            index[1].append('上行')
            index[1].append('下行')
            time.sleep(2)
            stations = GetStationByRoute(web['href'])
            retStations.append(stations[0])
            retStations.append(stations[1])
    except:
        pass
    return (retStations,index)

if __name__ == '__main__':
    url = 'https://bus.mapbar.com/beijing/xianlu'
    ret = GetRoutes(url)
    # ret = ([['1',2,3,4],[1,2],[1,2,3],[1]],[['a','a','b','b'],[0,-1,0,-1]])
    longestRoute = len(max(ret[0],key=len))
    cols = [i for i in range(1,longestRoute+1)]
    p = pd.DataFrame(ret[0],index=ret[1],columns=cols)
    p = p.fillna(' ')
    p.to_csv('routeAndStation.csv')
    print(p)