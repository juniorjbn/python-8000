from flask import Flask
import os
import socket
app = Flask(__name__)
host = socket.gethostname()

@app.route('/')
def hello():
    return '\nHello World!\nIm trying to find a better job.\nSee my Host name is changing by refreshing page %s\n\n' % (host)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("8000"), debug=True)
