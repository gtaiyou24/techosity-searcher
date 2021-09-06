from typing import Optional, Set, List, Dict

from domain.model.blog import BlogRepository, Blog, BlogId


class InMemoryBlogRepository(BlogRepository):
    blogs = {
        BlogId("1"): Blog.of("1",
                             "新卒エンジニアがフルリモートで知識を吸収するためにモブプロを取り入れてみた話 - Yahoo! JAPAN Tech Blog",
                             "入社してからずっとリモートだった新卒が、モブプロの導入をチームに提案して取り組んだ話です。導入の結果、チームビルディングや知識の冗長化につながりました。",
                             "https://techblog.yahoo.co.jp/entry/2021083030177162/"),
        BlogId("2"): Blog.of("2",
                             "ヤフーがサポートするベクトル検索エンジンVald 〜 類似検索の最前線 - Yahoo! JAPAN Tech Blog",
                             "ヤフーがサポートするOSSベクトル検索エンジン「Vald」は類似画像検索などに活用されています。Valdの概要から活用事例までご紹介します！",
                             "https://techblog.yahoo.co.jp/entry/2021061430159867/"),
        BlogId("3"): Blog.of("3",
                             "ヤフオク!でユーザーが落札したいと感じる商品推薦の作り方 - Yahoo! JAPAN Tech Blog",
                             "二次流通ECレコメンデーションにおいて独自開発の多腕バンディット・アルゴリズムを利用し、ユーザーが落札したいと思う商品を推薦できるようにしました",
                             "https://techblog.yahoo.co.jp/entry/2021072030169734/"),
        BlogId("4"): Blog.of("4",
                             "Poincaré Embeddings による職種の類似度計算とその利用 - LAPRAS AI LAB",
                             'scouty アルゴリズムエンジニアの高濱です。外部への情報発信はこの記事が最初なのでこの場を借りて自己紹介させていただきますが、私は scouty 代表の島田、リードエンジニアの伊藤と京都大学工学部情報学科での同期で、京都大学大学院情報学研究科鹿島研究室で修士課程を修了した後、株式会社リクルートホールディングスを経て scouty に入社しました。代表的な著作物は [Takahama et al … "Poincaré Embeddings による職種の類似度計算とその利用" の続きを読む',
                             'https://ai-lab.lapras.com/nlp/poincare-embeddings/'),
        BlogId("5"): Blog.of("5",
                             "2019年現在の文・文書生成に関してのまとめ - LAPRAS AI LAB",
                             'LAPRAS の森元です。AI LAB でのはじめての投稿になります。私は、修士課程・博士課程を通して自然言語処理学の研究をしてきました。特に推論や因果関係に興味があり、主に含意関係認識の研究を行ってきています。先月4月よりリサーチャーとして LAPRAS に入社しました。 本記事は、2019年4月現在の文自動生成に関してのサーベイを行った結果をまとめたものです。 はじめに LAPRAS の提供し … "2019年現在の文・文書生成に関してのまとめ" の続きを読む',
                             "https://ai-lab.lapras.com/nlp/text-generation-2019/"),
        BlogId("6"): Blog.of("6",
                             "生存時間解析について - 概要編 - LAPRAS AI LAB",
                             'scoutyの高濱です。本記事では、インターンの田村くんと協力してscoutyでの転職可能性予測ロジックに組み込んだ生存時間解析に関する基礎的な事項の説明を行います。 転職可能性予測は、こちらの記事の通り、候補者の現在の転職の可能性を推定して提示し、スカウトメールを送るか否かの判断を助けます。 生存時間解析は、予測ロジックのコンポーネントのひとつとして、経歴などの情報から候補者が現職を退職する時期 … "生存時間解析について – 概要編" の続きを読む',
                             "https://ai-lab.lapras.com/ml/survival-time/")
    }

    def blog_of(self, id: BlogId) -> Optional[Blog]:
        return self.blogs.get(
            id,
            Blog.of(id.id, "title is {}".format(id.id), "description", "https://techblog.yahoo.co.jp/")
        )

    def blog_list_of(self, id_list: List[BlogId]) -> List[Blog]:
        return [self.blog_of(id) for id in id_list]
