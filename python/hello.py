from wsgiref.simple_server import make_server

def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['<p>Hello, WSGI!</p>']

httpd = make_server('', 8070, app)
httpd.serve_forever()
