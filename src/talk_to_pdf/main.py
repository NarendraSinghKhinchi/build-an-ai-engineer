import logging
from fastapi import FastAPI 
from talk_to_pdf.core.config import settings
from talk_to_pdf.api.routers import document
from contextlib import asynccontextmanager
from talk_to_pdf.core.rabbitmq import connect_rabbitmq, close_rabbitmq

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# The code before 'yield' runs on startup. The code after runs on shutdown.
@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_rabbitmq()
    yield
    await close_rabbitmq()

# Add the lifespan parameter here!
app = FastAPI(
    title=settings.project_name,
    version=settings.version,
    lifespan=lifespan
)

app.include_router(document.router)

@app.get("/health")
async def health_check():
    logger.info("Health check endpoint hit")
    return {"status": "healthy", "version":settings.version}