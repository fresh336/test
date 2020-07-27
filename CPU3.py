# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 18:52:23 2020

@author: root
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re,time,sys
import socket
import datetime

def _read_cpu_usage(): 
        """Read the current system cpu usage from /proc/stat""" 
        statfile = "/proc/stat" 
        cpulist = [] 
        try: 
                f = open(statfile, 'r') 
                lines = f.readlines() 
        except: 
                print ("ERROR: Can not open %s,The system cannot continue to run" % (statfile) )
                return [] 
        for line in lines:
            tmplist = line.split()
            if len(tmplist) < 5:
                continue
            for b in tmplist:
                 m = re.search(r'cpu\d+',b)
                 if m is not None:
                    cpulist.append(tmplist)
        f.close()
        return cpulist

def get_cpu_usage(): 
        cpuusage = {} 
        cpustart = {} 
        cpuend = {} 
        linestart = _read_cpu_usage() 
        if not linestart: 
                return 0 
        for cpustr in linestart: 
                usni=int(cpustr[1])+int(cpustr[2])+int(cpustr[3])+int(cpustr[5])+int(cpustr[6])+int(cpustr[7])+int(cpustr[4]) 
                usn=int(cpustr[1])+int(cpustr[2])+int(cpustr[3]) 
                cpustart[cpustr[0]] = str(usni)+":"+str(usn) 
        sleep = 2 
        time.sleep(sleep) 
        lineend = _read_cpu_usage() 
        if not lineend: 
                return 0 
        for cpustr in lineend: 
                usni=int(cpustr[1])+int(cpustr[2])+int(cpustr[3])+int(cpustr[5])+int(cpustr[6])+int(cpustr[7])+int(cpustr[4]) 
                usn=int(cpustr[1])+int(cpustr[2])+int(cpustr[3]) 
                cpuend[cpustr[0]] = str(usni)+":"+str(usn) 
        for line in cpustart: 
                start = cpustart[line].split(':') 
                usni1,usn1 = float(start[0]),float(start[1]) 
                end = cpuend[line].split(':') 
                usni2,usn2 = float(end[0]),float(end[1]) 
                cpuper=(usn2-usn1)/(usni2-usni1) 
                cpuusage[line] = cpuper
         
        return cpuusage 

if __name__ == '__main__': 
    
   address = ('192.168.169.139', 31500)  # 服务端地址和端口
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #域，AF_INET（Internet 网络，常用）/类型：面向流对应TCP，数据报对应UDP
   s.bind(address)  # 绑定服务端地址和端口 
   print ('Waiting for connection...')
   while True:

       
        a = get_cpu_usage()['cpu0']
        print ('cpu used age:' ,a)
        
        data, addr = s.recvfrom(1024)  # 返回数据和接入连接的（客户端）地址
        data = data.decode()
        if not data:
           break
        print('[Received]', data)
        send = str(a).encode()
        s.sendto(send, addr)  # UDP 是无状态连接，所以每次连接都需要给出目的地址
        time.sleep(1)
        
   s.close()
        