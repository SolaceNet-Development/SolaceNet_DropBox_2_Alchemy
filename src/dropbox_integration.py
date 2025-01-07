import dropbox
from dropbox.exceptions import ApiError, AuthError
from dotenv import load_dotenv
import os
import pathlib
from typing import List
import logging
from functools import wraps
import time

class DropboxException(Exception):
    """Custom exception for Dropbox-related errors."""
    pass

def retry_on_error(max_retries: int = 3, delay: float = 1.0):
    """Decorator for retrying operations on failure."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (ApiError, AuthError) as e:
                    if attempt == max_retries - 1:
                        raise DropboxException(f"Operation failed after {max_retries} attempts: {str(e)}")
                    time.sleep(delay * (attempt + 1))
            return None
        return wrapper
    return decorator

load_dotenv()
DROPBOX_ACCESS_TOKEN = os.getenv("DROPBOX_ACCESS_TOKEN")

class DropboxClient:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.authenticate()

    def authenticate(self) -> None:
        """Initialize and authenticate Dropbox client."""
        if not DROPBOX_ACCESS_TOKEN:
            raise DropboxException("Dropbox access token not found in environment variables")
        try:
            self.dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)
            self.dbx.users_get_current_account()
            self.logger.info("Successfully authenticated with Dropbox")
        except AuthError as e:
            self.logger.error(f"Authentication failed: {str(e)}")
            raise DropboxException("Invalid Dropbox access token")

    @retry_on_error()
    def upload_to_dropbox(self, local_path: str, dropbox_path: str) -> None:
        """
        Upload a file to Dropbox.
        
        Args:
            local_path: Path to the local file
            dropbox_path: Destination path in Dropbox
        
        Raises:
            DropboxException: If upload fails
            FileNotFoundError: If local file doesn't exist
        """
        try:
            local_path = pathlib.Path(local_path)
            if not local_path.exists():
                raise FileNotFoundError(f"Local file not found: {local_path}")

            with open(local_path, 'rb') as f:
                self.dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode.overwrite)
            self.logger.info(f"Successfully uploaded {local_path} to {dropbox_path}")
        except ApiError as e:
            self.logger.error(f"Upload failed: {str(e)}")
            raise DropboxException(f"Upload failed: {str(e)}")

    @retry_on_error()
    def download_from_dropbox(self, dropbox_path: str, local_path: str) -> None:
        """
        Download a file from Dropbox.
        
        Args:
            dropbox_path: Path to the file in Dropbox
            local_path: Destination path on local filesystem
        
        Raises:
            DropboxException: If download fails
        """
        try:
            local_path = pathlib.Path(local_path)
            local_path.parent.mkdir(parents=True, exist_ok=True)
            
            self.dbx.files_download_to_file(str(local_path), dropbox_path)
            self.logger.info(f"Successfully downloaded {dropbox_path} to {local_path}")
        except ApiError as e:
            self.logger.error(f"Download failed: {str(e)}")
            raise DropboxException(f"Download failed: {str(e)}")

    @retry_on_error()
    def list_folder(self, folder_path: str) -> List[str]:
        """
        List contents of a Dropbox folder.
        
        Args:
            folder_path: Path to the folder in Dropbox
        
        Returns:
            List of file and folder names in the specified folder
        
        Raises:
            DropboxException: If listing fails
        """
        try:
            result = self.dbx.files_list_folder(folder_path)
            return [entry.name for entry in result.entries]
        except ApiError as e:
            self.logger.error(f"Listing folder failed: {str(e)}")
            raise DropboxException(f"Listing folder failed: {str(e)}")

    @retry_on_error()
    def delete_file(self, dropbox_path: str) -> None:
        """
        Delete a file from Dropbox.
        
        Args:
            dropbox_path: Path to the file in Dropbox
        
        Raises:
            DropboxException: If deletion fails
        """
        try:
            self.dbx.files_delete_v2(dropbox_path)
            self.logger.info(f"Successfully deleted {dropbox_path}")
        except ApiError as e:
            self.logger.error(f"Deletion failed: {str(e)}")
            raise DropboxException(f"Deletion failed: {str(e)}")
