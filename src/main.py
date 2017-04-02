# !/usr/bin/env python
# -*- coding:utf-8 -*-
from status_check import ping, http_request
from status_check import XmppCheck
from log import db_push
import json
from mail import send_mail
from edit_web_status import EditWebStatus

JSON_PATH = './../secret_data.json'

def get_json_property():
 f = open(JSON_PATH, 'rb')
 return json.load(f) 

def main():
  json = get_json_property() 
  ews = EditWebStatus()

  #ICMP Ping
  ping_status = ping(json['host']) 
  db_push('ICMP',json['host'], ping_status) 
  send_mail(json['from_addr'], json['to_addr'], 0) 
  ews.push_dict('ICMP', ping_status)

  #HTTP Request Status Code
  http_status = http_request(json['http_url'], json['http_uid'], json['http_pw']) 
  db_push('HTTP', json['http_url'], http_status) 
  send_mail(json['from_addr'], json['to_addr'], 1) 
  ews.push_dict('HTTP', http_status)

  #XMPP Ping
  xmpp = XmppCheck(json['jid'], json['sox_pw'])
  xmpp_status = xmpp.xmpp_ping() 
  db_push('SOX', json['jid'], xmpp_status) 
  send_mail(json['from_addr'], json['to_addr'], 2) 
  ews.push_dict('SOX', xmpp_status)
  
  #throw {protocol:status} dict to json file
  ews.edit_web_status() 

if __name__ == '__main__':
  main() 
