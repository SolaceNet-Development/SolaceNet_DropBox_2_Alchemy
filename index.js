const fs = require('fs');

// Load configuration
const config = JSON.parse(fs.readFileSync('config.json', 'utf8'));

// Access DropBox App Key and App Secret
const dropboxAppKey = config.dropbox.appKey;
const dropboxAppSecret = config.dropbox.appSecret;

// ...existing code...

// Example usage
console.log(`DropBox App Key: ${dropboxAppKey}`);
console.log(`DropBox App Secret: ${dropboxAppSecret}`);

// ...existing code...
