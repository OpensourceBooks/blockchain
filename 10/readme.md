### hash上链


本示例和第8个没什么区别，区别仅仅是本示例是对内容的hash上链。不论你传什么内容，区块链里只保存hash。

向某个节点上链

```
python3 client.py -host localhost -port 3000 -fa Z/qsNWOAAWULpqvtM/OMHmJE+6PG0oPUsOMGk2ySYgrUB5noaZsD6b0NbbPgslr1cdninkqYKcJ+sx74/Mhn2A== -ta 8v0+I3q+o6bChXOC37NWj4zd3NI6Tw8hb7LCTnV3wKy4gS1FuQwcIN+f8NCpY99TZkGkOP+GnmVwZ3a3zTeWRA== -memo "你好啊" -pk 196f72bf05e307458a0691ca73a2981d859e499ef9fc264183feddde5bd47217
```

返回：

```
{
  "hash": "7d278864ae6f407907c2b2c50275b0ceecd86565ed5871287f18db2a",
  "index": 2
}
```

然后在首页查询即可。
