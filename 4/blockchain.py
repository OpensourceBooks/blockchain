#!/usr/bin/python
# -*- coding:utf-8 -*-
import hashlib as hasher
from time import time
import json
from flask import Flask, jsonify,render_template
from argparse import ArgumentParser
blockchain = []
nodes=[]

def add_node(node):
    nodes.append(node)

def hash(index,data,timestamp,previous_hash):
    sha = hasher.sha256()
    sha.update("{0}{1}{2}{3}".format(index,data,timestamp,previous_hash).encode("utf8"))
    return sha.hexdigest()

def make_a_block(index,timestamp,data,previous_hash):
    block={}
    block["index"]=index
    block["timestamp"]=timestamp
    block["data"]=data
    block["previous_hash"]=previous_hash
    block["hash"]=hash(index,data,timestamp,previous_hash)
    return block

def add_a_block(data):

    last_block = blockchain[len(blockchain)-1]

    index=last_block["index"]+1
    timestamp=int(round(time() * 1000))
    previous_hash=last_block["hash"]


    blockchain.append(make_a_block(index,timestamp,data,previous_hash))


def make_a_genesis_block():
    index=0
    timestamp=int(round(time() * 1000))
    data="Genesis Block"
    previous_hash=0

    blockchain.append(make_a_block(index,timestamp,data,previous_hash))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/say/<string:msg>',methods=['GET'])
def add_block(msg):
    add_a_block(msg)
    return jsonify(blockchain)

@app.route('/blocks/last',methods=['GET'])
def get_last_block():
    last_block = blockchain[len(blockchain)-1]
    return jsonify(last_block)

@app.route('/blocks/<int:index>',methods=['GET'])
def get_block(index):
    if(len(blockchain)>=index):
        block = blockchain[index]
        return jsonify(block)
    else:
        return jsonify({"error":"noindex"})

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

@app.route('/blocks/all',methods=['GET'])
def get_all_block():
    return jsonify(blockchain)

if __name__ == '__main__':
    make_a_genesis_block()
    add_a_block("hello")
    add_a_block("hi~")
    add_a_block("~")


    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=8080, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    app.run(debug=True,host='0.0.0.0',port=port)
