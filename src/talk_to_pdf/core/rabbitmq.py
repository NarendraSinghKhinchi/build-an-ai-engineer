import aio_pika
import logging
from talk_to_pdf.core.config import settings

logger = logging.getLogger(__name__)

# This global variable will hold our single, long-lived connection
rabbitmq_connection: aio_pika.RobustConnection | None = None

async def connect_rabbitmq():
    """Called once when the FastAPI server starts."""
    global rabbitmq_connection
    rabbitmq_connection = await aio_pika.connect_robust(settings.rabbitmq_url)
    logger.info("Connected to RabbitMQ")

async def close_rabbitmq():
    """Called once when the FastAPI server shuts down."""
    global rabbitmq_connection
    if rabbitmq_connection:
        await rabbitmq_connection.close()
        logger.info("Closed RabbitMQ connection")

async def publish_message(queue_name: str, message_body: str):
    """Uses the existing global connection to publish a message."""
    if not rabbitmq_connection:
        logger.error("RabbitMQ connection is not established!")
        return

    try:
        # We DO NOT close the connection here. 
        # We only open a lightweight "channel", which we close after publishing using 'async with'
        async with rabbitmq_connection.channel() as channel:
            await channel.declare_queue(queue_name, durable=True)
            await channel.default_exchange.publish(
                aio_pika.Message(body=message_body.encode()),
                routing_key=queue_name
            )
            logger.info(f"Published message to {queue_name}: {message_body}")
    except Exception as e:
        logger.error(f"Failed to publish message: {e}")
