import urllib.request
from bs4 import BeautifulSoup
global x
x = 0
url = "https://www.socwall.com/wallpapers/page:1/"
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
#获取单个页面的html代码，即点进去一个主页图片后的html
def get_html(url):
    req = urllib.request.Request(url,headers = header)
    html = urllib.request.urlopen(req)
    html = html.read()
    return html
#根据主页获取1-9页的url，这里我只写了9页，因为没有优化，所有不敢写太多。 
def get_allurls(url):
    urls = []
    for x in range(1,10):
        urllsit = list(url)
        urllsit[-2] = str(x)
        item = ''.join(urllsit)
        urls.append(item)
    return urls
#每个主页都有多个图片的预览图，点击就进入到该图片的展示页面，这里获取的是一个页面所有预览图点击时的请求
def get_one_page_img_urls(url):
    page = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'})
    html = urllib.request.urlopen(page).read()
    soup = BeautifulSoup(html,'lxml')
    items = soup.select("a.image")
    hrefs = []
    for item in items:
        href = item['href']
        hrefs.append(href)
    return hrefs
#获取一页上的所有图片
def get_one_page_imgs(hrefs):#hrefs 是一个页面下的所有连接请求
    global x
    for href in hrefs:
        imgurl = 'https://www.socwall.com'+href
        html = get_html(imgurl)
        soup = BeautifulSoup(html,'lxml')
        items = soup.select("div.wallpaper img")
        for item in items:
            url = 'https://www.socwall.com' + item['src']
            content = get_html(url)
            with open("f:/desktopImages/%s.jpg"%x,'wb') as f:
                f.write(content)
                f.close()
            x = x+1
#获取所有图片
def download_all_images(url):
    print("正在下载图片...")
    urls = get_allurls(url)
    for url in urls:
        hrefs = get_one_page_img_urls(url)
        get_one_page_imgs(hrefs)
    print("图片下载已完成！")
# if __name__ == '__main__':
#     download_all_images(url)
download_all_images(url)
