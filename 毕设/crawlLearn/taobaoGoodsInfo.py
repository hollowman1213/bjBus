# -*- coding:utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup

def searchHTML(url):
    try:
        r = requests.get(url,headers = {'User-Agent':'Mozilla/5.0','cookie':'_cc_=Vq8l%2BKCLiw%3D%3D; _l_g_=Ug%3D%3D; _nk_=%5Cu7B49%5Cu5F52%5Cu67651388; _tb_token_=5565bee6136e; cookie1=BYfkFCqWzJQll9cCnKHNlQ%2B2NimUn7dJrM5MmmHjPyM%3D; cookie17=UNX%2FRstO8aFyzA%3D%3D; cookie2=1f8708d92bfc716776e877457b6a0067; csg=e25e639d; dnk=%5Cu7B49%5Cu5F52%5Cu67651388; existShop=MTYwNzU4MjMwOQ%3D%3D; isg=BP__gk--nOefDZiWLqiywAw6jNWJ5FOGgBU-OZHMm671oB8imbTj1n2z4vBe4yv-; l=eBIcLd0lOlg47c0JBOfahurza77OSIdYYuPzaNbMiOCP_Q1B5e1CWZJjnhL6C31Vh6b6R3WAR1y8BeYBcQRrnxv9SV7Rs1Dmn; lgc=%5Cu7B49%5Cu5F52%5Cu67651388; sg=86a; sgcookie=E100%2Fe0lJ1clLFI29lPcih6e36uMThf8%2Bh8k4Y3ohCNptq9huMNVrXdymhpPAv5XQWBDshqH9JjtWVxJkNNEJSakfg%3D%3D; skt=f72c8fe6cba90444; t=d4fd89e48926c5637c34501f7584b837; tfstk=csJPB7MmM9YfuRBOET6UOTH8JbxRZ9vMprSCZBspAjYZygBlM3WpakHsfa3Q9; tracknick=%5Cu7B49%5Cu5F52%5Cu67651388; uc1=cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&pas=0&existShop=false&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&cookie14=Uoe0al0vBE9Qlw%3D%3D&cookie21=VFC%2FuZ9ainBZ; uc3=vt3=F8dCuAJ1IMvlSbmBMJs%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D&id2=UNX%2FRstO8aFyzA%3D%3D&nk2=1oeqdmyRBNPfvg%3D%3D; uc4=id4=0%40UgJ6xUezWScu0SrM%2BtZucafxaIiK&nk4=0%401Db8X6Sk80jsbn34y2odpIeLWkZA; unb=3543333406; cna=/qpYGPpSmzgCAXzNTVpoeuO/; hng=CN%7Czh-CN%7CCNY%7C156; mt=ci=0_0; thw=cn; ubn=p; ucn=center; enc=4ZkpAPvD21Rle%2FihQp1wvt6SMwxY3EqQr1L%2F%2BEUJyOMpz0G6TWb8HKO5zkVNGtqFxRb5TG1bhMe%2F43x3ZyZl2g%3D%3D; xlly_s=1; _m_h5_tk=54579be44ce589dd457aa092b0b29b58_1607589927215; _m_h5_tk_enc=44b2245df02d9e7a867fbcb222294f89; _samesite_flag_=true'})
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


def parsePage(ilt,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        l = len(plt)
        for i in range(l):
            price = eval(plt[i].split(':')[1]) #eval：对括号内的字符串求值
            title = eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        print('parsePage error')


def printGoodsList(ilt):
    tplt = '{:<4}\t{:<8}\t{:<16}'
    print(tplt.format('序号','价格','商品名称'))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count,g[0],g[1]))


def main(goods:str,depth = 2):
    infoList = []
    url = 'https://s.taobao.com/search?q=' + goods
    for i in range(depth):
        curPageUrl = url + '&s=' + str(44*i)
        try:
            html = searchHTML(curPageUrl)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)


if __name__ == '__main__':
    main('书包',3)