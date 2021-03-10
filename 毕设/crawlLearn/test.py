# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        return r.text
    except:
        return ""


def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,'html.parser')
    # print(soup.prettify())
    table = soup.find('table','rk-table')
    tbody = table.find('tbody')
    # print(tbody)
    for univ in tbody.children:
        if isinstance(univ,bs4.element.Tag):
            tds = univ('td')
            ulist.append([tds[0].text, tds[1].text, tds[4].text])

def printUnivList(ulist,num):
    print('{0:<10}\t{1:{3}<10}\t{2:<10}'.format('排名','学校名称','总分',chr(12288)))
    for i in range(num):
        print('{0:<10}\t{1:{3}<10}\t{2:<10}'.format(ulist[i][0].strip(),ulist[i][1].strip(),ulist[i][2].strip(),chr(12288)))

def main():
    uinfo = []
    url = "https://www.shanghairanking.cn/rankings/bcur/2020"
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,len(uinfo))

main()


