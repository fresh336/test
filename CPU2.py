# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 15:19:22 2020

@author: root
"""

#!/usr/bin/env Python   
import time
import sys
import os

def load_stat():

    loadavg = {}

    f = open("/proc/loadavg")

    con = f.read().split()

    f.close()

    loadavg['lavg_1']=con[0]

    loadavg['lavg_5']=con[1]

    loadavg['lavg_15']=con[2]

    loadavg['nr']=con[3]

    loadavg['last_pid']=con[4]

    return loadavg 
    
    

while 1:
   time.sleep(2)
   print ("loadavg",load_stat()['lavg_15'])
   