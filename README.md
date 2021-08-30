# Techosity Search

## 起動方法
```bash
$ cd ~/path/to/techosity-searcher
$ docker build -t techosity-searcher:latest .
$ docker img ls | grep techosity-searcher
$ docker container run --rm \
    --env-file=.env \
    -p 5000:5000 \
    -v `pwd`:/app/ \
    techosity-searcher:latest
```
[http://localhost:5000](http://localhost:5000)にアクセスするとページが表示されます
