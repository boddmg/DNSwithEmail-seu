# -*- coding: cp936 -*-
from distutils.core import setup
import py2exe
import shutil  

options = {"py2exe":
    {"compressed": 0, 
     "optimize": 2,
     "bundle_files": 1,
    }
    }
setup(console=['DnsWithEmail_Getip.py'],options = options)
setup(console=['DnsWithEmail_Uploader.py'],options = options)
shutil.copyfile("config.ini","dist\config.ini")
