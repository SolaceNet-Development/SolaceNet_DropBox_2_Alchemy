# API Documentation

## Dropbox Integration
This section covers the integration with Dropbox, including authentication and file upload processes.

## Endpoints

### Dropbox API
- **Upload File**: `POST /dropbox/upload`
  - Description: Uploads a file to Dropbox.
  - Parameters:
    - `file`: The file to be uploaded (multipart/form-data).
    - `path`: The destination path in Dropbox (string).
  - Request Example:
    ```bash
    curl -X POST https://api.example.com/dropbox/upload \
      -F "file=@/path/to/your/file.txt" \
      -F "path=/destination/path/in/dropbox"
    ```
  - Response Example:
    ```json
    {
      "success": true,
      "file_id": "id:examplefileid"
    }
    ```

### Alchemy API
- **Send File**: `POST /alchemy/send`
  - Description: Sends a file from Dropbox to the Alchemy API.
  - Parameters:
    - `file_id`: The ID of the file in Dropbox (string).
    - `destination`: The destination endpoint in Alchemy (string).
  - Request Example:
    ```bash
    curl -X POST https://api.example.com/alchemy/send \
      -d '{"file_id": "id:examplefileid", "destination": "alchemy/endpoint"}' \
      -H "Content-Type: application/json"
    ```
  - Response Example:
    ```json
    {
      "success": true,
      "transaction_id": "exampletransactionid"
    }
    ```

### Crypto Host Interface
- **Get Transaction Status**: `GET /crypto/status`
  - Description: Retrieves the status of a transaction from the Crypto Host.
  - Parameters:
    - `transaction_id`: The ID of the transaction (string).
  - Request Example:
    ```bash
    curl -X GET "https://api.example.com/crypto/status?transaction_id=exampletransactionid"
    ```
  - Response Example:
    ```json
    {
      "status": "completed",
      "details": {
        "timestamp": "2023-10-01T12:00:00Z",
        "amount": "1000",
        "currency": "ETH"
      }
    }
    ```
