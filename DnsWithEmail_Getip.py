# -*- coding: cp936 -*-
import smtplib  
import socket
import email.mime.text
import sys
import time
import share
import poplib

class getoutofloop(Exception): pass

if __name__ == '__main__':
    [mail_username,mail_password]=share.SetIDFromFile("config.ini")

    emailServer = poplib.POP3('pop3.seu.edu.cn')    
    print "Connect the server success!"
    emailServer.user(mail_username)  
    emailServer.pass_(mail_password)  

    emailMsgNum, emailSize = emailServer.stat()  
      
    try:
        for i in range(emailMsgNum):
            for piece in emailServer.retr(i+1)[1]:  
                if piece.startswith('Subject: IP:'):
                    print "IP:"+piece.split('Subject: IP:')[1]
                    raise getoutofloop()
    except getoutofloop:
        pass
    emailServer.quit() 
