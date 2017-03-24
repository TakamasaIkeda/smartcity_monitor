#!/usr/bin/env python
# -*- coding:utf-8 -*-

def edit_web_status(status):
  f = open('../public_html/data.json', 'wb') 
  if(status == 0):
    f.write('[0]') 
  else:
    f.write('[1]') 
  f.close() 
