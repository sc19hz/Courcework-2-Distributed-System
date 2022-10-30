# -*- coding:utf-8 -*-
from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
from config import Config
import sqlite3
import urllib.request
import json
from flask_cors import *

app = Flask(__name__)
CORS(app, supports_credentials=True)  # 允许跨域请求
app.config.from_object(Config)
api = Api(app)


class Service0(Resource):
    def get(self, date, province):
        conn = sqlite3.connect('new.db')
        sql1 = "SELECT cityZh FROM city where provinceZh="
        sql2 = " and suitable_date like "
        str1 = "'%"
        str2 = "%'"
        str3 = "'"
        sql = sql1 + str3
        sql = sql + province
        sql = sql + str3
        sql = sql + sql2
        sql = sql + str1
        sql = sql + date
        sql = sql + str2
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        row = rows[0]
        res = ''.join(row)
        return res


api.add_resource(Service0, '/<string:date>/<string:province>')
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='5000')
