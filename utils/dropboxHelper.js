const { Dropbox } = require("dropbox");
const fs = require("fs");

const dropbox = new Dropbox({ accessToken: process.env.DROPBOX_ACCESS_TOKEN });

const uploadFileToDropbox = async (filePath, fileName) => {
  const fileContents = fs.readFileSync(filePath);
  return dropbox.filesUpload({
    path: `/${fileName}`,
    contents: fileContents,
  });
};

module.exports = { uploadFileToDropbox };