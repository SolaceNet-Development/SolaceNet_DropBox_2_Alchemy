import os
import logging
from typing import Any, Dict, Optional
from pathlib import Path
import json
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def validate_file_path(file_path: str) -> bool:
    """
    Validate if a file path exists and is accessible.
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        bool: True if valid, False otherwise
    """
    try:
        return Path(file_path).exists()
    except Exception as e:
        logger.error(f"Error validating file path: {e}")
        return False

def ensure_directory_exists(directory_path: str) -> None:
    """
    Create directory if it doesn't exist.
    
    Args:
        directory_path (str): Path to directory
    """
    Path(directory_path).mkdir(parents=True, exist_ok=True)

def load_json_file(file_path: str) -> Optional[Dict[str, Any]]:
    """
    Load and parse JSON file.
    
    Args:
        file_path (str): Path to JSON file
        
    Returns:
        Optional[Dict]: Parsed JSON data or None if error occurs
    """
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Error loading JSON file: {e}")
        return None

def save_json_file(data: Dict[str, Any], file_path: str) -> bool:
    """
    Save data to JSON file.
    
    Args:
        data (Dict): Data to save
        file_path (str): Output file path
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except Exception as e:
        logger.error(f"Error saving JSON file: {e}")
        return False

def get_timestamp() -> str:
    """
    Get current timestamp in ISO format.
    
    Returns:
        str: Formatted timestamp
    """
    return datetime.now().isoformat()

def format_api_response(success: bool, data: Any = None, error: str = None) -> Dict[str, Any]:
    """
    Format API response in consistent structure.
    
    Args:
        success (bool): Operation success status
        data (Any, optional): Response data
        error (str, optional): Error message
        
    Returns:
        Dict: Formatted response
    """
    return {
        "success": success,
        "timestamp": get_timestamp(),
        "data": data,
        "error": error
    }

def validate_api_key(api_key: str) -> bool:
    """
    Validate API key format.
    
    Args:
        api_key (str): API key to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    return bool(api_key and len(api_key) >= 32)

def sanitize_filename(filename: str) -> str:
    """
    Sanitize filename for safe file system operations.
    
    Args:
        filename (str): Original filename
        
    Returns:
        str: Sanitized filename
    """
    return "".join(c for c in filename if c.isalnum() or c in "._- ").strip()
