#### 下载 Cassandra
将/packages/apache-cassandra-3.11.3-bin.tar.gz 拷贝至/usr/local/bin/ 目录下

#### 解压
``` bash
$ tar zxvf apache-cassandra-3.11.3-bin.tar.gz
```

3. 启动
``` bash
/usr/local/bin/apache-cassandra-3.11.3/bin
./cassandra -f -R //用root用户启动
```

启动直接 killed

原因：内存太小

扩大内存后，启动成功
