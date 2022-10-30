# -*- coding:utf-8 -*-
from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
from config import Config
import urllib.request
import json
from flask_cors import *

app = Flask(__name__)
CORS(app, supports_credentials=True)  # 允许跨域请求
app.config.from_object(Config)
api = Api(app)


class Service2(Resource):
    def get(self, id):
        # """Get the weather interface"""
        host = 'https://v0.yiketianqi.com/api'
        querys = 'unescape=1&version=v61&appid=68185384%20&appsecret=4i9jWmpe&cityid='
        url = host + '?' + querys + id
        request = urllib.request.Request(url)
        # According to the requirements of the API, define the corresponding Content-Type
        request.add_header('Content-Type', 'application/json; charset=UTF-8')
        response = urllib.request.urlopen(request)
        content = response.read().decode(encoding='UTF-8', errors='ignore')
        city_dict = json.loads(content)
        a = []
        a.append(city_dict['date'])
        a.append(city_dict['week'])
        a.append(city_dict['city'])
        a.append(city_dict['country'])
        a.append(city_dict['wea'])  # weather
        if int(city_dict['tem1']) < int(city_dict['tem2']):  # 最低温和最高温
            a.append(city_dict['tem1'])
            a.append(city_dict['tem2'])
        else:
            a.append(city_dict['tem2'])
            a.append(city_dict['tem1'])
        a.append(city_dict['win'])  # 风向
        a.append(city_dict['win_speed_day'])
        a.append(city_dict['humidity'])  # 湿度
        a.append(city_dict['air_level'])  # 空气质量
        dic2 = city_dict['aqi']
        a.append(dic2['air_tips'])  # tip1
        a.append(dic2['kouzhao'])  # tip2
        a.append(dic2['yundong'])  # tip3
        a.append(dic2['waichu'])  # tip4
        a.append(dic2['kaichuang'])  # tip5
        a.append(dic2['jinghuaqi'])  # tip6

        return a
        return content


api.add_resource(Service2, '/<string:id>')
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='5002')
