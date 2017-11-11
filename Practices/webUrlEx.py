# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 17:28:15 2017
responseurllib.request.urlopeur
@author: weizy
"""

import urllib.request
import urllib.parse

def youdao(str1='I love henry'):
    urlYoudao="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com"
    
    head={}
    head['Referer']='http://fanyi.youdao.com'
    head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    data={}
    data['type']='AUTO'
    data['i']=str1
    data['doctype']='json'
    data['xmlVersion']='1.6'
    data['keyfrom']='fanyi.web'
    data['ue']='UTF-8'
    data['typoResult']='true'
    
    data=urllib.parse.urlencode(data).encode('utf-8')
    req=urllib.request.Request(urlYoudao,data,head)
    response=urllib.request.urlopen(req)
    html=response.read().decode('utf-8')
    return html


def webOpen(url):
    response=urllib.request.urlopen(url)
    html=response.read()
    return html
    

if __name__=='__main__':
    '''
    urlCount="http://wenshu.court.gov.cn/"
    print(webOpen(urlCount).decode('utf-8'))
    urlCat="http://placekitten.com/g/400/400"
    cat_img=webOpen(urlCat)
    with open('cat_400_600.jpg','wb') as f:
        f.write(cat_img)
    '''
    print(youdao())