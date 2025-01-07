from web3 import Web3
from dotenv import load_dotenv
import os
from dataclasses import dataclass
import logging
from typing import Optional

@dataclass
class AlchemyConfig:
    """Configuration for Alchemy connection."""
    api_key: str
    network: str = "mainnet"

    @property
    def endpoint(self) -> str:
        return f"https://eth-{self.network}.g.alchemy.com/v2/{self.api_key}"

    @classmethod
    def from_env(cls) -> 'AlchemyConfig':
        """Create configuration from environment variables."""
        load_dotenv()
        api_key = os.getenv("ALCHEMY_API_KEY")
        if not api_key:
            raise ValueError("ALCHEMY_API_KEY not found in environment variables")
        return cls(api_key=api_key)

class AlchemyClient:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.config = AlchemyConfig.from_env()
        self.web3: Optional[Web3] = None
        self.connect()

    def connect(self) -> None:
        """Establish connection to Alchemy."""
        try:
            self.web3 = Web3(Web3.HTTPProvider(self.config.endpoint))
            if not self.web3.isConnected():
                raise ConnectionError("Failed to connect to Alchemy")
            self.logger.info("Successfully connected to Alchemy")
        except Exception as e:
            self.logger.error(f"Failed to connect to Alchemy: {str(e)}")
            raise
