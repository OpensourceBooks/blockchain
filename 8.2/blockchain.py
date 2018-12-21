#!/usr/bin/python
# -*- coding:utf-8 -*-
import hashlib as hasher
from time import time
import json
from flask import Flask, jsonify,render_template,request
from argparse import ArgumentParser
import requests

import requests
import base64
import ecdsa

from blockchain_helper import *

bch = BlockchainHelper()

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    # 查找
    if request.method == 'POST':
        address=request.form.get('address')

        out_logs=[]
        in_logs=[]

        blockchain = bch.get_blocks()

        for i in range(1,len(blockchain)):
            block=blockchain[i]
            if address == block["consignor"]:
                out_logs.append(block)
            if address == block["consignee"]:
                in_logs.append(block)
        return render_template('index.html',out_logs=out_logs,in_logs=in_logs)
    if request.method == 'GET':
        return render_template('index.html')

#信息上链
@app.route('/post',methods=['POST'])
def post():
    if request.method == 'POST':
        consignor=request.form.get('consignor')
        consignee=request.form.get('consignee')
        memo=request.form.get('memo')
        signature=request.form.get('signature')
        message=request.form.get('message')
        if bch.validate_signature(consignor, signature, message):
            res = bch.add_a_block(consignor,consignee,memo)
            return res
        else:
            return jsonify({"error":"err"})

@app.route('/blocks/last',methods=['GET'])
def get_last_block():
    return jsonify(bch.json(bch.get_block_last()))

@app.route('/blocks/<int:index>',methods=['GET'])
def get_block(index):
    return jsonify(bch.json(bch.get_blocks_with(index)))

@app.route('/blocks/<int:from_index>/<int:to_index>',methods=['GET'])
def get_block_from_to(from_index,to_index):
    blocks=[]
    if(len(blockchain)>from_index and len(blockchain)>to_index and to_index>=from_index):
        for i in range(from_index,to_index+1):
            block=blockchain[i]
            blocks.append(block)
        return jsonify(blocks)
    else:
        return jsonify({"error":"noindex"})

#验证
@app.route('/validate',methods=['GET'])
def blocks_validate():

    return jsonify(bch.validate(bch.get_blocks()))

@app.route('/blocks/all',methods=['GET'])
def get_all_block():
    return jsonify(bch.json(bch.get_blocks_all()))

#查看区块链高度
@app.route('/blocks/height',methods=['GET'])
def get_block_height():
    return jsonify(bch.get_height())

#查看节点
@app.route('/nodes',methods=['GET'])
def get_get_nodes():
    return jsonify(nodes)

#添加节点
@app.route('/nodes/add/<string:ip>/<int:port>',methods=['GET'])
def add_nodes(ip,port):
    node = {"ip":ip,"port":port}
    #确保不重复添加
    if node not in nodes:
        nodes.append(node)
    return jsonify(nodes)

#同步区块
@app.route('/blocks/sync',methods=['GET'])
def blocks_sync():
    json=[]
    for node in nodes:
        ip = node["ip"]
        port = node["port"]
        url_height = "http://{0}:{1}/blocks/height".format(ip,port)
        url_all = "http://{0}:{1}/blocks/all".format(ip,port)
        #尝试去同步
        try:
            #尝试获得对方高度
            r_height = requests.get(url_height)
            height = int(r_height.json())
            self_index = get_height()


            #如果对方的比自己的大
            if height > self_index:
                r_blocks_all = requests.get(url_all)
                blocks = r_blocks_all.json()
                #对对方的区块进行验证
                is_validate = validate(blocks)
                #把对方的blockchain赋值自己的blokchain
                if (is_validate):
                    blockchain.clear()
                    for block in blocks:
                        blockchain.append(block)
                    return jsonify("synced")
                else:
                    return jsonify("not validate")
            else:
                #不同步
                return jsonify("no synced")

        except:
            return jsonify("error")
    return jsonify("no nodes")

if __name__ == '__main__':
    bch.make_a_genesis_block()
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=8080, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    app.run(debug=True,host='0.0.0.0',port=port)
