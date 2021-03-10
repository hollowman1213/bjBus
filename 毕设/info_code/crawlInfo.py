# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import bs4
import time
import pandas as pd

def crawlNoticeLink(num):
    data = {
        'txtPage':num,
        'txtDisplayRows':9,
        'txtType':1,
        'txtCode':'',
        'txtContainer':'content',
        'txtStyle':2
    }
    head = {
        'Host': 'www.bjbus.com',
        'Origin': 'http://www.bjbus.com',
        'User-Agent': 'Mozilla/5.0',
        'Referer': 'http://www.bjbus.com/home/fun_news_list.php?uNewsType=1&uStyle=2&uSec=00000177&uSub=00000178',
        'X-Requested-With': 'XMLHttpRequest'
    }
    try:
        r = requests.post('http://www.bjbus.com/home/ajax_news_list.php', data=data, headers=head)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text,'html.parser')
        hrefs = soup.find_all(href=re.compile('fun_news_detail.php'))
        l = len(hrefs)
        rst = []
        for i in range(0, l, 2):
            rst.append(hrefs[i]['href'])
        return rst
    except:
        return []

def crawlDetailPage(links):
    rootUrl = 'http://www.bjbus.com/home/'
    l = len(links)
    totTitle = []
    totArticle = []
    changeInfoTitle = []
    changeInfoArticle = []
    for i in range(l):
        try:
            r = requests.get(rootUrl + links[i],headers = {'User-Agent':'Mozilla/5.0'})
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            soup = BeautifulSoup(r.text,'html.parser')
            title = ''
            title = soup.find('h1',class_= 'title')
            title = str(title.string)
            articleCont = soup.find('div',class_='article_cont')
            article = ''
            for child in articleCont.children:
                if isinstance(child, bs4.element.Tag):
                    article += str(child.text)
            if article != '' and title != '':
                print(title)
                totTitle.append(title)
                totArticle.append(article)
                if '临时' in title or '降雨影响' in title:
                    continue
                if ('路' in title or '线' in title or '站' in title) and \
                        ('停' in title or '增' in title or '新开' in title or '调整' in title or '撤销' in title or '取消' in title):
                    pass
                else:
                    continue
                changeInfoArticle.append(article)
                changeInfoTitle.append(title)

        except:
            continue
        return totTitle,totArticle,changeInfoTitle,changeInfoArticle


def printNotice(rideNotice):
    tplt = '{0:^5}\t{1:{3}<50}\t{2:<}'
    print(tplt.format('序号', '标题', '内容(前50字)', chr(12288)))
    l = len(rideNotice)
    for i in range(l):
        global cnt
        cnt = cnt + 1
        print(tplt.format(cnt, rideNotice[i][0], rideNotice[i][1][:100], chr(12288)))


if __name__ == '__main__':
    # totPage = input("请输入通告页数：")
    # totPage = int(totPage)
    totPage = 220
    for i in range(totPage):
        curLink = []
        try:
            curLink = crawlNoticeLink(i)
        except:
            continue
        time.sleep(0.1)
        ret = crawlDetailPage(curLink)
    totPdTitle = pd.Series(ret[0])
    totPdArticle = pd.Series(ret[1])
    changeInfoPdTitle = pd.Series(ret[2])
    changeInfoPdArticle = pd.Series(ret[3])
    totData = pd.DataFrame({'title':totPdTitle,'content':totPdArticle})
    changeInfoData = pd.DataFrame({'title':changeInfoPdTitle,'content':changeInfoPdArticle})
    totData.to_csv('allInfo.csv')
    changeInfoData.to_csv('changeInfo.csv')
