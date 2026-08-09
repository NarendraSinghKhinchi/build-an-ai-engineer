import asyncio
import aio_pika
import logging
import sys
import os

# This allows our ai_engine to import models/configs from talk_to_pdf
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from talk_to_pdf.core.config import settings
from talk_to_pdf.core.constants import QUEUE_DOCUMENT_PROCESSING

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def process_message(message: aio_pika.IncomingMessage):
    """This function is called automatically a every time a message arrives in the queue."""
    async with message.process():
        document_id = message.body.decode()
        logger.info(f"Received job to process document: {document_id}")

        # TODO: write the pdf extraction logic here
        await asyncio.sleep(2)
        logger.info(f"Processed document: {document_id}")


async def main():
    """ Starts the worker and listens forever."""
    connection = await aio_pika.connect_robust(settings.rabbitmq_url)

    async with connection:
        channel = await connection.channel()

        await channel.set_qos(
            prefetch_count=1
        )

        queue = await channel.declare_queue(QUEUE_DOCUMENT_PROCESSING, durable=True)

        logger.info("Worker started. Waiting for messages...")

        await queue.consume(process_message)

        await asyncio.Future()
        

if __name__ == "__main__":
    asyncio.run(main())
        