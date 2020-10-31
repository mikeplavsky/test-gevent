from flask import Flask
from gevent.pywsgi import WSGIServer 

from gevent import monkey, sleep
from gevent.pool import Pool

monkey.patch_all()

app = Flask(__name__)

@app.route('/')
def index():

    sleep(1)
    return "Done!\n"

wsgi = WSGIServer(
        ('0.0.0.0',5000), 
        app, 
        spawn=Pool(1000))

wsgi.serve_forever()
