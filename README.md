# scrape

## 概要
以下の２サイトの記事をテキストファイルに抽出します。<br>
記事のファイル名と同じ名前のテキストファイルに出力します。

### TechCrunch(http://jp.techcrunch.com/)
「機械学習」「人工知能」というタグが付与された記事<br>
＊共に検索結果のページ数があらかじめわかっているものとします。

### iotnews（https://iotnews.jp/）
「機械学習」というワードで検索した結果<br>
＊検索結果のページ数があらかじめわかっているものとします。

## 使いかた
1. 検索内容にあわせて修正します
    1. あらかじめ上記サイトで検索を行い、検索タグやワードにあったURL、ページ数に変更
    1. 出力フォルダ名（存在しないフォルダ名なら予め作成しておく）
2. 実行します

```
$ pyhon scraping_techCrunch.py
```
