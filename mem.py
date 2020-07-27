# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 15:21:01 2020

@author: root
"""

#!/usr/bin/env Python



from __future__ import print_function
from collections import OrderedDict

  
import time

def meminfo():

    ''' Return the information in /proc/meminfo

    as a dictionary '''

    meminfo=OrderedDict()

 

    with open('/proc/meminfo') as f:

         for line in f:

             meminfo[line.split(':')[0]] = line.split(':')[1].strip()

    return meminfo

 

if __name__=='__main__':

    #print(meminfo())

 
    while True:
          
          meminfo = meminfo()
          print('Total memory: {0}'.format(meminfo['MemTotal']))
          print('Free memory: {0}'.format(meminfo['MemFree']))
          time.sleep(1)