#### 安装 java
Cassandra 是运行于 java 环境之上，所以 JRE 是必须要安装的
参考：install java and run a java code in linux

如果没有安装jre, 启动 cassandra 会报错：
![image](https://github.com/yuanyaru/cassandra/blob/master/images/jre.jpg)

#### 下载 Cassandra
将/packages/apache-cassandra-3.11.3-bin.tar.gz 拷贝至/usr/local/bin/ 目录下

#### 解压
``` bash
$ tar zxvf apache-cassandra-3.11.3-bin.tar.gz
```

#### 启动
``` bash
/usr/local/bin/apache-cassandra-3.11.3/bin
./cassandra -f -R
```

* 启动直接 killed

![image](https://github.com/yuanyaru/cassandra/blob/master/images/killed.jpg)

原因：内存太小

![image](https://github.com/yuanyaru/cassandra/blob/master/images/memory-small.jpg)

* 扩大内存后，启动成功

![image](https://github.com/yuanyaru/cassandra/blob/master/images/memory-big.jpg)

