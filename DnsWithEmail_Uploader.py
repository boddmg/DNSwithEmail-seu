#!/usr/bin/python
import smtplib
import socket
import subprocess
import email.mime.text
import time
import share
import socket
import platform


def SendEmail(title,context):
    # get mail information
    [mail_username,mail_password]=share.SetIDFromFile("config.ini")
    from_addr = mail_username+'@seu.edu.cn'
    to_addrs=(from_addr)

    # HOST & PORT
    HOST = 'smtp.seu.edu.cn'
    PORT = 25

    # Create SMTP Object
    smtp = smtplib.SMTP()
    print 'connecting ...'

    # show the debug log
    #smtp.set_debuglevel(1)

    # connet
    try:
        print smtp.connect(HOST,PORT)
    except:
        print 'CONNECT ERROR ****'

    # login with username & password
    try:
        print 'loginning ...'
        smtp.login(mail_username,mail_password)
    except:
        print 'LOGIN ERROR ****'
    # fill content with MIMEText's object
    msg = email.mime.text.MIMEText(context)
    msg['From'] = from_addr
    msg['To'] = ';'.join(to_addrs)
    msg['Subject']=title
    #print msg.as_string()
    smtp.sendmail(from_addr,to_addrs,msg.as_string())
    print 'Send success!'
    smtp.quit()

def get_ip_list():
    system = platform.system()
    ip_list = []
    if system == "Linux":
        ip_str = subprocess.Popen("ifconfig", stdout=subprocess.PIPE).stdout.read()
        ip_str = ip_str.split()
        for i in ip_str:
            if i.find("addr:") != -1:
                ip_list.append(i[5:])
    else:
        ip_list = map(lambda i:i[2], socket.gethostbyname_ex(socket.gethostname()))
    return ip_list

def getip():
    rightIP = ''
    ip_list = get_ip_list()
    for i in ip_list:
        if  i.find('172.31') != -1 or i.find('121.229') != -1 or i.find('223.3') != -1:
           rightIP=i
    return rightIP

if __name__ == '__main__':
    current_ip=''
    while True:
        try:
            ip = getip()
            if ip =='':
                print 'get ip failed!'
            else:
                print ip
                if current_ip != ip:
                    SendEmail('IP:'+ip,'IP:'+ip)
                    current_ip = ip
        except Exception, e:
            print e
            pass
        time.sleep(30)
