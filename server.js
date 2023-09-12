const http = require('http');
const fs = require('fs');

// Create a server
const server = http.createServer((req, res) => {
  // Serve the static HTML page
  if (req.url === '/') {
    fs.readFile('index.html', 'utf8', (err, data) => {
      if (err) {
        res.writeHead(404);
        res.end('File not found.');
      } else {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(data);
      }
    });
  }
  // Handle data from ESP8266
  else if (req.url === '/data' && req.method === 'POST') {
    let body = '';
    req.on('data', (chunk) => {
      body += chunk;
    });

    req.on('end', () => {
      // Parse the JSON data sent by the ESP8266
      const data = JSON.parse(body);
      
      // Process the data (you can store it in a database or perform any required actions)
      console.log('Received data from ESP8266:');
      console.log(data);

      // Send a response to the ESP8266
      res.writeHead(200, { 'Content-Type': 'text/plain' });
      res.end('Data received.');
    });
  }
  // Handle other routes
  else {
    res.writeHead(404);
    res.end('Not Found.');
  }
});

// Listen on port 3000
server.listen(3000, () => {
  console.log('Server is running on port 3000');
});
