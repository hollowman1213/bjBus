# -*- coding:utf-8 -*-
import hashlib
import re
from urllib import parse

import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS

info = Flask(__name__)
CORS(info)

@info.route('/',methods=['GET','POST'])
def getStationByRoute():
    p = pd.read_csv("../info_code/allinfo.csv",index_col=0)
    p = p.to_json(orient='records',force_ascii=False)
    return jsonify(ret=p)

if __name__ == '__main__':
    info.run()