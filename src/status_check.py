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


def http_request(url, uid=None, password=None):
    status = 0
    try:
      request = requests.get(url, auth=(uid, password)) 
      status = request.status_code
    except:
      print 'BAD Request: Maybe URL is wrong?'

    if status == 200:
        print("[HTTP OK]:" + url) 
        return 0
    else:
        print("[Err NG:]" + url) 
        return 1

#xmpp checking

class XmppPing(sleekxmpp.ClientXMPP): 
  def __init__(self, jid, password, pingjid): 
     self.flag = int()
     sleekxmpp.ClientXMPP.__init__(self, jid, password) 
     if pingjid is None:
     	pingjid = self.boundjid.bare
     self.pingjid = pingjid
     self.register_plugin('xep_0030') 
     self.register_plugin('xep_0004') 
     self.register_plugin('xep_0060') 
     self.register_plugin('xep_0199') 
     self.add_event_handler("session_start", self.start, threaded=True) 

  def start(self, event): 
     self.send_presence() 
     self.get_roster()

     try:
       rtt = self['xep_0199'].ping(self.pingjid, timeout=10) 
       print("[XMPP OK]: RTT: %s", rtt) 
       self.flag = 0
     except IqError as e:
       print("[XMPP Error]%s: %s", self.pingjid, e.iq['error']['connection']) 
       self.flag = 1
     finally:
       self.disconnect()

  def get_status(self): 
      return self.flag
