import re
import urllib.request
#获取网页内容即DOM
def get_html(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    html = html.decode('utf-8')#将HTML以utf-8的格式解码，否则容易出现乱码和一些错误
    return html
#获取该DOM下所有的图片连接
def get_imgs(html):
    reg = r'src="(.+?\.jpg)" width'#获取图片时的正则表达式
    reg_img = re.compile(reg)
    imglist = reg_img.findall(html)
    return imglist
#将图片下载保存在磁盘上
def output(url):
    html = get_html(url)
    imglist = get_imgs(html)
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,"f:\\%s.jpg"%x)
        x += 1

if __name__ == '__main':
    print('正在运行...')
    output('http://tieba.baidu.com/p/1753935195')
# output('http://tieba.baidu.com/p/1753935195')这一条语句前面不能加空格和回车
