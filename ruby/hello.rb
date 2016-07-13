require 'rack'

app = proc do |env|
  ['200', {'Content-Type' => 'text/html'}, ['<p>Hello, Rack!</p>']]
end

Rack::Handler::WEBrick.run(app, :Port => 8090, :Host => '0.0.0.0')
