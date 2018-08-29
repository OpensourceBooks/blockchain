### 区块链浏览器


我们需要有一个接口，可以获得某个地址的全部信息。



生成私钥匙和公钥

```
python3 generate.py
```

测试一下，指定ip和端口，发送一条测试上链的数据。

```
python3 test.py -host localhost -port 3333
```


向某个节点上链

```
python3 client.py -host localhost -port 3333 -fa Z/qsNWOAAWULpqvtM/OMHmJE+6PG0oPUsOMGk2ySYgrUB5noaZsD6b0NbbPgslr1cdninkqYKcJ+sx74/Mhn2A== -ta 8v0+I3q+o6bChXOC37NWj4zd3NI6Tw8hb7LCTnV3wKy4gS1FuQwcIN+f8NCpY99TZkGkOP+GnmVwZ3a3zTeWRA== -memo hello -pk 196f72bf05e307458a0691ca73a2981d859e499ef9fc264183feddde5bd47217
```

然后在首页查询即可
