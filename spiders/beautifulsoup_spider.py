import urllib.request
from bs4 import BeautifulSoup


def get_html(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'})
    res = urllib.request.urlopen(req)
    html = res.read().decode("utf-8")
    return html


def get_imgs(html):
    x = 1
    soup = BeautifulSoup(html,'lxml')
    items = soup.select("img.BDE_Image")
    for item in items:
        with open("f:/IMG/%s.jpg"%x,'wb') as f:
            res = urllib.request.urlopen(item["src"])
            f.write(res.read())
            f.close()
        x = x+1


if __name__ == '__main__':
    print("开始获取页面...")
    html = get_html("https://tieba.baidu.com/p/1753935195?red_tag=0742995080")
    print("获取页面完毕!")
    print("开始下载图片...")
    get_imgs(html)
    print("图片下载完成!")

