#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import Flask, jsonify,render_template,request
from argparse import ArgumentParser
import redis
import json
pool = redis.ConnectionPool(host='127.0.0.1', port=6379 ,decode_responses=True)  
r = redis.Redis(connection_pool=pool)

app = Flask(__name__)

@app.route('/api/blocks/all',methods=['POST','GET'])
def blocks():
    if (r.get("block_height")):
        block_height = int(r.get("block_height"))
        print ("block height:{0}".format(block_height))

        blockchain = []

        for i in range(0,block_height+1):
            block = r.hgetall("block_{0}".format(i))
            
            blockchain.append(block)

        #print (blockchain[0][b"this_hash"].decode('utf-8'))
        return jsonify(blockchain)
    else:
        print ("None")

    

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=8080, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    app.run(debug=True,host='0.0.0.0',port=port)
