# Usage Instructions

## Environment Setup
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Unix
   .\venv\Scripts\activate   # Windows
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
1. Copy `.env.example` to `.env`
2. Fill in required credentials:
   - DROPBOX_ACCESS_TOKEN
   - ALCHEMY_API_KEY
   - CRYPTO_HOST_IP
   - ALCHEMY_ACCESS_KEY

## Running the Service
1. Execute main script:
   ```bash
   python src/main.py
   ```

## Monitoring and Logs
- Check console output for operation status
- Review API responses in logs
- Monitor transaction status via Alchemy dashboard
