### 增加了节点同步时验证的区块链

### 关键代码

```
#验证区块链
def validate(blocks):
    bool = True
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
```

### 用法：

分别启动2个节点：

```
python3 blockchain -p 8001
```

```
python3 blockchain -p 8002
```

浏览器打开 http://localhost:8001/nodes/add/localhost/8002

返回数据说明8002节点添加成功

```json
[
  {
    "ip": "localhost",
    "port": 8002
  }
]
```

在浏览器打开 http://localhost:8002/say/tom

这是在8002节点增加了一个区块。

在浏览器中打开 http://localhost:8001/blocks/all

可以看到8001节点只有一个跟块，因为没有同步。

```json
[
  {
    "data": "Genesis Block",
    "hash": "0e7a7f285f4c1ef2856c7b24ce7b11de15cddff7e7c2a733a16aa8c7f78085ae",
    "index": 0,
    "previous_hash": 0,
    "timestamp": 1533901217798
  }
]
```

然后我们在8001节点上同步：http://localhost:8001/blocks/sync

显示：

```json
"synced"
```

说明同步节点并且验证成功。

接下来查看所有的节点：http://localhost:8001/blocks/all

```json
[
  {
    "data": "Genesis Block",
    "hash": "d476a30fcfefa496c3f01a345b3b6d2a8234390da98cfc3c0899eec8037d437b",
    "index": 0,
    "previous_hash": 0,
    "timestamp": 1533901225899
  },
  {
    "data": "tom",
    "hash": "f3fbe9b7b0e74c47f1e2452b422f50d80dca8f05b7912c98843a2c69a4d48433",
    "index": 1,
    "previous_hash": "d476a30fcfefa496c3f01a345b3b6d2a8234390da98cfc3c0899eec8037d437b",
    "timestamp": 1533901358960
  }
]
```

说明8001的区块链已经验证了8002的区块链，并且实现了节点同步。
