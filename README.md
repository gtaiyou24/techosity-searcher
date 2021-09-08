# Techosity Search

## 起動方法
```bash
$ cd ~/path/to/techosity-searcher

$ cp ./searcher/.env.sample ./searcher/.env
$ cp ./elasticsearch/.env.sample ./elasticsearch/.env

$ docker-compose up --build
```

<details><summary>[ElasticSearch]インデックスの作成/データ投入</summary>

```bash
$ curl -XPUT 'http://localhost:9200/blogs'
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

ElasticSearchが起動したら、Flaskを起動します。
```bash
$ docker-compose run --rm -v `pwd`/searcher:/app/ -p 5000:5000 searcher python start_flask.py
```
[http://localhost:5000](http://localhost:5000)にアクセスするとページが表示されます
