#!/usr/bin/python
# -*- coding:utf-8 -*-
import redis
import json
pool = redis.ConnectionPool(host='127.0.0.1', port=6379 ,decode_responses=True)  
r = redis.Redis(connection_pool=pool)



if (r.get("block_height")):
    block_height = int(r.get("block_height"))
    print ("block height:{0}".format(block_height))

    blockchain = []

    for i in range(0,block_height+1):
        block = r.hgetall("block_{0}".format(i))
        blockchain.append(block)

    #print (blockchain[0][b"this_hash"].decode('utf-8'))
    print (blockchain)
else:
    print ("None")    

