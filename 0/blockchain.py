#!/usr/bin/python
# -*- coding:utf-8 -*-
import hashlib as hasher
import json
blockchain = []


def hash(data,previous_hash):
    sha = hasher.sha256()
    sha.update("{0}{1}".format(data,previous_hash).encode("utf8"))
    return sha.hexdigest()

def make_a_block(data,previous_hash):
    block={}
    block["data"]=data
    block["previous_hash"]=previous_hash
    block["hash"]=hash(data,previous_hash)
    return block

def add_a_block(data):

    last_block = blockchain[len(blockchain)-1]
    previous_hash=last_block["hash"]
    blockchain.append(make_a_block(data,previous_hash))


def make_a_genesis_block():
    data="this is the genesis block"
    previous_hash=0

    blockchain.append(make_a_block(data,previous_hash))


if __name__ == '__main__':
    make_a_genesis_block()
    add_a_block("this is block 1")
    add_a_block("this is block 2")
    add_a_block("this is block 3")
    print (json.dumps(blockchain))
