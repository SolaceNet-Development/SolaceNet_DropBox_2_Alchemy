# SolaceNet DropBox API Integration

## Overview
Integration between Dropbox API and blockchain services using Alchemy.

## Setup
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create `.env` file with required credentials:
   ```
   DROPBOX_ACCESS_TOKEN=your_token
   ALCHEMY_API_KEY=your_key
   CRYPTO_HOST_IP=your_host
   ```

## Usage
Run the main script:

# Dropbox to Alchemy Uploader

## Prerequisites

Ensure you have:
- Node.js and npm/pnpm installed on your machine.
- A Dropbox API key and Alchemy API key.
- A .env file in the root directory of your project to store sensitive credentials.
- An account on Dropbox and Alchemy (if not already registered).

## Setting Up Your Project

### Node.js Version

1. Initialize your Node.js project:

```bash
mkdir dropbox-alchemy-uploader
cd dropbox-alchemy-uploader
npm init -y
```

2. Install required dependencies:

```bash
pnpm add dotenv dropbox axios express multer
```

3. Create the following file structure:

```
dropbox-alchemy-uploader/
├── .env
├── app.js
├── package.json
└── uploads/
```

4. Create a .env file and add the following keys:

```
DROPBOX_ACCESS_TOKEN=your_dropbox_access_token
ALCHEMY_API_KEY=your_alchemy_api_key
```

## Building the File Upload Application

### Node.js Version

1. Configure Dropbox API integration:
- In the app.js file, set up the Dropbox SDK:

```javascript
require("dotenv").config();
const { Dropbox } = require("dropbox");
const axios = require("axios");
const express = require("express");
const multer = require("multer");
const fs = require("fs");
const path = require("path");

const app = express();
const upload = multer({ dest: "uploads/" });

const dropbox = new Dropbox({
  accessToken: process.env.DROPBOX_ACCESS_TOKEN,
});

const ALCHEMY_API_KEY = process.env.ALCHEMY_API_KEY;
```

2. Set up the upload endpoint:
- Add an API route to handle file uploads:

```javascript
app.post("/upload", upload.single("file"), async (req, res) => {
  const filePath = req.file.path;
  const fileName = req.file.originalname;

  try {
    // Upload file to Dropbox
    const dropboxResponse = await dropbox.filesUpload({
      path: `/${fileName}`,
      contents: fs.readFileSync(filePath),
    });

    console.log("Uploaded to Dropbox:", dropboxResponse);

    // Send the file information to Alchemy API
    const alchemyResponse = await axios.post(
      `https://api.alchemyapi.io/v2/${ALCHEMY_API_KEY}`,
      {
        dropboxFilePath: dropboxResponse.result.path_display,
      }
    );

    console.log("Sent to Alchemy:", alchemyResponse.data);

    res.status(200).send({
      message: "File uploaded to Dropbox and sent to Alchemy API",
      dropboxPath: dropboxResponse.result.path_display,
      alchemyResponse: alchemyResponse.data,
    });
  } catch (error) {
    console.error(error);
    res.status(500).send({ error: "An error occurred" });
  } finally {
    // Clean up temporary file
    fs.unlinkSync(filePath);
  }
});
```

3. Add a default route:
- To test server functionality, add a simple health check route:

```javascript
app.get("/", (req, res) => {
  res.send("Server is running");
});
```

4. Start the Express server:
- Add the following to app.js:

```javascript
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
```

## Testing the Application

1. Start the server:

```bash
node app.js
```

2. Send a test file using an HTTP client:
- Use tools like Postman or cURL to send a file to the /upload endpoint:

```bash
curl -X POST -F "file=@/path/to/your/file.txt" http://localhost:3000/upload
```

3. Verify the responses:
- Confirm the file appears in your Dropbox folder.
- Check the data was successfully sent to the Alchemy API.

## Documentation Sources

- Dropbox API Docs: https://www.dropbox.com/developers/documentation
- Alchemy API Docs: https://docs.alchemy.com/
- Multer for File Uploads: https://github.com/expressjs/multer
- Axios for HTTP Requests: https://axios-http.com/docs/intro

## Key Knowledge Points

- Dropbox Integration: Use the dropbox.filesUpload method to send files directly to Dropbox.
- Alchemy API Requests: Properly format the data for POST requests and authenticate using the API key.
- File Handling: Use Multer to handle file uploads and manage temporary files with fs.
- Environment Variables: Store API keys and sensitive information securely using the .env file and the dotenv library.
