import time
from collections.abc import Callable
from typing import Any

import pika
import pika.exceptions


class MessagingClient:
    def __init__(
        self, host: str, retry_attempts: int = 5, retry_delay: float = 2.0
    ) -> None:
        self.host = host
        self.retry_attempts = retry_attempts
        self.retry_delay = retry_delay
        self._connect()

    def _connect(self):
        attempts = 0
        while attempts < self.retry_attempts:
            try:
                connection = pika.BlockingConnection(
                    pika.ConnectionParameters(self.host)
                )
                self.channel = connection.channel()
                return
            except pika.exceptions.AMQPConnectionError as e:
                attempts += 1
                print(
                    f"Connection failed: {e}. Retrying {attempts}/{self.retry_attempts}..."
                )
                time.sleep(self.retry_delay)
        raise Exception("Could not connect to RabbitMQ after retries.")

    def producer(
        self, exchange: str, routing_key: str, body: Any
    ):
        try:
            self.channel.exchange_declare(exchange=exchange, exchange_type="fanout")
            self.channel.basic_publish(
                exchange=exchange, routing_key=routing_key, body=body
            )
        except pika.exceptions.AMQPError as e:
            print(f"Failed to publish message: {e}")

    def consumer(self, queue: str, callback: Callable, exchange: str, routing_key: str):
        try:
            self.channel.exchange_declare(exchange=exchange, exchange_type="fanout")
            self.channel.queue_declare(queue=queue)
            self.channel.queue_bind(
                exchange=exchange, queue=queue, routing_key=routing_key
            )
            self.channel.basic_consume(
                queue=queue,
                auto_ack=False,
                on_message_callback=self._wrap_callback(callback),
            )
            print("Starting consumer...")
            self.channel.start_consuming()
        except pika.exceptions.AMQPError as e:
            print(f"Failed to consume messages: {e}")
            self._connect()

    def _wrap_callback(self, callback: Callable):
        def wrapped_callback(ch, method, properties, body):
            try:
                callback(ch, method, properties, body)
                ch.basic_ack(delivery_tag=method.delivery_tag)
            except Exception as e:
                print(f"Error processing message: {e}")
                ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)

        return wrapped_callback

    def __del__(self):
        try:
            self.channel.close()
        except AttributeError:
            pass
