#!/usr/bin/env python
# -*- coding:utf-8 -*-
import logging
import os

def status_logging():
  log_format = '%(asctime)s- %(name)s - %(levelname)s - %(message)s'    
  log_path = './../var/log/status.log'
  logging.basicConfig(format=log_format, filename=log_path, level=logging.ERROR) 
  logging.error('HTTP') 

def edit_web_status(status):
  f = open('../public_html/data.json', 'wb') 
  if(status == 0):
    f.write('[0]') 
  else:
    f.write('[1]') 
  f.close() 

if __name__ == '__main__':  
  status_logging() 
  edit_web_status(0) 
