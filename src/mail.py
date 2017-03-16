# !/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.MIMEText import MIMEText
from email.Utils import formatdate

message = [
            "HOST PING ERROR OCCURED: HOST PING NOT RETURNED"
            "HTTP ERROR OCCURED: STATUS NOT 200",
            "XMPP ERROR OCCURED: PING NOT RETURENED",
          ]

#TODO: cannot login to vinci by smtp_ssl
#argument:; 0:Host ping, 1:HTTP Request Status, 2:XMPP ping
def send_mail(from_addr, to_addr, message_num):
  msg = MIMEText(message[message_num]) 
  msg['Subject'] = "Smartcity: Error Notification"
  msg['From'] = from_addr
  msg['To'] = to_addr
  msg['Date'] = formatdate() 
  
  try:
    s = smtplib.SMTP_SSL('vinci.ht.sfc.keio.ac.jp', 465) 
    s.connect() 
    s.login('takamasa', 'tkms13??') 
    print('yes') 
    s.sendmail(from_addr, [to_addr], msg.as_string()) 
    s.close() 
  except smtplib.SMTPSenderRefused, error:
    print(error) 
    print'yes'

if __name__ == '__main__':
  send_mail(FROM_ADDR, TO_ADDR, 1) 
