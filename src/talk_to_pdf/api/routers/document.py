import uuid 
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status 
from sqlalchemy.ext.asyncio import AsyncSession

from talk_to_pdf.core.database import get_db
from talk_to_pdf.services.storage import storage_provider 
from talk_to_pdf.models.document import Document, DocumentStatus
from talk_to_pdf.core.rabbitmq import publish_message
from talk_to_pdf.core.constants import QUEUE_DOCUMENT_PROCESSING

router = APIRouter(prefix="/documents", tags=["Documents"])
MAX_FILE_SIZE = 10*1024*1024

@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db)
):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Only PDF files are allowed"
        )

    if file.size and file.size > MAX_FILE_SIZE:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "File is too large. Maximum file size is 10MB."
        )

    doc_id = uuid.uuid4()
    db_document = Document(
        id= doc_id,
        filename=file.filename,
        content_type=file.content_type,
        file_size=file.size or 0,
        storage_path="",
        status = DocumentStatus.PROCESSING
    )
    db.add(db_document)
    await db.flush()

    try:
        saved_path = await storage_provider.save_file(str(doc_id), file)
        db_document.storage_path = saved_path 
        await db.commit()

        # Send a job to the queue for the AI Engine to pick up
        await publish_message(
            queue_name=QUEUE_DOCUMENT_PROCESSING, 
            message_body=str(doc_id)
        )

        return {
            "message": "File uploaded successfully",
            "document_id": doc_id
        }
    except Exception as e:
        await db.rollback()
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = f"Failed to upload file: {str(e)}"
        )


    
    