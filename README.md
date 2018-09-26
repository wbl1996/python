# python
几个爬虫，都是最简单的那种，还没解决反爬虫的问题  
反反爬虫需要的技术：
1. 增加请求头
2. 申请多个小号，轮换用户
3. 轮换ip
---
## 我分别使用了不同的方式进行爬虫
1. [scrapy框架](https://github.com/wbl1996/python/tree/master/scrapy/novel)  
这是针对大型项目的框架，使用方便
2. 非框架
- [正则表达式](https://github.com/wbl1996/python/blob/master/spiders/re_spider.py)
- [BeautifulSoup](https://github.com/wbl1996/python/blob/master/spiders/beautifulsoup_spider.py)
## 关于下载文件
有两种方式  
1. 使用[with open](https://github.com/wbl1996/python/blob/master/spiders/image_spider.py) 
2. 使用[urlretrieve](https://github.com/wbl1996/python/blob/master/spiders/beautifulsoup_urlretrive_spider.py)  
使用urlretrieve可能会遇到403的问题，解决方案如下：
- opener = urllib.request.build_opener()
- opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
- urllib.request.install_opener(opener)
- urllib.request.urlretrieve(url,"f:\\img.jpg")
