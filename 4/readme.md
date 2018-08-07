### 增加了节点同步的区块链

增加一个list，保存节点。

```
nodes=[]
```

多个节点，因此要可以选择端口的参数

增加一个引入：
```
from argparse import ArgumentParser
```

启动代码如下：
```
parser = ArgumentParser()
parser.add_argument('-p', '--port', default=8080, type=int, help='port to listen on')
args = parser.parse_args()
port = args.port
app.run(debug=True,host='0.0.0.0',port=port)
```

添加一个能获得最新区块的api

添加一个获得全部区块的api

添加一个从xx到xx的区块的api

我们启动区块链

```
python blockchain.py -p 9090
```
访问全部区块：

http://localhost:9090/blocks/all


访问最新的区块：

http://localhost:9090/blocks/last

```json
{
  "data": "~",
  "hash": "5b9d3b614c7e28a330a7ae6517d2132709725e9812dd8b80f7f8e702fd1bc4c3",
  "index": 3,
  "previous_hash": "2624e776d1adc8c2b99e42458f69957ab8f66477dff393a1c8f8b6b3da417672",
  "timestamp": 1533632972579
}
```

其中index就是区块链的高度


访问index从1～3的区块

http://localhost:9090/blocks/1/3

```json
[
  {
    "data": "hello",
    "hash": "bbea6b876254a17d03cf154821be34be2ba782500da2b9310baa9d2f08567181",
    "index": 1,
    "previous_hash": "d2c6ff3b8ab521d7837ac64873f7228d9f7e96ce727cec2a815d135545c65f44",
    "timestamp": 1533634461058
  },
  {
    "data": "hi~",
    "hash": "ad65bd6611bb84416766f231cfc87c86c885ad4f0a12bfa002c40119abd23b23",
    "index": 2,
    "previous_hash": "bbea6b876254a17d03cf154821be34be2ba782500da2b9310baa9d2f08567181",
    "timestamp": 1533634461058
  },
  {
    "data": "~",
    "hash": "b2bc5f8762252de051c06eccd2cadeda43a200f1e834e0033e056b341d0688d6",
    "index": 3,
    "previous_hash": "ad65bd6611bb84416766f231cfc87c86c885ad4f0a12bfa002c40119abd23b23",
    "timestamp": 1533634461058
  }
]
```

访问index为2的区块

http://localhost:9090/blocks/2

```json
{
  "data": "hi~",
  "hash": "ad65bd6611bb84416766f231cfc87c86c885ad4f0a12bfa002c40119abd23b23",
  "index": 2,
  "previous_hash": "bbea6b876254a17d03cf154821be34be2ba782500da2b9310baa9d2f08567181",
  "timestamp": 1533634461058
}
```
