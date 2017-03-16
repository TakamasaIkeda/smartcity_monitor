#!/usr/bin/env python
#-*- coding: utf-8 -*-
import subprocess
import requests
import sleekxmpp
import sys

#this file is for checking status of server. Ping, HTTP status, xmpp ping
#pingコマンドの出力メッセージ
RETURN_PACKET = 'icmp_seq=0'
ERRORS = {
            "timeout" : 'Request Timed Out',
            "unknown_host" : 'Unknown Host',
            "host_unreachable" : 'Destination Host Unreachable',
            "ttl_expired" : 'TTL Expired Transit',
            "loss_packet" : '0 received'
          }

def ping(host): 
    #pingコマンドを投げ, 標準出力とエラー出力をパイプ
    ping = subprocess.Popen(
        ["ping", "-c", "1", host],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    ) 

    #pingコマンドでpipeで返ってきた値とやりとりすることを定義
    out, error = ping.communicate() 
    message = ''
    isError = any([ err_msg in out for err_msg in ERRORS.values()])  


    #場合によってエラーメッセージの出力
    if isError == False:
        print("[ping OK]:" + host) 
        return 0
    elif isError == True:
        print("[ping NG]:" + host + "->" + message) 
        return 1
    else:
        print("[Err]:" + error) 
        return 1


def http_request(url, uid, password):
    request = requests.get(url, auth=(uid, password)) 
    status = request.status_code

    if status == 200:
        print("[HTTP OK]:" + url) 
        return 0
    else:
        print("[Err NG:]" + url) 
        return 1

#xmpp checking
class XmppCheck(sleekxmpp.ClientXMPP): 
  def __init__(self, jid, pw):
    super(XmppCheck, self).__init__(jid,pw)  
    self.register_plugin('xep_0030')  
    self.register_plugin('xep_0004')  
    self.register_plugin('xep_0060')  
    self.register_plugin('xep_0199') #xmpp_ping's registration 
    self.add_event_handler("session_start", self.start, threaded=False) 

  def start(self, event): 
    #get connection
    self.send_presence()    
    self.get_roster() 

    print("send ping") 
    result = self['xep_0199'].send_ping(self.jid, block=True)

    #When ping result was False or None
    if result is None or result is False:
     self.disconnect() 
     print("Ping Not Good") 
     return 1
    else:
     self.disconnect() 
     print("Ping Good") 
     return 0

  def xmpp_ping(self): 
    if self.connect():
      self.process(block=True) 
    else:
      print("unable to connect")  
