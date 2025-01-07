require("dotenv").config();
const { uploadFileToDropbox } = require("./utils/dropboxHelper");
const axios = require("axios");
const express = require("express");
const multer = require("multer");
const fs = require("fs");
const path = require("path");

const app = express();
const upload = multer({ dest: "uploads/" });

const ALCHEMY_API_KEY = process.env.ALCHEMY_API_KEY;

app.post("/upload", upload.single("file"), async (req, res) => {
  const filePath = req.file.path;
  const fileName = req.file.originalname;

  try {
    // Upload file to Dropbox
    const dropboxResponse = await uploadFileToDropbox(filePath, fileName);

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

app.get("/", (req, res) => {
  res.send("Server is running");
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});