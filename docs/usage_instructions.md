# Usage Instructions

## Purpose
The purpose of this project is to upload files to Dropbox and then send these files to the designated Alchemy API using credentials specified in the `.env` file.

## Environment Setup (Python)
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

## Environment Setup (Node.js)
1. Ensure you have Node.js and npm/pnpm installed on your machine.
2. Initialize your Node.js project:
   ```bash
   mkdir dropbox-alchemy-uploader
   cd dropbox-alchemy-uploader
   npm init -y
   ```
3. Install required dependencies:
   ```bash
   pnpm add dotenv dropbox axios express multer
   ```
4. Create the following file structure:
   ```
   dropbox-alchemy-uploader/
   ├── .env
   ├── app.js
   ├── package.json
   ├── uploads/
   └── logs/
   ```
5. Create a `.env` file and add the following keys:
   ```
   DROPBOX_ACCESS_TOKEN=your_dropbox_access_token
   ALCHEMY_API_KEY=your_alchemy_api_key
   ```

## Configuration
1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Fill in required credentials in the `.env` file:
   - `DROPBOX_ACCESS_TOKEN`: Your Dropbox access token.
   - `ALCHEMY_API_KEY`: Your Alchemy API key.
   - `CRYPTO_HOST_IP`: The IP address of your Crypto Host.
   - `ALCHEMY_ACCESS_KEY`: Your Alchemy access key.

## Running the Service (Python)
1. Ensure the virtual environment is activated:
   ```bash
   source venv/bin/activate  # Unix
   .\venv\Scripts\activate   # Windows
   ```
2. Execute the main script:
   ```bash
   python src/main.py
   ```

## Running the Service (Node.js)
1. Start the server:
   ```bash
   node app.js
   ```
2. Send a test file using an HTTP client:
   ```bash
   curl -X POST -F "file=@/path/to/your/file.txt" http://localhost:3000/upload
   ```

## Monitoring and Logs
- Check console output for operation status.
- Review API responses in logs located in the `logs` directory.
- Monitor transaction status via the Alchemy dashboard.

## Troubleshooting
- **Invalid Credentials**: Ensure that the credentials in the `.env` file are correct and have not expired.
- **Network Issues**: Verify that your network connection is stable and that the IP addresses and endpoints are reachable.
- **Dependency Errors**: Make sure all dependencies are installed correctly by running `pip install -r requirements.txt` again.
- **File Upload Issues**: Ensure the file paths specified are correct and that you have the necessary permissions to access them.
- **Missing Directories**: Ensure that the `uploads` and `logs` directories exist and have the correct permissions.
