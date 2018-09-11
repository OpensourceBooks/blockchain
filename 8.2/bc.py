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

class Block:
    def __init__(self,index,timestamp,consignor,consignee,memo,previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.consignor = consignor
        self.consignee = consignee
        self.memo = memo
        self.previous_hash = previous_hash

class BlockchainHelper:
    def __init__(self):
        self.blockchain = []
        self.nodes = []

    def get_blocks(self):
        return self.blockchain

    #验证区块链
    def validate(self):
        bool = True
        blocks = self.blockchain
        #上一个区块
        previous_index = 0
        previous_hash = 0
        for block in blocks:
            index = block["index"]
            hash = block["hash"]
            if (index > 0):
                #如果index是衔接的
                if (previous_index == index-1):
                    pass
                else:
                    bool = False
                #如果上一个区块的当前hash和当前区块的上一个hash值能对上
                if (previous_hash == block["previous_hash"]):
                    pass
                else:
                    bool = False

                if bool:
                    #把当前的变为上一个
                    previous_index = index
                    previous_hash = hash
            if (index == 0):
                previous_index = index
                previous_hash = hash
                pass
        return bool

    #添加节点
    def add_node(self,node):
        self.nodes.append(node)

    #返回自身区块链高度
    def get_height(self):
        last_block = self.blockchain[len(blockchain)-1]
        last_block_index = last_block["index"]
        return last_block_index


    def hash(self,index,consignor,consignee,memo,timestamp,previous_hash):
        sha = hasher.sha256()
        sha.update("{0}{1}{2}{3}{4}{5}".format(index,consignor,consignee,memo,timestamp,previous_hash).encode("utf8"))
        return sha.hexdigest()

    def add_a_block(self,consignor,consignee,memo):
        last_block = self.blockchain[len(blockchain)-1]
        index=last_block["index"]+1
        timestamp=int(round(time() * 1000))
        previous_hash=last_block["hash"]
        self.blockchain.append(Block(index,timestamp,consignor,consignee,memo,previous_hash))

    def make_a_genesis_block(self):
        index=0
        timestamp=int(round(time() * 1000))
        consignor = 0
        consignee = 0
        memo="Genesis Block"
        previous_hash=0
        self.blockchain.append(Block(index,timestamp,consignor,consignee,memo,previous_hash))

    def validate_signature(self,public_key, signature, message):
        public_key = (base64.b64decode(public_key)).hex()
        signature = base64.b64decode(signature)
        try:
            vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(public_key), curve=ecdsa.SECP256k1)
            return vk.verify(signature, message.encode())
        except:
            return False