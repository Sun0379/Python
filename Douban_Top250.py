#-*coding:utf-8-*-
#引入BeautifulSoup，这个东西可以从HTML/XML中提取标签内容
from bs4 import BeautifulSoup
#requests是urllib的升级版
import requests
#codecs的open()方法，会在读取的时候将其自动转换为内部unicode
import codecs

TOP250_URL = 'http://movie.douban.com/top250'

#请求url的时候加入header，伪装成浏览器
def html_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
        }
    data = requests.get(url,headers=headers).content
    return data
def parse_html(html):
    #创建BeautifulSoup对象时要指定解释器，用lxml或者html.parser都可以
    soup = BeautifulSoup(html,"lxml")
    #find()方法检测字符串中是否包含某些关键字
    #开发者工具搜索一下片名，确定关键字grid_view/ol/li
    movie_list_soup = soup.find('ol',attrs={'class':'grid_view'})
    movie_name_list = []
    for movie_li in movie_list_soup.find_all('li'):
        detail = movie_li.find('div',attrs={'class':'hd'})  
        movie_name = detail.find('span',attrs={'class':'title'}).getText()
        movie_name_list.append(movie_name)
        print (movie_name)
    next_page = soup.find('span',attrs={'class':'next'}).find('a')
    if next_page:
        return movie_name_list,TOP250_URL + next_page['href']
    #None表示不写入url
    return movie_name_list,None

def main():
    url = TOP250_URL
    with codecs.open('movies','wb',encoding='utf-8') as fp:
        while url:
            html = html_page(url)
            movies,url = parse_html(html)
            fp.write(u'{movies}\n'.format(movies='\n'.join(movies)))
    #print(download_page(TOP250_URL))

if __name__ == '__main__':
    main()
