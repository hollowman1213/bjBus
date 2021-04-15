# -*- coding:utf-8 -*-
import pandas as pd
import os

def insertInfo(p,old,new,time):
    lenIndex = len(p.index)
    lenCol = len(p.columns)
    if lenCol == 0:
        p['1'] = []
        p['2'] = []
        p.loc[lenIndex] = [time+' ' +new,old]
        return p
    lineWithOld = p[p['1'].str.contains(old)]
    if lineWithOld.empty:
        newLine = [time+' '+new, old]
        newLine.extend(['' for i in range(lenCol - 2)])
        p.loc[lenIndex] = newLine
    else:
        idx = lineWithOld.index[0]
        l = list(p.loc[idx])
        l.insert(0, time+' '+new)
        if len(l) > lenCol:
            p[lenCol] = ['' for i in range(lenIndex)]
        p.loc[idx] = l
    return p

if __name__ == '__main__':
    if os.path.exists('oldRoute.csv'):
        routes = pd.read_csv('oldRoute.csv',index_col=0)
    else:
        routes = pd.DataFrame()
    if os.path.exists('oldStation.csv'):
        stations = pd.read_csv('oldStation.csv',index_col=0)
    else:
        stations = pd.DataFrame()

    print('请输入路号/站名变化\n路号变化：输入四个变量，以空格隔开，第一个变量为数字0，第二个变量为修改前的路号，第三个变量为修改后的路号，第四个为修改的通知时间，如\n0 1路 2路 20110101（将1路改名为2路）'
          '\n站名变化：输入四个变量，以空格隔开，第一个变量为数字1，第二个变量为修改前的站名，第三个变量为修改后的站名，第四个为修改的通知时间，如\n1 北大南门站 北大东门站 20110101（将北大南门站更名为北大东门站）\n')

    while True:
        Input = input("请输入：")
        Input = Input.split()
        if Input[0] == '0':
            routes = insertInfo(routes,Input[1],Input[2],Input[3])
            routes.to_csv('oldRoute.csv')
            print(Input[1]+' ' + Input[2]+' complete')
        else:
            stations = insertInfo(stations,Input[1],Input[2],Input[3])
            stations.to_csv('oldStation.csv')
            print(Input[1]+' ' + Input[2]+' complete')

