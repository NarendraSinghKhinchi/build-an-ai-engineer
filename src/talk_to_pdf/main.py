import logging
from fastapi import FastAPI 
from talk_to_pdf.core.config import settings

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.project_name,
    version=settings.version
)

@app.get("/health")
async def health_check():
    logger.info("Health check endpoint hit")
    return {"status": "healthy", "version":settings.version}