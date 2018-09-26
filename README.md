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
