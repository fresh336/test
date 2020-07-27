from lxml import etree
import requests
from urllib.parse import urljoin
import time
from random import random
import os
#导入所需要的库，这里只有requests库需要下载
"""
本实验可以利用http下载一个网页下的所有图片“jpge和png格式”
用于树莓派对局域网一个设备的控制下载
"""
class Spider(object):
    """
    定义一个爬虫类
    """
    def __init__(self, url1):
        """
        初始化构造函数
        :param url1: 图片的链接地址，即图片的父目录
        """
        self.url = url1
        self.url_list = None
        self.headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36\
         (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
         #浏览器标识，这已经是一个不存在的浏览器

    def get_all_url(self):
        """
        该函数用于获取url下所有的图片链接
        :return:
        """
        response = requests.get(self.url, headers=self.headers)
        #获取
        text = response.text
        #HTTP响应以字符串形式返回
        html = etree.HTML(text)
        result_list = html.xpath('//a/@href')  # 获取所有链接
        result_list2 = [urljoin(response.url, x) for x in result_list]  # 拼接所有链接
        result_list3 = [y for y in result_list2 if y.lower().endswith('jpg') or y.lower().endswith('png')]#获取要下载的就jpge和png格式文件
        print('共发现{}条超链接'.format(len(result_list2)))
        print('其中{}条为图片'.format(len(result_list3)))
        self.url_list = result_list3

    def download_one_picture(self, url_1):
        """
        用于下载单张图片
        :param
        """
        response = requests.get(url_1, headers=self.headers, stream=False)  # 暂不开始下载
        size = int(response.headers['Content-Length'])  # 获取文件大小
        size2 = size / (1024**2)
        # 判断文件夹是否存在，不存在则创建
        if not os.path.exists('./img'):
            os.mkdir('./img')
        file_name = url_1.split('/')[-1]  # 获取文件名
        download_size = 0  # 已下载大小
        print(f'正在下载，文件大小为{size2:.2f}M')
        start_time = time.time()  # 记录开始时间
        with open('./img/' + file_name, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):  # 分片下载
                #使用分片下载可以边下边存还可以统计下载速度
                if bool(chunk):
                    download_size += 1024
                    a = '*' * int(100 * download_size / size)  # 已完成
                    b = '_' * int(100 - download_size * 100 / size)  # 未完成
                    c = (download_size / size) * 100
                    t = time.time() - start_time
                    speed = round(download_size / t / 1024, 2)
                    print('\r完成度：{:^3.0f}%\t[{}{}]已下载：{:.2f}k，网速：{:.2f}k/s'\
                          .format(c, a, b, download_size / 1024, speed), end='')
                          #利用变量做一个类似进度条
                    f.write(chunk)
                    f.flush()
        print('\n该文件下载完成\n')

    def download_all_picture(self):
        self.get_all_url()  # 获取超链接下所有图片
        # 循环下载
        for url_ll in self.url_list:
            self.download_one_picture(url_ll)
            time.sleep(random() + 0.2)
        print('\n')
        print('=' * 20)
        print('所有文件均下载完毕')
        print('=' * 20)


if __name__ == '__main__':
    #url = 'http:192.168.122.1：61000/'
    url = input('请输入图片所在网址，按回车键正式运行：')
    spider = Spider(url)
    spider.download_all_picture()  # 下载所有图片
    # spider.get_all_url()
    # test_png_url = 'https://www.vbahome.cn/static/blog/img/summary.png'
    # spider.download_one_picture(test_png_url)
