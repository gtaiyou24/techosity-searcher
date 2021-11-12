from typing import NoReturn

import pika
from injector import inject, singleton

from application.blog import BlogApplicationService
from application.blog.command import SaveBlogCommand
from logger import log
from port.adapter.messaging import ExchangeListener


@singleton
class RabbitMQBlogSavedListener(ExchangeListener):

    @inject
    def __init__(self, blog_application_service: BlogApplicationService):
        self.__blog_application_service = blog_application_service

        # TODO : 以下の処理をクラスに切り分けられないか
        log.debug("Connecting to server ...")
        # RabbitMQサーバと接続
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host="rabbitmq", port=5672, virtual_host='/', credentials=pika.PlainCredentials('guest', 'guest')))
        # チャンネルの確立
        channel = connection.channel()
        # キューに接続
        channel.queue_declare(queue=self.queue_name(), durable=True)

        # コンシューマの登録
        def callback(channel, method, properties, body):
            log.debug(f"Received {body}")
            message = body.decode()
            self.filtered_dispatch(message)
            log.debug("Done")
            # 受信したことをキューに知らせる
            channel.basic_ack(delivery_tag=method.delivery_tag)

        channel.basic_consume(queue=self.queue_name(), on_message_callback=callback)

        try:
            log.debug("Waiting for messages. To exit press Ctrl+C")
            channel.start_consuming()
        except KeyboardInterrupt:
            log.debug("Done")

    def queue_name(self) -> str:
        return "blogs.save"

    def filtered_dispatch(self, text_message: str) -> NoReturn:
        """受信したメッセージを処理する"""
        log.debug("メッセージを受信しました！")
        json: dict = eval(text_message)
        self.__blog_application_service.save(
            SaveBlogCommand(json['id'], json['title'], json['description'], json['url']))
