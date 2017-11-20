import requests
import re
from bs4 import BeautifulSoup

file_path = './data/'

searchResults = ['https://iotnews.jp/archives/tag/%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92','https://iotnews.jp/archives/tag/%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92/page/2', 'https://iotnews.jp/archives/tag/%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92/page/3']
contentsUrls = []

def findContentsURL(url):
    # 対象URLにアクセス
    res = requests.get(url)

    # コンテンツ（検索結果）を取得
    content = res.content
    soup = BeautifulSoup(content, 'html.parser')
    targets = soup.find_all('article', class_='field_post_1')

    for target in targets:
        txt = target.a['href']
        contentsUrls.append(txt)

def getContens(url):
    # 対象URLにアクセス
    print(url)
    paths = url.split('/')
    fname = paths[len(paths) - 1]
    fw = open(file_path + fname, 'w')

    res = requests.get(url)

    # コンテンツ（検索結果）を取得
    content = res.content
    soup = BeautifulSoup(content, 'html.parser')
    targets = soup.find_all('section', class_='post-content')

    for target in targets:
        txt = target.find_all('p') 

        for t in txt:
            fw.write(t.text)

    fw.close()


if __name__ == '__main__':
    for searchResult in searchResults:
        findContentsURL(searchResult)
#    for contentsUrl in contentsUrls:
#        print(contentsUrl)

#    print('--------------')
#    getContens('https://iotnews.jp/archives/58902')


    for contentsUrl in contentsUrls:
        getContens(contentsUrl)
#    for content in contents:
#        print('--------------')
#        print(contents)
