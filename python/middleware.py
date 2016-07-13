from wsgiref.simple_server import make_server

def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['<p>Hello, WSGI!</p>']

class Middleware:
    def __init__(self, app):
        self.wrapped_app = app

    def __call__(self, environ, start_response):
        result = self.wrapped_app(environ, start_response)
        result.insert(0, '<h1>Middleware</h1>')
        return result

httpd = make_server('', 8070, Middleware(app))
httpd.serve_forever()
