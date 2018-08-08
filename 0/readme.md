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
[{
	"data": "this is the genesis block",
	"previous_hash": 0,
	"hash": "bb8d6f67262cdda0872593280a5b0642a07a1196bbcc3042379811cf25b8c9d1"
}, {
	"data": "this is block 1",
	"previous_hash": "bb8d6f67262cdda0872593280a5b0642a07a1196bbcc3042379811cf25b8c9d1",
	"hash": "eef23e3fd8de411b5138dfc7c936f343fcb11cfce11757e6118b172a192307d5"
}, {
	"data": "this is block 2",
	"previous_hash": "eef23e3fd8de411b5138dfc7c936f343fcb11cfce11757e6118b172a192307d5",
	"hash": "802631e0a0a6efcace29b7d826b64b9bc59a29ec4b220afd562f1ccd66641961"
}, {
	"data": "this is block 3",
	"previous_hash": "802631e0a0a6efcace29b7d826b64b9bc59a29ec4b220afd562f1ccd66641961",
	"hash": "ea4991a6b820214c68527d752b409d8a7a6e9cbd837373d737903e0f4d988d80"
}]
```

解释一下，为什么叫做区块链，这个图，大家可以很直观地看到：

![blockchain](blockchain.svg)

所谓区块链，不可篡改就在于，每个区块的hash值，都会被下一个区块引用和验证。如果某个区块的内容被人为更改了，那么该区块的hash值一定会变。而该区块的下一个区块引用了之前的hash值，现在值对不上了，因此区块就会出现错误。

这一特性，就是不可篡改的原理。

如下图所示，假设把block_1的内容给篡改了，那么block_1的hash就变化了。结果导致block_2的previous_hash和block_1的hash对不上，因此这个区块链就断裂了。

![blockchain](blockchain_err.svg)
