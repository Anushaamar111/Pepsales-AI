# queue.py
import aio_pika
import json

RABBITMQ_URL = "amqp://guest:guest@localhost/"

async def send_to_queue(notification_data):
    connection = await aio_pika.connect_robust(RABBITMQ_URL)
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue("notifications", durable=True)
        await channel.default_exchange.publish(
            aio_pika.Message(
                body=json.dumps(notification_data).encode(),
                delivery_mode=aio_pika.DeliveryMode.PERSISTENT,
            ),
            routing_key=queue.name,
        )
