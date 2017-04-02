#!/usr/bin/env python
# -*- coding:utf-8 -*-

class EditWebStatus():
  list_status = []
  str_status = ""

  def __init__(self):
    pass
  
  @classmethod
  def edit_web_status(cls):
    for i in xrange(len(cls.list_status)):
	cls.str_status = cls.str_status + cls.list_status[i]
    cls.str_status = "{" + cls.str_status.replace("}{", "},{") + "}"
    f = open('/var/www/public_html/data.json', 'w+') 
    f.write(cls.str_status) 
    f.close() 
  
  #push {"protocol", status(int)} to cls.list_status
  @classmethod
  def push_dict(cls, protocol, status):
    each_protocol = "{\"%s\":%d}" % (protocol, status)
    cls.list_status.append(each_protocol)
    print cls.list_status

if __name__ == "__main__":
  ews = EditWebStatus()
  ews.push_dict('HTTP', 0)
  ews.push_dict('ICMP', 0)
  ews.push_dict('XMPP', 0)
  ews.edit_web_status()
