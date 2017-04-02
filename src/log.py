#!/usr/bin/env python
# -*- coding:utf-8 -*-
import MySQLdb
import time

def status_logging(msg_num):
  log_format = '%(asctime)s- %(name)s - %(levelname)s - %(message)s'    
  log_path = './../var/log/status.log'
  logging.basicConfig(format=log_format, filename=log_path, level=logging.ERROR) 
  logging.error(err_msg[msg_num]) 

#protocol:"ICMP", "HTTP", "SOX", status: true/false/ dst:string
def db_push(protocol, dst, status_num): 
  status = (status_num == 0) 
  
  connector = MySQLdb.connect(host='localhost', db="SmartcityLog", user="takamasa", charset="utf8")   
  cursor = connector.cursor() 
  
  timestamp = time.strftime('%Y-%m-%d %H:%M:%S') 
  sql = "insert into sox_ping_log(created, protocol, destination, status) values (%s, %s, %s, %s);"
  args = [timestamp, protocol, dst, status] 
  cursor.execute(sql, args) 
  connector.commit() 

  cursor.close()
  connector.close() 

if __name__ == "__main__":
  db_push("HTTP", "https://www.google.com", 1) 
