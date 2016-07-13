class App
  def call(env)
    ['200', {'Content-Type' => 'text/html'}, ['<p>Hello, Rack!</p>']]
  end
end
