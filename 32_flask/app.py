from flask import Flask
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

@app.route('/hello')
def hello():
    app.logger.info('Endpoint: /hello')
    return 'Hello, world!'

@app.route('/html')
def html():
    app.logger.info('Endpoint: /html')
    return 'index.html'

@app.route('/json')
def json():
    app.logger.info('Endpoint: /json')
    data = {
        'message': 'Hello, world!'
    }
    return data

if __name__ == '__main__':
    app.run(debug=True)
