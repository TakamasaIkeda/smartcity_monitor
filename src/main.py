# !/usr/bin/env python
# -*- coding:utf-8 -*-
from status_check import ping, http_request
from status_check import XmppPing
from log import db_push
import json
from mail import send_mail
from edit_web_status import EditWebStatus

JSON_PATH = '/var/smartcity_monitor/secret_data.json'

def get_json_property():
 f = open(JSON_PATH, 'rb')
 return json.load(f) 

def main():
  json = get_json_property() 
  ews = EditWebStatus()
  ping_status, http_status, xmpp_status = int(), int(), int()

  #ICMP Ping
  ping_status = ping(json['host']) 
  db_push('ICMP',json['host'], ping_status) 
  if(ping_status != 0):
    send_mail(json['from_addr'], json['to_addr'], 0) 
  ews.push_dict('ICMP', ping_status)

  #HTTP Request Status Code
  http_status = http_request(json['http_url'], json['http_uid'], json['http_pw']) 
  db_push('HTTP', json['http_url'], http_status) 
  if(http_status != 0):
    send_mail(json['from_addr'], json['to_addr'], 1) 
  ews.push_dict('HTTP', http_status)

  #XMPP Ping
  xmpp = XmppPing(json['jid'], json['sox_pw'], json['jid'])
  if xmpp.connect():
    xmpp.process(block=True) 
    xmpp_status = xmpp.get_status()
  else:
    print("It cannnot connect to sox server for some reason")

  db_push('SOX', json['jid'], xmpp_status) 
  if(xmpp_status != 0):
    send_mail(json['from_addr'], json['to_addr'], 2) 
  ews.push_dict('XMPP', xmpp_status)
  
  #throw {protocol:status} dict to json file
  ews.edit_web_status() 

if __name__ == '__main__':
  main() 
