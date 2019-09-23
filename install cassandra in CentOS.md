#### 安装 java
Cassandra 是运行于 java 环境之上，所以 JRE 是必须要安装的，安装步骤见：
[https://github.com/yuanyaru/cassandra/blob/master/install%20java%20and%20run%20a%20java%20code%20in%20linux.txt](https://github.com/yuanyaru/cassandra/blob/master/install%20java%20and%20run%20a%20java%20code%20in%20linux.txt)

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
* 终止 

#### 集群环境搭建
两个节点：
节点1：192.168.100.64（seed）
节点2：192.168.100.63
1. 配置节点1
* 配置Cassandra，打开并编辑Cassandra.yaml文件
``` bash
seed_provider:
    - class_name: org.apache.cassandra.locator.SimpleSeedProvider
      parameters:
          - seeds: "192.168.100.64"  # 改为你的对外访问的ip
listen_address: 192.168.100.64  # 改为你的对外访问的ip
start_rpc: true  # 这样别的应用才能连到它
rpc_address: 0.0.0.0  # 局域网内别的机器连接
broadcast_rpc_address: 192.168.100.64  # 改为你的对外访问的ip
```
* 启动节点1
2. 配置节点2
* 与节点1非常类似，要改动配置里面的seeds那一项的ip为节点1的ip
* 启动节点2

![image](https://github.com/yuanyaru/cassandra/blob/master/images/2start.png)

![image](https://github.com/yuanyaru/cassandra/blob/master/images/2check.png)