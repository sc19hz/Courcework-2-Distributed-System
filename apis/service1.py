from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
from config import Config
import sqlite3
from flask_cors import *

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config.from_object(Config)
api = Api(app)


class Service1(Resource):
    def get(self, name):
        conn = sqlite3.connect('new.db')
        sql = "SELECT id FROM city where cityZh="
        str1 = '"'
        sql = sql + str1
        sql = sql + name
        sql = sql + str1
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        row = rows[0]
        res = ''.join(row)
        res = res[2:]
        p = jsonify(res)
        # print(type(p))
        return res


api.add_resource(Service1, '/<string:name>')
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='5001')
