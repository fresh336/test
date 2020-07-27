#!/usr/bin/env python
#-*-coding:utf-8-*
#------------------------------
import datetime,sys
from time import sleep
import matplotlib.pyplot as plt
from pylab import *
import socket
import datetime
mpl.rcParams['font.sans-serif'] = ['SimHei']  #画图中支持黑体字体
address = ('192.168.93.128', 31500)  # 服务端地址和端口
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #域，AF_INET（Internet 网络，常用）/类型：面向流对应TCP，数据报对应UDP
t = []  # 创建时间空列表
cpu = []  # 创建CPU空列表
up = []  # 创建CPU空列表
down = []  # 创建CPU空列表
plt.figure(figsize=(8, 4))
k = 1
while True:
    trigger = 'connection ok'  # input('Input: ')
    s.sendto(trigger.encode(), address)
    data, addr = s.recvfrom(1024)  # 返回数据和接入连接的（服务端）地址
    data = float(data.decode())
    #b="%.2f%%" % (data * 100)
    b=float(data)
    print('[RX_Used]',b)  #转换成百分比
    #print(data2.split('+')[1])
    #print(data2.split('+')[2])
    t.append(datetime.datetime.now().strftime('%I:%M:%S'))  # 指定时间格式为:时+分+秒,并append追加到列表t[]末尾
    ##########cpu.append(b)
    up.append(b)
    #print(t);print(cpu)
    #print("^_^===============================俺是分割线===============================^_^")
    plt.ylim(0, 1)    # 限定纵轴的范围
    ######################################################################################开始画图
    y = int(k / 8)
    if y >= 1:
                #plt.plot(t, t1, marker='o', mec='r', mfc='w', label=u'温度曲线图')  # 画t和t1的折线图,mec是外圈颜色，mfc是填充颜色
                plt.plot(t, cpu,marker='p', mec='y', mfc='w', label=u'CPU占用率曲线图')  # 画t和h1的折线图
                #plt.plot(t, up,marker='p', mec='y', mfc='w', label=u'上行速度')  # 画t和h1的折线图
                #plt.plot(t, down,marker='p', mec='r', mfc='w', label=u'下行速度')  # 画t和h1的折线图
                plt.xticks(t[::y], rotation=45)  # 把x轴文字弄成斜45度，排布不密集
    else:
                #plt.plot(t, t1, marker='o', mec='r', mfc='w', label=u'温度曲线图')  # 画t和t1的折线图,mec是外圈颜色，mfc是填充颜色
                plt.plot(t, cpu, marker='p', mec='y', mfc='w', label=u'CPU占用率曲线图')  # 画t和h1的折线图
                #plt.plot(t, up,marker='p', mec='y', mfc='w', label=u'上行速度')  # 画t和h1的折线图
                #plt.plot(t, down,marker='p', mec='r', mfc='w', label=u'下行速度')  # 画t和h1的折线图
                plt.xticks(t, rotation=45)

    plt.legend()                      #让图例生效
    #plt.xticks(t, rotation=45)        #把x轴文字弄成斜45度
    plt.margins(0)                    #把图表弄好看点
    plt.xlabel("Time")                #添加X轴标签
    #plt.ylabel("CPU_Used")           #添加Y轴标签
    plt.ylabel("Used")           #添加Y轴标签
    plt.title("Linux服务器性能监控平台-"+str(len(t))+"次数据")  #添加title标题
    k=k+1
    plt.savefig("D:\\cpu_Used.png")      #将画图的图片保存到默认路径中
    #plt.savefig("D:\\download_Used.png")      #将画图的图片保存到默认路径中
    plt.pause(1)                     #暂停12秒
    #plt.show
    plt.clf()    # 清除当前figure所有axes，但是不关闭这个window，所以能继续复用于其它的plot。




s.close()