import hashlib
word="测试一下"
hash=hashlib.sha224("{0}".format(word).encode('utf-8')).hexdigest()
print (hash)
