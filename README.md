# Techosity Searcher
技術検索アプリ「Techosity」の検索システム

## 起動方法
```bash
$ cd ~/path/to/techosity-searcher

# .envファイルをコピーして、適切な値に書き換える
$ cp ./searcher/.env.sample ./searcher/.env
$ cp ./elasticsearch/.env.sample ./elasticsearch/.env

# コンテナの起動
$ docker-compose up --build

# Flask(API)を起動
$ docker-compose run --rm -v `pwd`/searcher:/app/ -p 5000:5000 searcher python start_api.py

# RabbitMQ(MQ)を起動
$ docker-compose run --rm -v `pwd`/searcher:/app/ searcher python start_mq.py
```

 - [Flaskアプリ画面](http://localhost:5000)
 - [RabbitMQのツール画面](http://localhost:15672/)

## 検索エンジン
検索エンジンには、ElasticSearchを利用しています。

<details><summary>インデックスの作成</summary>

```bash
# インデックスblogsを作成
$ curl -XPUT 'http://localhost:9200/blogs'
```

</details>

<details><summary>データ投入</summary>

```bash
# blogsインデックスにデータ投入
$ curl -XPUT 'http://localhost:9200/blogs/_doc/1?pretty' -H 'Content-Type: application/json' -d '
{
  "title": "LAPRASポートフォリオタグの分類実験とパイプライン設計 - LAPRAS AI LAB",
  "description": "はじめに こんにちは、LAPRASのAILABチームです。今回は池・田嶋・森元で、LAPRASポートフォリオのタグをエンジニア関連のタグ(エンジニアタグ)とそうでないタグ(非エンジニアタグ)に分類する分類器を検討してみました。ここではその実験の詳細と、また再現性のある方法で分類器を得るためのパイプラインについて検討した内容をまとめます。 タグ分類 現在のLAPRASポートフォリオ上では図のようにユ … \"LAPRASポートフォリオタグの分類実験とパイプライン設計\" の続きを読む",
  "url": "https://ai-lab.lapras.com/nlp/laprasポートフォリオタグの分類実験とパイプライン/"
}
'
$ curl -XPUT 'http://localhost:9200/blogs/_doc/2?pretty' -H 'Content-Type: application/json' -d '
{
  "title": "求人のレベル判定に関する実験まとめ - LAPRAS AI LAB",
  "description": "はじめに こんにちは、LAPRAS Researchチームの池・森元です。LAPRASでは最近、転職活動支援の一環として新機能のJOB LISTや転職支援サービスのLAPRAS CAREER β版をリリースしています。これらに伴い、私たちResearchチームでは、人と求人のマッチングアルゴリズム開発に注力しています。 人と求人のマッチング時には転職希望者と求人のレベル感をマッチさせる必要がありま … \"求人のレベル判定に関する実験まとめ\" の続きを読む",
  "url": "https://ai-lab.lapras.com/deep-learning/求人のレベル判定に関する実験まとめ/"
}
'
$ curl -XPUT 'http://localhost:9200/blogs/_doc/3?pretty' -H 'Content-Type: application/json' -d '
{
  "title": "生存時間解析について – 概要編 - LAPRAS AI LAB",
  "description": "scoutyの高濱です。本記事では、インターンの田村くんと協力してscoutyでの転職可能性予測ロジックに組み込んだ生存時間解析に関する基礎的な事項の説明を行います。 転職可能性予測は、こちらの記事の通り、候補者の現在の転職の可能性を推定して提示し、スカウトメールを送るか否かの判断を助けます。 生存時間解析は、予測ロジックのコンポーネントのひとつとして、経歴などの情報から候補者が現職を退職する時期（月単位）を予測するために利用されています。",
  "url": "https://ai-lab.lapras.com/ml/survival-time/"
}
'
```

</details>


## 参考文献

MQ

 - [FastAPIでRabbitMQを使ってみる - Qiita](https://qiita.com/satto_sann/items/ca3647662843e65530c7)
 - [pythonでrabbimqを扱う - Qiita](https://qiita.com/mink0212/items/8d692e17b34793655c66)
 - [RabbitMQ tutorial - "Hello world!" 
 — RabbitMQ](https://www.rabbitmq.com/tutorials/tutorial-one-python.html)
 - [python — Python and RabbitMQ-複数のチャネルからの消費イベントをリッスンする最良の方法？](https://www.it-mure.jp.net/ja/python/python-and-rabbitmq%E8%A4%87%E6%95%B0%E3%81%AE%E3%83%81%E3%83%A3%E3%83%8D%E3%83%AB%E3%81%8B%E3%82%89%E3%81%AE%E6%B6%88%E8%B2%BB%E3%82%A4%E3%83%99%E3%83%B3%E3%83%88%E3%82%92%E3%83%AA%E3%83%83%E3%82%B9%E3%83%B3%E3%81%99%E3%82%8B%E6%9C%80%E8%89%AF%E3%81%AE%E6%96%B9%E6%B3%95%EF%BC%9F/1051158256/)
 - [IDDD_Samples/ExchangeListener.java at 05d95572f2ad6b85357b216d7d617b27359a360d · VaughnVernon/IDDD_Samples](https://github.com/VaughnVernon/IDDD_Samples/blob/05d95572f2ad6b85357b216d7d617b27359a360d/iddd_common/src/main/java/com/saasovation/common/port/adapter/messaging/rabbitmq/ExchangeListener.java)

ElasticSearch

 - [Python Elasticsearch 基本的な使い方まとめ - Qiita](https://qiita.com/satto_sann/items/8a63761bbfd6542bb9a2)
 - [Elasticsearch > dockerで構築、Twitter情報を取得しKibanaで可視化 - Qiita](https://qiita.com/sugasaki/items/cbacfec3f488e907ded0)
 - [DockerコンテナでElasticSearchを起動する（docker-compose） - Qiita](https://qiita.com/hiroky_814/items/7a8ddddd472d47f6435b)
 - [はじめての Elasticsearch - Qiita](https://qiita.com/nskydiving/items/1c2dc4e0b9c98d164329)