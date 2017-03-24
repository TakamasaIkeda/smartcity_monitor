#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logging
import os

err_msg = ['ICMP Error: Ping NOT Returned', 'HTTP ERROR: HTTP Status NOT 200', 'SOX ERROR: SOX ping NOT RETURNED']
def status_logging(msg_num):
  log_format = '%(asctime)s- %(name)s - %(levelname)s - %(message)s'    
  log_path = './../var/log/status.log'
  logging.basicConfig(format=log_format, filename=log_path, level=logging.ERROR) 
  logging.error(err_msg[msg_num]) 

def 

if __name__ == '__main__':  
  status_logging(1) 
