# /usr/bin/python
# -*- encoding:utf-8 -*-

# pip2 install cassandra-driver
# 引入 Cluster 模块
from cassandra.cluster import Cluster


# 新建keyspace和table
def main():
    # 默认本机数据库集群(IP127.0.0.1)
    cluster = Cluster(["192.168.100.64"])
    # 连接并创建一个会话
    session = cluster.connect()
    # 创建KeySpace；使用第一个副本放置策略，即简单策略；选择复制因子为3个副本。
    session.execute("drop keyspace test;")
    session.execute("CREATE KEYSPACE test WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '3'};")
    # 选择keyspace
    session.execute('use test;')
    # 创建table
    session.execute("create table test.user(name text primary key, age int, email varchar);")
    # session.execute("drop table test.user")
    session.execute("insert into test.user (name, age, email) values (%s, %s, %s);", ['aaa', 21, 'aaa@21.com'])
    session.execute("insert into test.user (name, age, email) values (%s, %s, %s);", ['bbb', 22, 'bbb@22.com'])
    session.execute("insert into test.user (name, age, email) values (%s, %s, %s);", ['ccc', 23, 'ccc@23.com'])

    # 查询keyspaces/tables/columns状态
    print "--------------------------- 查询 keyspaces --------------------------------"
    print cluster.metadata.keyspaces
    print "--------------------------- 查询 test 中所有 table ------------------------"
    print cluster.metadata.keyspaces['test'].tables
    print "--------------------------- 查询 user table -------------------------------"
    print cluster.metadata.keyspaces['test'].tables['user']
    print "--------------------------- 查询 user columns -----------------------------"
    print cluster.metadata.keyspaces['test'].tables['user'].columns
    print "--------------------------- 查询 column age -------------------------------"
    print cluster.metadata.keyspaces['test'].tables['user'].columns['age']
    print "--------------------------- 查询 user rows --------------------------------"
    rows = session.execute("select * from test.user;")
    for row in rows:
        print row

    use_keyspace()

    # 关闭连接
    cluster.shutdown()
    # 查看是否关闭连接
    print(cluster.is_shutdown)


def use_keyspace():
    cluster = Cluster(["192.168.100.64"])
    session = cluster.connect("test")
    session.execute("create table student(id varchar primary key, name varchar, city varchar);")
    session.execute("insert into student (id, name, city) values (%s, %s, %s);", ["2019091901", "张三", "BeiJing"])
    session.execute("insert into student (id, name, city) values (%s, %s, %s);", ["2019091902", "李四", "ShangHai"])
    session.execute("insert into student (id, name, city) values (%s, %s, %s);", ["2019091903", "王五", "XiAn"])
    result = session.execute("select * from student where name = '张三' ALLOW FILTERING;")
    print result

    session.execute("update student set city = '北京' where id = '2019091901';")
    result = session.execute("select city from student where id = '2019091901' ALLOW FILTERING")
    print result

    session.execute("delete from student where id = '2019091901'")
    result = session.execute("select * from student")
    for i in result:
        print i


if __name__ == '__main__':
    main()
