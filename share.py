import ConfigParser
def SetIDFromFile(fileName):
    cf = ConfigParser.ConfigParser()
    cf.readfp(open(fileName))    
    mail_username=cf.get("EmailAccount","ID",raw=True)
    mail_password=cf.get("EmailAccount","password",raw=True)
    return [mail_username,mail_password]
