# -*- coding:utf-8 -*-
import pandas as pd

if __name__ == '__main__':
    p = pd.read_csv('../info_code/allInfo.csv')
    bool1 = p['content'].str.contains('路号|站名')
    bool2 = p['title'].str.contains('路号|站名')
    changeNameInfo = p[bool1|bool2]
    changeNameInfo.to_csv('changeNameInfo.csv')
