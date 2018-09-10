from bs4 import BeautifulSoup
import urllib.request

url = "https://tieba.baidu.com/p/5639915974"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
def get_html(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'})
    res = urllib.request.urlopen(req)
    html = res.read().decode("utf-8")
    return html
def download(html):
    soup = BeautifulSoup(html,'lxml')
    items = soup.select("div.post_bubble_middle_inner img.BDE_Image")
    x=0
    for item in items:
        urllib.request.urlretrieve(item['src'],"f:\\%s.jpg"%x)
        x=x+1
if __name__ == '__main__':
    html = get_html(url)
    print("正在下载图片...")
    download(html)
    print("图片下载完成!")
