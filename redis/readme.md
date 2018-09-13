### install redis-server

```
sudo apt install redis-server
```

### install redis for python

```
pip3 install redis
```

### make a genesis block

```
python3 genesis.py
```

### show blockchain

```
python3 show_all_blockchain.py
```

### remove all data

```
python3 remove_all.py
```

### RESTful API

```
python3 blockchain.py -p3333
```

```
http://localhost:3333/api/blocks/all
```