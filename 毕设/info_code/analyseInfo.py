# -*- coding:utf-8 -*-
import pandas as pd
def readReason():
    ret = {}
    content = ""
    with open('reason.txt','r') as f:
        content = f.read()
    content = content.splitlines()
    for r in content:
        r = r.split('：')
        ret[r[0]] = r[1].split('，')
    return ret
if __name__ == '__main__':
    reasons = readReason()
    data = pd.read_csv('allInfo.csv',index_col=0)
    newsNum = data.shape[0]
    # dict用以建立新的列，该列表示每条新闻所属的类别
    dict = {}
    for i in range(newsNum):
        curClassify = ""
        news = data.loc[i]['content']
        if len(news) >= 100:
            news = news[:100]
        for k in reasons.keys():
            keyWords = reasons[k]
            for word in keyWords:
                if word in news:
                    curClassify = curClassify + " " + k
                    break
            if curClassify != "":
                break
        dict[i] = curClassify

    data['classification'] = pd.Series(dict)
    data.to_csv('allinfo.csv')
