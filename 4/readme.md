### 增加了一些查询功能、可以选择端口的参数

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

我们启动区块链

```
python blockchain.py -p 9090
```
访问全部区块：

http://localhost:9090/blocks/all

```json
[
  {
    "data": "Genesis Block",
    "hash": "74eaf9085aa458f99c724583e4314b361bae60bff74e4cb82f89c9ecaa671406",
    "index": 0,
    "previous_hash": 0,
    "timestamp": 1533634910741
  },
  {
    "data": "hello",
    "hash": "41c28040287d26d66780f1175606fbf22d6a73c11355c64ae590b32d5e22d61b",
    "index": 1,
    "previous_hash": "74eaf9085aa458f99c724583e4314b361bae60bff74e4cb82f89c9ecaa671406",
    "timestamp": 1533634910741
  },
  {
    "data": "hi~",
    "hash": "45aff7916c3410f9f93ac2a9dbcc24af33caa9120890ce0f1cabe02a3514b106",
    "index": 2,
    "previous_hash": "41c28040287d26d66780f1175606fbf22d6a73c11355c64ae590b32d5e22d61b",
    "timestamp": 1533634910741
  },
  {
    "data": "~",
    "hash": "cd3d295b8c2c168830e24132f58073f2d39cee95fa6ae4d87a8be248fe8eaf3f",
    "index": 3,
    "previous_hash": "45aff7916c3410f9f93ac2a9dbcc24af33caa9120890ce0f1cabe02a3514b106",
    "timestamp": 1533634910741
  }
]
```

访问最新的区块：

http://localhost:9090/blocks/last

你能得到类似的结果：

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

你能得到类似的结果：

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

你能得到类似的结果：

```json
{
  "data": "hi~",
  "hash": "ad65bd6611bb84416766f231cfc87c86c885ad4f0a12bfa002c40119abd23b23",
  "index": 2,
  "previous_hash": "bbea6b876254a17d03cf154821be34be2ba782500da2b9310baa9d2f08567181",
  "timestamp": 1533634461058
}
```
