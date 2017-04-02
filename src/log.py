#!/usr/bin/env python
# -*- coding:utf-8 -*-
import MySQLdb
import time

#protocol:"ICMP", "HTTP", "SOX", status: true/false/ dst:string
def db_push(protocol, dst, status_num): 
  status = (status_num != 0) 
  
  connector = MySQLdb.connect(host='localhost', db="SmartcityLog", user="takamasa", charset="utf8")   
  cursor = connector.cursor() 
  
  timestamp = time.strftime('%Y-%m-%d %H:%M:%S') 
  sql = "insert into sox_ping_log(created, protocol, destination, status) values (%s, %s, %s, %s);"
  args = [timestamp, protocol, dst, status] 
  cursor.execute(sql, args) 
  connector.commit() 

  cursor.close()
  connector.close() 
