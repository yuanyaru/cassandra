#!/usr/bin/python

from cassandra.cluster import Cluster


cluster = Cluster(["192.168.100.62"])
session = cluster.connect()
session.execute("CREATE KEYSPACE test WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '3'};")
print(cluster.metadata.keyspaces)
