from flask import Flask, render_template
from livereload import Server

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return render_template('hello.html')


if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.watch('bulmaio_jinja2/templates/*')
    server.watch('bulmaio_jinja2/*')
    server.serve()
