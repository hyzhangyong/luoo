#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: hyzhangyong
# @Date:   2016-05-15 00:23:46
# @Last Modified by:   hyzhangyong
# @Last Modified time: 2016-05-15 18:30:20
import re,os
import urllib
import requests
from lxml.html import fromstring
def mkdir(name):
    #name=name.decode('utf-8').encode('gbk')
    ospath=os.getcwd()
    path=os.path.join(ospath,name)
    isExists=os.path.exists(name)
    if not isExists:
        print name.decode('utf-8').encode('gbk'),u'创建成功!'
        os.makedirs(name)
    else:
        print name.decode('utf-8').encode('gbk'),u'已存在!'
    return path
def main(afew):
    url='http://www.luoo.net/music/'+afew
    # url='http://www.luoo.net/music/820'
    # p=re.compile(r'\d+')
    # afew=p.search(url).group()
    req=requests.get(url)
    # print req.content
    Introduction=fromstring(req.content).xpath('//div[@class="vol-desc"]/text()')
    Introduction=[x.strip() for x in Introduction]
    title=fromstring(req.content).xpath('//span[@class="vol-title"]/text()')
    img=fromstring(req.content).xpath('//div[@class="vol-cover-wrapper"]/img/@src')
    path=mkdir(title[0])
    with open(os.path.join(path,title[0]+'.txt'), 'w') as f:
        f.write('\n'.join(Introduction))
    mp3name=fromstring(req.content).xpath('//div[@class="track-wrapper clearfix"]/a[1]/text()')
    for i in range(len(mp3name)):
        local=os.path.join(path,mp3name[i]+'.mp3')
        i=i+1
        mp3url='http://luoo-mp3.kssws.ks-cdn.com/low/luoo/radio'+afew+'/'+'%02d'%i+'.mp3'
        urllib.urlretrieve(mp3url,local)
    urllib.urlretrieve(img[0],os.path.join(path,title[0]+'.jpg'))
if __name__ == '__main__':
    afew=raw_input('请输入期数回车下载:'.decode('utf-8').encode('gbk'))
    while afew =='':
        afew=raw_input('请输入期数回车下载:'.decode('utf-8').encode('gbk'))
    main(afew)
