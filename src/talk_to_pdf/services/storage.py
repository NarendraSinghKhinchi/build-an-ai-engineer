import os
from abc import ABC, abstractmethod
from fastapi import UploadFile

# The abstract interface that defines the contract
class StorageProvider(ABC):
    @abstractmethod
    async def save_file(self, file_id: str, file: UploadFile) -> str:
        """Saves a file and returns the storage path."""
        pass

# The concrete implementation for local development
class LocalStorageProvider(StorageProvider):
    def __init__(self, base_dir: str = "upload_data"):
        self.base_dir = base_dir
        # Ensure the upload directory exists when the app starts
        os.makedirs(self.base_dir, exist_ok=True)

    async def save_file(self, file_id: str, file: UploadFile) -> str:
        # We rename the file to match the database UUID. 
        # This prevents collisions if two users upload "document.pdf"
        extension = os.path.splitext(file.filename)[1] if file.filename else ""
        filename = f"{file_id}{extension}"
        file_path = os.path.join(self.base_dir, filename)
        
        # Read and write asynchronously in 1MB chunks 
        # This prevents crashing if someone uploads a 500MB PDF!
        with open(file_path, "wb") as buffer:
            while chunk := await file.read(1024 * 1024):
                buffer.write(chunk)
                
        return file_path

# We instantiate this here. In a more advanced setup, we would use Dependency Injection.
storage_provider = LocalStorageProvider()
