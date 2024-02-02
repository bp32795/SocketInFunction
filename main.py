import os
from flask_socketio import SocketIO
from flask import Flask, render_template, request, jsonify, session

from forloop import forloop

application = Flask(__name__)
application.secret_key = os.urandom(24)
socketio = SocketIO(application, logger=True, engineio_logger=True)

@application.route('/', methods=['GET'])
def index():
    string = forloop(socketio)
    return render_template('index.html') # Press Ctrl+F8 to toggle the breakpoint.
# @socketio.on('progress')
# def send_message(data):
#     socketio.emit('progress',data)
#     print(f"emitted: {data}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    socketio.run(application, allow_unsafe_werkzeug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
