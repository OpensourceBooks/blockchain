### 最简单的区块链

最简单的区块链仅仅有区块链的结构：

1、data

内此处可以放内容

2、previous_hash

上一个区块的hash

3、hash

本区块的hash

有了这三个，就能形成最基本的区块链。

运行方法：

```
python blockchain.py
```

如果正常，你应该能得到类似如下的返回：

```json
[{"data": "Genesis Block", "previous_hash": 0, "hash": "8500b59bb5271135cd9bcbf0afd693028d76df3b9c7da58d412b13fc8a8f9394"}, {"data": "hello", "previous_hash": "8500b59bb5271135cd9bcbf0afd693028d76df3b9c7da58d412b13fc8a8f9394", "hash": "994c587fa5ec4506c973518784308953c60a994c3df5571fa182f3df08e35059"}, {"data": "hi~", "previous_hash": "994c587fa5ec4506c973518784308953c60a994c3df5571fa182f3df08e35059", "hash": "f329f07360b04770f828301a993cce520057c91e79f7c7c586b9fb825e45b2c0"}, {"data": "~", "previous_hash": "f329f07360b04770f828301a993cce520057c91e79f7c7c586b9fb825e45b2c0", "hash": "4f1780b69d3004de1f97f371631851a9587e4634e8e73ac9021f0bb35780e2eb"}]

```
