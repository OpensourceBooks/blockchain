# 使用签名提交memo上链。

这是个无币区块链的应用，没有UTXO。因此也没有wallet的概念。

客户端可以生成地址，然后使用私钥签名，签名的内容经过服务端检查，可以上链。


### 生成一个地址 和私钥

```
python3 client.py -a n
```

返回的信息类似：

```
address:Z/qsNWOAAWULpqvtM/OMHmJE+6PG0oPUsOMGk2ySYgrUB5noaZsD6b0NbbPgslr1cdninkqYKcJ+sx74/Mhn2A==

private_key:196f72bf05e307458a0691ca73a2981d859e499ef9fc264183feddde5bd47217
```
### 使用签名发消息上链

```
python3 client.py -a s -f Z/qsNWOAAWULpqvtM/OMHmJE+6PG0oPUsOMGk2ySYgrUB5noaZsD6b0NbbPgslr1cdninkqYKcJ+sx74/Mhn2A== -t Z/qsNWOAAWULpqvtM/OMHmJE+6PG0oPUsOMGk2ySYgrUB5noaZsD6b0NbbPgslr1cdninkqYKcJ+sx74/Mhn2A== -m hello -p 196f72bf05e307458a0691ca73a2981d859e499ef9fc264183feddde5bd47217
```

收到信息类似如下：


```
[
  {
    "data": "Genesis Block",
    "hash": "65661446c4106d81e864fe4dca5fea70364023f881330017489207652d53e3fc",
    "index": 0,
    "previous_hash": 0,
    "timestamp": 1534499678402
  },
  {
    "data": {
      "from": "gwCSgiOvn0ndfftgsOIYNjPjEcT24BrMEWH7lZ5qCmFlyaUnR/frznDDFdfNSWJLGta14c+0gDUc7RS4kkf1aQ==",
      "memo": "hello",
      "to": "gwCSgiOvn0ndfftgsOIYNjPjEcT24BrMEWH7lZ5qCmFlyaUnR/frznDDFdfNSWJLGta14c+0gDUc7RS4kkf1aQ=="
    },
    "hash": "89f9e9c445690624dceca3ef8f3f43b65f6a6558ffd25c13bc952e9d7624838a",
    "index": 1,
    "previous_hash": "65661446c4106d81e864fe4dca5fea70364023f881330017489207652d53e3fc",
    "timestamp": 1534499684262
  },
  {
    "data": {
      "from": "Z/qsNWOAAWULpqvtM/OMHmJE+6PG0oPUsOMGk2ySYgrUB5noaZsD6b0NbbPgslr1cdninkqYKcJ+sx74/Mhn2A==",
      "memo": "hello",
      "to": "Z/qsNWOAAWULpqvtM/OMHmJE+6PG0oPUsOMGk2ySYgrUB5noaZsD6b0NbbPgslr1cdninkqYKcJ+sx74/Mhn2A=="
    },
    "hash": "144d2a6f6724b78f5ccd1c81e01fae8c6a7b9ec474a3131f94331203e9daa9a7",
    "index": 2,
    "previous_hash": "89f9e9c445690624dceca3ef8f3f43b65f6a6558ffd25c13bc952e9d7624838a",
    "timestamp": 1534501157600
  }
]
```
