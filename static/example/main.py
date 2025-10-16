from flask import Flask, render_template
from flask_socketio import SocketIO
import random
import time
from bmp180 import BMP180
from mpu6050 import mpu6050
from tfluna import TFLuna
import RPi.GPIO as GPIO # type: ignore

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key!'
socketio = SocketIO(app)

MOTOR_IN1_PIN = 12
MOTOR_IN2_PIN = 6

print("INFO: Initializing hardware...")
bmp = BMP180()
mpu = mpu6050(0x68)
luna = TFLuna()
luna.open()
luna.set_samp_rate(20)
GPIO.setmode(GPIO.BCM)
GPIO.setup([MOTOR_IN1_PIN, MOTOR_IN2_PIN], GPIO.OUT)

@app.route('/')
def index():
    return render_template('index.html')

def background_thread():
    while True:
        socketio.sleep(1)
        try:
            pressure = round(bmp.get_pressure() / 100.0, 2)
            accel = mpu.get_accel_data()
            gyro = mpu.get_gyro_data()
            distance, strength, temp = luna.read()

            data_payload = {
                'barometricPressure': pressure,
                'accelX': round(accel['x'], 2),
                'accelY': round(accel['y'], 2),
                'accelZ': round(accel['z'], 2),
                'gyroX': round(gyro['x'], 2),
                'gyroY': round(gyro['y'], 2),
                'gyroZ': round(gyro['z'], 2),
                'lidarDistance': round(distance * 100.0, 2)
            }
            socketio.emit('update_data', data_payload)

        except Exception as e:
            print(f"ERROR: Could not read from sensors: {e}")
            socketio.emit('update_data', {'error': str(e)})

@socketio.on('connect')
def handle_connect():
    print('INFO: Client connected.')
    socketio.start_background_task(target=background_thread)

@socketio.on('control_motor')
def handle_motor_control(message):
    """Handles motor control events from the client."""
    action = message.get('action')
    print(f"EVENT: Received 'control_motor' with action: '{action}'")
    if action == 'forward':
        GPIO.output([MOTOR_IN1_PIN, MOTOR_IN2_PIN], [GPIO.HIGH, GPIO.LOW])
    elif action == 'backward':
        GPIO.output([MOTOR_IN1_PIN, MOTOR_IN2_PIN], [GPIO.LOW, GPIO.HIGH])
    elif action == 'stop':
        GPIO.output([MOTOR_IN1_PIN, MOTOR_IN2_PIN], [GPIO.LOW, GPIO.LOW])
    else:
        print(f"WARNING: Unknown motor action '{action}'")

def main():
    print("INFO: Starting server on http://0.0.0.0:80")
    socketio.run(app, host='0.0.0.0', port=80, debug=True)

if __name__ == '__main__':
    try:
        main()
    finally:
        GPIO.cleanup()
        print("INFO: Server stopped and GPIO cleaned up.")