# !/usr/bin/env python
# -*- coding:utf-8 -*-
from status_check import ping, http_request
from status_check import XmppCheck
import json

JSON_PATH = './../secret_data.json'

def get_json_property():
 f = open(JSON_PATH, 'rb')
 return json.load(f) 
  
def main():
  json = get_json_property() 
  ping_status = ping(json['host']) 
  http_status = http_request(json['http_url'], json['http_uid'], json['http_pw']) 
  xmpp = XmppCheck(json['jid'], json['sox_pw'])
  xmpp_status = xmpp.xmpp_ping() 
  print ping_status, http_status, xmpp_status

if __name__ == '__main__':
  main() 
