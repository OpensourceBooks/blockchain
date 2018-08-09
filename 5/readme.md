### 增加了节点同步的区块链

增加一个list，保存节点。

```
nodes=[]
```

为了方便同步数据，我们要增加一个接口，可以获知区块链高度。

http://localhost:8080/blocks/height

这样，即可得到区块链的高度。当目标节点的区块链高度大于本地区块链高度时，才去同步。


查看节点

http://localhost:8080/nodes

添加节点

http://localhost:8080/nodes/add/localhost/9000

得到：

```json
[
  {
    "ip": "localhost",
    "port": 9000
  }
]
```

在8080的节点中加入另一个节点8081

http://localhost:8080/nodes/add/localhost/8081

查看8080节点

http://localhost:8080/nodes

在8081的区块链中加一条信息

http://localhost:8081/say/jerry2

在8080节点中同步

http://localhost:8080/blocks/sync

查看节点

如果没同步：

```
"no synced"
```

如果同步了：

```
"synced"
```


http://localhost:8080/blocks/all
