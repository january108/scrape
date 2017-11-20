import requests
import re
from bs4 import BeautifulSoup

file_path = './techCrunch/'

# TECH CRUNCH 機械学習 1-6
idxsMachine = ['1', '2', '3', '4', '5', '6', ]
searchMachine = 'http://jp.techcrunch.com/%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92/page/*/'

idxsAI = ['1', '2', '3', '4', '5', '6', '7']
searchAI = 'http://jp.techcrunch.com/%E4%BA%BA%E5%B7%A5%E7%9F%A5%E8%83%BD/page/*/'

contentsUrls = []


def findSearchURL(url, replace):
    # 対象URLにアクセス
    realurl = url.replace('*', replace)
    res = requests.get(realurl)

    # コンテンツ（検索結果）を取得
    content = res.content
    soup = BeautifulSoup(content, 'html.parser')
    results = soup.find_all('div', class_='block-content')

    for result in results:
        title = result.h2.text
        url = result.a['href']
        contentsUrls.append(str(url))

def getContens(url):
    print(url)
    # 出力ファイルを決める
    paths = [i for i in re.split(r'/',url) if i != '']
    fname = paths[len(paths) - 1]
    fw = open(file_path + fname, 'w')

    # 対象URLにアクセス
    res = requests.get(url)

    # コンテンツ（検索結果）を取得
    content = res.content
    soup = BeautifulSoup(content, 'html.parser')

    target = soup.find('div', class_='l-main')
    title = target.h1.text
    fw.write(title)

    article = target.find('div', class_='text')
    txt = article.find_all('p')
    for t in txt:
        t1 = t.text

        if t1 == '':
            continue

        idx = t1.find('[原文へ]')
        if idx != -1:
            break

        idx = t1.find(('!function'))
        if idx != -1:
            continue

        fw.write(t1)

    fw.close()

def sample():
    url = 'https://pycon.jp/2017/ja/sponsors/'
    res = requests.get(url)
    content = res.content
    soup = BeautifulSoup(content, 'html.parser')
    sponsors = soup.find_all('div', class_='sponsor-content')
    for sponsor in sponsors:
        url = sponsor.h3.a['href']
        name = sponsor.h4.text
        print(name, url)

if __name__ == '__main__':
    # タグ：機械学習の記事のURLを取得
    for idx in idxsMachine:
        findSearchURL(searchMachine, idx)
    # タグ：人工知能の記事のURLを取得
    for idx in idxsAI:
        findSearchURL(searchAI, idx)
    # 重複を排除
    contentsUnq = list(set(contentsUrls))
#    contentsUnq.sort()

    # 記事のコンテンツを取得し、ファイル出力
    for contentsUrl in contentsUnq:
        getContens(contentsUrl)
#    getContens('http://jp.techcrunch.com/2017/11/18/2017-11-16-the-tesla-semi-tackles-this-classic-truck-safety-problem-using-tech/')
