class Middleware
  def initialize(app)
    @app = app
  end

  def call(env)
    status, headers, body = @app.call(env)
    body.each {|line| line.upcase! }
    return [status, headers, body]
  end
end
