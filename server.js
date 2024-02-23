// Route localhost:3000 to append to proper prism mock
const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();

// Forward all requests from /v2 to the Prism server
app.use('/v2', createProxyMiddleware({ target: 'http://127.0.0.1:4010', pathRewrite: { '^/v2': '' } }));

// Listen on port 3000 (you can choose any port)
app.listen(3000, () => {
  console.log(`Proxy server listening on http://localhost:3000/v2`);
});