var http = require('http');

http.createServer(function(request, response) {
  response.statusCode = 200;
  response.setHeader('Content-Type', 'text/plain');
  response.write("The following is what I got:\n");

  request.on('data', function(chunk) {
    response.write(chunk);
  }).on('end', function() {
    response.end("\nThat's all!");
  });
}).listen(8090);
