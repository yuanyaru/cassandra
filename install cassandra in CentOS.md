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

* 启动时无法加载某个类:

![image](https://github.com/yuanyaru/cassandra/blob/master/images/cannot-load-class.png)

原因：环境变量版本和实际版本不一致
解决：改了环境变量，还是报这个错，关机重启就可以了

如果没有报什么奇奇怪怪的 ERROR 然后看到 Node /x.x.x.x state jump to NORMAL，这样cassandra就算安装完成了

![image](https://github.com/yuanyaru/cassandra/blob/master/images/start-success.png)

也可以在在bin目录下使用 ./nodetool status 查看集群信息确认一下

![image](https://github.com/yuanyaru/cassandra/blob/master/images/check.png)

#### 操作cassandra数据库，bin目录下
* ./cqlsh 进入数据库
* 退出 cqlsh 直接 Ctrl+d
* 终止 pkill -u `id -un` -f cassandra

### 注意
配置Cassandra，打开并编辑Cassandra.yaml文件，修改start_rpc: false -》 start_rpc: true
这样别的应用才能连到它。
