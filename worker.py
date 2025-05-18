import asyncio
import aio_pika
import json
from tenacity import retry, stop_after_attempt, wait_fixed
from app.database import notifications_collection

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
async def save_notification(data):
    await notifications_collection.insert_one(data)
    print("✅ Notification saved:", data)

async def deliver_notification(data):
    if data["type"] == "email":
        print(" Sending email:", data["content"])
    elif data["type"] == "sms":
        print(" Sending SMS:", data["content"])
    elif data["type"] == "in-app":
        print(" In-app notification:", data["content"])
    else:
        raise ValueError("Unsupported notification type")

async def main():
    connection = await aio_pika.connect_robust("amqp://guest:guest@localhost/")
    channel = await connection.channel()
    queue = await channel.declare_queue("notifications", durable=True)

    async with queue.iterator() as queue_iter:
        async for message in queue_iter:
            async with message.process():
                data = json.loads(message.body)
                try:
                    await deliver_notification(data)
                    data["status"] = "sent"
                except Exception as e:
                    print(" Delivery failed:", e)
                    data["status"] = "failed"
                await save_notification(data)

if __name__ == "__main__":
    asyncio.run(main())
