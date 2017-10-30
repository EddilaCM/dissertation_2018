# __author__ = 'cm'
# -*- coding:utf-8 -*-
import urllib2
import random
from lxml import etree
from cookielib import CookieJar


# 仿浏览器得到HTML,返回节点树
def header_browser(enable_proxy, url_pool, url, agent, accept, accept_charset, accept_encoding, host):
    header = {'User-Agent': agent, 'Accept': accept, 'Accept-Charset': accept_charset, 'Accept_Encoding': accept_encoding, 'Connection': 'close', 'Referer':None , 'Host':host}
    req_timeout = 10
    # 代理设置
    proxy = url_pool[random.randint(0, len(url_pool)-1)]
    print('this IP:',proxy)
    # 是否使用代理
    enable_proxy = enable_proxy
    proxy_handler = urllib2.ProxyHandler({"http":"http://%s" % proxy})
    null_proxy_handler = urllib2.ProxyHandler({})
    if enable_proxy:
        opener = urllib2.build_opener(proxy_handler,urllib2.HTTPHandler(debuglevel=1))
    else:
        opener = urllib2.build_opener(null_proxy_handler)
    urllib2.install_opener(opener)
    try:
        request = urllib2.Request(url, None, header)
    except urllib2.URLError,e:
        print(e.reason)
    response = urllib2.urlopen(request, None, timeout=None)
    html = response.read()
    # print(html)
    my_etree = etree.HTML(html)
    return my_etree


# url带参数
def header_browser1(enable_proxy, url_pool, args, url, agent, accept, accept_charset, accept_encoding, host):
    header = {'User-Agent': agent, 'Accept': accept, 'Accept-Charset': accept_charset, 'Accept_Encoding': accept_encoding, 'Connection': 'close', 'Referer':None , 'Host':host}
    req_timeout = 10
    # 代理意见
    proxy = url_pool[random.randint(0,len(url_pool)-1)]
    print('this IP:',proxy)
    # 是否使用代理
    enable_proxy = enable_proxy
    proxy_handler = urllib2.ProxyHandler({"http":"http://%s" % proxy})
    null_proxy_handler = urllib2.ProxyHandler({})
    if enable_proxy:
        opener = urllib2.build_opener(proxy_handler,urllib2.HTTPHandler(debuglevel=1))
    else:
        opener = urllib2.build_opener(null_proxy_handler)
    urllib2.install_opener(opener)
    data1 = urllib2.urlencode(args)
    url = url + '?' + data1
    print url
    try:
        request = urllib2.Request(url, None, header)
    except urllib2.URLError,e:
        print(e.reason)
    response = urllib2.urlopen(request, None, timeout=None)
    html = response.read()
    # print html
    my_etree = etree.HTML(html)
    # print my_etree
    return my_etree
    request.close()


# 模仿浏览器获取，不带url_pool,带cookie
def header_browser_cookie(url, agent, accept, accept_charset, accept_encoding, host):
    header = {'User-Agent': agent, 'Accept': accept, 'Accept-Charset': accept_charset, 'Accept_Encoding': accept_encoding, 'Connection': 'close', 'Referer':None , 'Host':host}
    req_timeout = 10
    cj = CookieJar
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    try:
        # req = urllib2.Request(url, None, header)
        req = opener.open(url)
    except urllib2.URLError,e:
        print(e.reason)
    resq = urllib2.urlopen(req, None, req_timeout)
    html = resq.read()
    # print html
    my_etree = etree.HTML(html)
    # print my_etree
    return my_etree


# 模仿浏览器获取，不带url_pool
def header_browser_nourl_pool(url, agent, accept, accept_charset, accept_encoding, host):
    header = {'User-Agent': agent, 'Accept': accept, 'Accept-Charset': accept_charset, 'Accept_Encoding': accept_encoding, 'Connection': 'close', 'Referer':None , 'Host':host}
    req_timeout = 10
    try:
        req = urllib2.Request(url, None, header)
    except urllib2.URLError,e:
        print(e.reason)
    resq = urllib2.urlopen(req, None, req_timeout)
    html = resq.read()
    # print html
    my_etree = etree.HTML(html)
    # print my_etree
    return my_etree

