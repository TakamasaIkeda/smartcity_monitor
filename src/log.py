#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logging

def status_logging():
  log_format = '%(asctime)s- %(name)s - %(levelname)s - %(message)s'    
  log_path = './../var/log/status.log'
  logging.basicConfig(format=log_format, filename=log_path, level=logging.ERROR) 
  logging.error('HTTP') 

if __name__ == '__main__':  
  status_logging() 
