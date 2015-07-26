#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import time
import httplib
from bs4 import BeautifulSoup
from urlparse import urlparse
from urllib import urlretrieve
import os
import json
# import hashlib
# import urllib
# import urllib2
# from PIL import Image
# https://www.google.com.hk/search?q=one+year+old+baby&newwindow=1&safe=active&hl=en&biw=1920&bih=955&site=imghp&tbm=isch&ijn=3&ei=azx1VYvkBqGzmwXs04LoDg&start=300


def get_img_keyword(keyword, start, file_object, dst):
    conn = httplib.HTTPSConnection('www.google.com.hk', 443)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
        # 'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'referer': 'https://www.google.com.hk/'
    }
    req_url = str("https://www.google.com.hk/search?q=" + keyword +
                 "&newwindow=1&safe=active&hl=en&biw=1920&bih=955&site=imghp&tbm=isch&ijn=3"
                 "&ei=azx1VYvkBqGzmwXs04LoDg&start=" + start)
    conn.request("GET", req_url, headers=headers)

    r1 = conn.getresponse()
    htmltext = r1.read()
    time.sleep(0.5)
    conn.close()

    img_urls = []
    formatted_images = []

    soup = BeautifulSoup(htmltext)
    results = soup.findAll("a")

    cot = 0
    t1 = 'source: '
    t2 = ' dst '
    t3 = ' success'
    t4 = ' fail'
    t5 = ' exist'

    for r in results:
        try:
            if "imgres?imgurl" in r['href']:
                img_urls.append(r['href'])
        except:
            a = 0

    for im in img_urls:
        refer_url = urlparse(str(im))
        image_f = refer_url.query.split("&")[0].replace("imgurl=", "")
        formatted_images.append(image_f)

        tt = image_f.split('/')
        image_name = tt[-1]
        # name = dst + '/' + date + '_' + image_name

        type = image_name.split('.')[-1]
        if type != 'jpg' and type != 'png' and type != 'JPG' and type != 'PNG':
            type = 'jpg'
            name = dst + '/' + image_name + '_' + str(cot) + '.' + type
        else:
            name = dst + '/' + image_name[0:len(image_name) - len(type) - 1] + '_' + str(cot) + '.' + type

        # type = image_name.split('.')[-1]
        cot += 1
        # name = dst + '/' + image_name[0:len(image_name)-len(type)-1] + '_' + str(cot) + '.' + type

        if os.path.exists(name):
            str_print = t1 + image_f + t2 + name + t5
            print str_print
            print >> file_object, str_print
            continue

        try:
            urlretrieve(image_f, name)
            tag = 1
        except:
            tag = 0
            pass

        if (tag == 1):
            str_print = t1 + image_f + t2 + name + t3
        else:
            str_print = t1 + image_f + t2 + name + t4

        print str_print
        print >> file_object, str_print

    return formatted_images

keywords_list = [
    # 'one+month+old', 'two+months+old', 'three+months+old', 'four+months+old','five+months+old', 'six+months+old','seven+months+old', 'eight+months+old', 'nine+months+old',
    # 'ten+month+old', 'eleven+months+old', 'twelve+months+old','one+year+old','2+years+old', '3+years+old', '4+years+old', '5+years+old','6+years+old', '7+years+old','8+years+old',
    # '9+years+old', '10+years+old', '11+years+old','12+years+old','13+years+old','14+years+old','15+years+old', '16+years+old', '17+years+old', '18+years+old', '19+years+old',
    # '20+years+old', '21+years+old','22+years+old', '23+years+old', '24+years+old', '25+years+old', '26+years+old','27+years+old', '28+years+old','29+years+old', '30+years+old',
    # '31+years+old', '32+years+old', '33+years+old', '34+years+old', '35+years+old', '36+years+old','37+years+old','38+years+old','39+years+old', '40+years+old',
    # '41+years+old', '42+years+old','43+years+old', '44+years+old', '45+years+old', '46+years+old','47+years+old','48+years+old','49+years+old', '50+years+old',
    # '51+years+old', '52+years+old', '53+years+old', '54+years+old', '55+years+old', '56+years+old',
    # '57+years+old', '58+years+old','59+years+old', '60+years+old','61+years+old', '62+years+old', '63+years+old', '64+years+old', '65+years+old', '66+years+old','67+years+old', '68+years+old','69+years+old', '70+years+old',
    # '71+years+old', '72+years+old', '73+years+old', '74+years+old', '75+years+old', '76+years+old','77+years+old', '78+years+old','79+years+old', '80+years+old',
    # '81+years+old', '82+years+old', '83+years+old','84+years+old', '85+years+old','86+years+old','87+years+old', '88+years+old','89+years+old', '90+years+old',
    # '91+years+old', '92+years+old', '93+years+old', '94+years+old','95+years+old', '96+years+old','97+years+old', '98+years+old','99+years+old', '100+years+old',
    # 'more+than+100+years+old'

    'face', 'infant', 'baby', 'child', 'person', 'girl', 'boy', 'man', 'woman', 'lady', 'gentleman', 'young', 'old',
    'infant+face', 'baby+face', 'child+face',
    'person+face', 'girl+face', 'beautiful+girl', 'beautiful+girl+face', 'boy+face', 'handsome+boy',
    'handsome+boy+face', 'man+face', 'woman+face',
    'lady+face', 'gentleman+face', 'young+face', 'young+age', 'young+age+face', 'young+person', 'young+person+face',
    'young+man', 'young+man+face',
    'young+woman', 'young+woman+face', 'old+face', 'old+age', 'old+age+face', 'old+person', 'old+person+face',
    'old+man', 'old+man+face', 'old+woman',
    'old+woman+face', 'middle+age', 'middle+age+face', 'middle-age+person', 'middle-age+person+face', 'middle-age+man',
    'middle-age+man+face',
    'middle-age+woman', 'middle-age+woman+face'
]

socket.setdefaulttimeout(10)
beg1 = 147  # 开始爬取点
end1 = 1000  # 结束爬取点
step = 21  # 爬取的步进

settings = json.load(open("./local_settings.json"))
path = str(settings["path"]) + "/google"
# 保存图片路径
dst = path + "/img"
# 保存爬取图片的信息路径
txt_dst = path + "/log"

# keywords in keywords_list:
# 26  gentleman+face
# 36  old+face
start_key = 36
for i in range(start_key, len(keywords_list)):

    # 获取关键字
    keywords = keywords_list[i]

    # 以关键字命名文件夹（存放爬取的图片）
    save_dst = dst + '/' + keywords
    if not os.path.exists(save_dst):
        os.makedirs(save_dst)

    # 以关键字命名文件夹（存放爬取的图片的txt信息）
    save_txt_dst = txt_dst + '/' + keywords
    if not os.path.exists(save_txt_dst):
        os.makedirs(save_txt_dst)

    if not (i == start_key):
        beg1 = 0

    for start in range(beg1, end1, step):

        link_txt = save_txt_dst + '/' + str(start) + '.txt'

        if os.path.exists(link_txt):
            file_tmp = open(link_txt, 'rU')
            count = len(file_tmp.readlines())
            file_tmp.close()
        else:
            count = 0

        if count == step:
            print link_txt, 'was finished, go to next one'
            continue

        # 保存某一个start开始的step个图片的信息（原链接，保存本地路径，是否爬取成功）
        file_object = open(link_txt, 'w')

        print keywords, 'start from ', str(start), ' to ', str(start + step - 1)
        # 爬取某一个start开始的step个图片
        ret = get_img_keyword(keywords, str(start), file_object, save_dst)

        file_object.close()

        # 当爬取完某一个关键字后，跳出循环到下一个关键字
        if len(ret) < 21:
            print  'it is finished for the keywords (web cralwer): ', keywords
            continue
