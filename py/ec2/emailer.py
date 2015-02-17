#!/usr/bin/python
import time
import sys  
import smtplib 
from config import * 
#sys.path.insert(0, '/usr/lib/python2.7/bridge/') 
                                                
#from bridgeclient import BridgeClient as bridgeclient
                                                     
TO = GTO
GMAIL_USER = GUSER
GMAIL_PASS = GPASS
SUBJECT = 'The Beehive Temp has Changed'
TEXT = 'The Beehive Temp is: '
#value = bridgeclient()                              
                                                     
#function to send email 
def send_email(a):
	print("Sending Email")
	smtpserver = smtplib.SMTP('smtp.gmail.com:587')
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo
	smtpserver.login(GMAIL_USER, GMAIL_PASS)
	header = 'To:' + TO + '\n' + 'From: ' + GMAIL_USER
	header = header + '\n' + 'Subject:' + SUBJECT + '\n'
	msg = header + '\n' + TEXT + a +'\n\n'
	smtpserver.sendmail(GMAIL_USER, TO, msg)
	smtpserver.close()


