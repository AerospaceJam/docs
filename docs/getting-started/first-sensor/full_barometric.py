from flask import Flask, render_template
from flask_socketio import SocketIO
import random
# Added:
from bmp180 import BMP180

app = Flask(__name__)
socketio = SocketIO(app)

# Added:
bmp = BMP180()

@app.route('/')
def index():
    return render_template('index.html')

def background_thread():
    while True:
        socketio.sleep(1)
        # Added:
        barometricPressure = bmp.get_pressure()
        socketio.emit(
            'update_data',
            {
                'randomNumber': random.randint(1, 100),
                # Added:
                'barometricPressure': barometricPressure
            }
        )

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    socketio.start_background_task(target=background_thread)

def main():
    socketio.run(app, host='0.0.0.0', port=80)

if __name__ == '__main__':
    main()
