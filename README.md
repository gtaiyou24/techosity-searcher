# Techosity Search

## 起動方法
```bash
$ cd ~/path/to/techosity-searcher

$ cp ./searcher/.env.sample ./searcher/.env
$ cp ./elasticsearch/.env.sample ./elasticsearch/.env

$ docker-compose up --build

$ docker-compose run --rm -v `pwd`/searcher:/app/ searcher python start_flask.py
```
[http://localhost:5000](http://localhost:5000)にアクセスするとページが表示されます
