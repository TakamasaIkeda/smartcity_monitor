# !/usr/bin/env python
# -*- coding:utf-8 -*-
from status_check import ping, http_request
from status_check import XmppCheck
from log import db_push
import json
from mail import send_mail
from edit_web_status import edit_web_status 

JSON_PATH = './../secret_data.json'

def get_json_property():
 f = open(JSON_PATH, 'rb')
 return json.load(f) 

def main():
  web_flag = 0
  json = get_json_property() 

  ping_status = ping(json['host']) 
  db_push('ICMP',json['host'], ping_status) 
  send_mail(json['from_addr'], json['to_addr'], 0) 
  web_flag = ping_status

  http_status = http_request(json['http_url'], json['http_uid'], json['http_pw']) 
  db_push('HTTP', json['http_url'], http_status) 
  send_mail(json['from_addr'], json['to_addr'], 1) 
  web_flag = ping_status

  xmpp = XmppCheck(json['jid'], json['sox_pw'])
  xmpp_status = xmpp.xmpp_ping() 
  db_push('SOX', json['jid'], xmpp_status) 
  send_mail(json['from_addr'], json['to_addr'], 2) 
  web_flag = xmpp_status

  edit_web_status(web_flag) 

if __name__ == '__main__':
  main() 
