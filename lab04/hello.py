import socket
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from container: ' + socket.gethostname()

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')