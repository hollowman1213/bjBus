# -*- coding:utf-8 -*-
import hashlib
import re
from urllib import parse

import pandas as pd
import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

map = Flask(__name__)
CORS(map)

def ListToStr(l):
    ret = ' '.join(l)
    ret = ret.split()
    ret = ret[2:]
    return ret

@map.route('/station',methods=['GET','POST'])
def getStationByRoute():
    p = pd.read_csv("../info_code/routeAndStation.csv")
    route = request.args.get("route")
    stations1 = p[(p['Unnamed: 0']==route)&(p['Unnamed: 1']=="上行")]
    stations2 = p[(p['Unnamed: 0'] == route) & (p['Unnamed: 1'] == "下行")]
    ret1 = ListToStr(list(stations1.iloc[0]))
    ret2 = ListToStr(list(stations2.iloc[0]))
    data = []
    for s in ret1:
        #l = getStationInfo(s)
        #print(s,l)
        #data.append(l)
        data.append(s)
    data.append('/')
    for s in ret2:
        #l = getStationInfo(s)
        #print(s,l)
        #data.append(l)
        data.append(s)
    data = ' '.join(data)
    return jsonify(ret=data)

def GetInfoUrl(address):
    # 以get请求为例http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak
    queryStr = '/geocoding/v3/?address=%s&output=json&ak=Z04uSU5SNotWF8LLajBU7xG8gE3MlqBI'%address
    # 对queryStr进行转码，safe内的保留字符不转换
    encodedStr = parse.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")
    # 在最后直接追加上yoursk
    rawStr = encodedStr + 'qyqP1SkIDnaWEE72gjmdyReWtVSjcEhR'
    # print(rawStr)
    # md5计算出的sn值7de5a22212ffaa9e326444c75a58f9a0
    # 最终合法请求url是http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak&sn=7de5a22212ffaa9e326444c75a58f9a0
    sn = (hashlib.md5(parse.quote_plus(rawStr).encode("utf-8")).hexdigest())
    url = parse.quote("http://api.map.baidu.com" + queryStr + "&sn=" + sn, safe="/:=&?#+!$,;'@()*[]")
    return url

def getStationInfo(address):
    url = GetInfoUrl(address)
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        if r.text[10] == "1":
            return ""
        else:
            # print(address,r.text[10])
            locate = re.findall(r'[0-9 .]{3,20}',r.text)
            return locate[0] + "+" + locate[1]
    except:
        print("爬取失败")

if __name__ == '__main__':
    map.run()
    # getStationInfo("天安门广场")