#!/usr/bin/python
# -*- coding:utf-8 -*-
import hashlib as hasher
import redis
from time import time
pool = redis.ConnectionPool(host='127.0.0.1', port=6379 ,decode_responses=True)  
r = redis.Redis(connection_pool=pool)

def hash(height,timestamp,data,from_address,to_address,previous_hash):
    sha = hasher.sha256()
    sha.update("{0}{1}{2}{3}{4}{5}".format(height,data,from_address,to_address,timestamp,previous_hash).encode("utf8"))
    return sha.hexdigest()

# 得到当前区块高度
if (r.get("block_height")):

    block_height = int(r.get("block_height"))

    # 新建区块：

    # 高度+1
    height = block_height + 1
    # 时间戳
    timestamp = int(round(time() * 1000))
    # 区块索引
    block_index = "block_{0}".format(height)
    # 内容
    data = "hello this is block No {0}".format(height)
    # 发送地址
    from_address = "0"
    # 接收地址
    to_address = "0"
    # 上一个hash
    last_block = r.hgetall("block_{0}".format(block_height))
    previous_hash = last_block["this_hash"]
    # 自身hash
    this_hash = hash(height,timestamp,data,from_address,to_address,previous_hash)


    # 更新区块高度
    r.set("block_height",height)

    # 添加区块的kv
    r.hset(block_index,"height",height)#高度(可以当作index)
    r.hset(block_index,"timestamp",timestamp)#时间戳
    r.hset(block_index,"data",data)#内容
    r.hset(block_index,"from_address",from_address)#发送者地址
    r.hset(block_index,"to_address",to_address)#接收者地址
    r.hset(block_index,"previous_hash",previous_hash)#上一个hash
    r.hset(block_index,"this_hash",this_hash)#hash