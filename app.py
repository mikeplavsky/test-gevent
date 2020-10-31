from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():

    import time
    time.sleep(1)

    return "Done!\n"
