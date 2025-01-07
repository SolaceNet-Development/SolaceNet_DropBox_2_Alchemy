import requests
from dotenv import load_dotenv
import os
from typing import Tuple
import logging
from dataclasses import dataclass
from requests.exceptions import RequestException

@dataclass
class CryptoHostConfig:
    """Configuration for crypto host connection."""
    host_ip: str
    access_key: str

    @classmethod
    def from_env(cls) -> 'CryptoHostConfig':
        """Create configuration from environment variables."""
        load_dotenv()
        host_ip = os.getenv("CRYPTO_HOST_IP")
        access_key = os.getenv("ALCHEMY_ACCESS_KEY")
        
        if not all([host_ip, access_key]):
            raise ValueError("Missing required environment variables")
        
        return cls(host_ip=host_ip, access_key=access_key)

class CryptoHostClient:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.config = CryptoHostConfig.from_env()

    def send_to_crypto_host(self, file_path: str) -> Tuple[int, str]:
        """
        Send file to crypto host.
        
        Args:
            file_path: Path to the file to be sent
            
        Returns:
            Tuple of (status_code, response_text)
            
        Raises:
            FileNotFoundError: If file doesn't exist
            RequestException: If request fails
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        try:
            with open(file_path, 'rb') as f:
                response = requests.post(
                    f"http://{self.config.host_ip}/upload",
                    headers={"Authorization": f"Bearer {self.config.access_key}"},
                    files={"file": f},
                    timeout=30
                )
            response.raise_for_status()
            self.logger.info(f"Successfully sent file to crypto host: {file_path}")
            return response.status_code, response.text
        except RequestException as e:
            self.logger.error(f"Failed to send file: {str(e)}")
            raise
