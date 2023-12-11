#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os
import shutil
import socket
import zipfile
from os.path import join, getsize


def zip_file(src_dir):
    '''
    实现对文件夹的压缩
    :param src_dir: 传入要压缩的文件夹路径
    :return:
    '''
    zip_name = src_dir +'.zip'
    z = zipfile.ZipFile(zip_name,'w',zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(src_dir):
        fpath = dirpath.replace(src_dir,'')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dirpath, filename),fpath+filename)
            print ('==压缩成功==')
    z.close()


def locathost_ip():
    '''
    获取本机的ip地址方法1
    :return:
    '''
    # # 获取计算机名称
    # hostname = socket.gethostname()
    # # 获取本机IP
    # ip = socket.gethostbyname(hostname)
    # return ip
    '''
    获取本机的ip地址方法2
    :return:
    '''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip
