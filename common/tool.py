#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os
import shutil
import socket
import zipfile
from os.path import join, getsize
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


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


def get_code():
    """
    进入登录页面截图并获取验证码位置进行截图保存到本地
    :return:
    """
    url = 'http://jswzh.gagogroup.cn:8081/Account/Login'
    driver = webdriver.Chrome()
    driver.maximize_window()  # 屏幕最大化
    driver.get(url)

    # 截指定位置的图片
    element = driver.find_element(By.XPATH, r"/html/body/div/div[3]/div/div/div/form/p[4]/img")  # 截百度一下图标
    # element.screenshot('./baiduyixia.png')     #图片会保存到当前目录下
    element.screenshot(r'/Users/chenjiawei/Desktop/测试数据/tp/code2.png')
    time.sleep(3)

    driver.close()


import ddddocr

'/Users/chenjiawei/Desktop/测试数据/tp/7.png'
def picture_ocr(picture):
    ocr = ddddocr.DdddOcr()
    with open(picture, 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)
    print(res[0])

'''
import tesserocr
from PIL import Image
import numpy as np
'/Users/chenjiawei/Desktop/测试数据/tp/7.png'
def picture_ocr1(picture):
    image = Image.open(picture)
    image = image.convert('L')
    threshold = 50
    array = np.array(image)
    array = np.where(array > threshold, 255, 0)
    image = Image.fromarray(array.astype('uint8'))
    image.show()
    test = tesserocr.image_to_text(image)
    print(test)
    # time.sleep(3)
    # image.close()
def picture_ocr2(picture):
    test = tesserocr.file_to_text(picture)
    print(test)
    if test[1] == "+":
        print(int(test[0]) + int(test[2]))
    elif test[1] == "-":
        print(int(test[0]) - int(test[2]))
    elif test[1] == "*":
        print(int(test[0]) * int(test[2]))
    elif test[1] == "/":
        print(int(test[0]) / int(test[2]))
    else:
        print("符合不匹配")


def picture_ocr3(picture):
    image = Image.open(picture)  # 读取图片
    image = image.convert("L")  # 传入L参数，代表将图片转为灰度图片
    width = image.size[0]  # 获取图片的宽度
    height = image.size[1]  # 获取图片的高度
    threshold = 150  # 设置阈值
    for h in range(0, height):
        for w in range(0, width):
            if image.getpixel((w, h)) < threshold:  # 遍历每一个像素点，并与阈值比较
                image.putpixel((w, h), (0))  # 如果小于阈值，则像素点的值变成0（黑色）
            else:
                image.putpixel((w, h), (255))  # 如果大于阈值，则像素点的值变成255（白色）
    image.show()
    result = tesserocr.image_to_text(image)  # 识别图片文字内容
    print(result)
    '''


if __name__ == '__main__':
    # picture_ocr('/Users/chenjiawei/Desktop/测试数据/tp/1.png')
    # picture_ocr2('/Users/chenjiawei/Desktop/测试数据/tp/code2.png')
    # picture_ocr2('/Users/chenjiawei/Desktop/测试数据/tp/1.png')
    pass





