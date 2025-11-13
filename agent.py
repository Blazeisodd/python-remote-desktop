# agent.py - Remote Desktop Agent
# This runs on the computer you want to control
import socketio
import pyautogui
import mss
import base64
from io import BytesIO
from PIL import Image

# EDIT THIS: Change to your server IP (run ipconfig/ifconfig to find it)
SERVER_URL = 'http://localhost:5000'

sio = socketio.Client()
pyautogui.FAILSAFE = False

@sio.event
def connect():
    print('Connected to controller!')
    print(f'Agent ID: {sio.sid}')
    print('Share this ID with the controller')

@sio.event
def disconnect():
    print('Disconnected from controller')

@sio.on('request_screen')
def handle_screen_request():
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        screenshot = sct.grab(monitor)
        img = Image.frombytes('RGB', screenshot.size, screenshot.bgra, 'raw', 'BGRX')
        buffered = BytesIO()
        img.save(buffered, format='JPEG', quality=60)
        img_str = base64.b64encode(buffered.getvalue()).decode()
        sio.emit('screen_data', img_str)

@sio.on('mouse_move')
def handle_mouse_move(data):
    pyautogui.moveTo(data['x'], data['y'])

@sio.on('mouse_click')
def handle_mouse_click(data):
    button = data.get('button', 'left')
    pyautogui.click(button=button)

@sio.on('key_press')
def handle_key_press(data):
    key = data['key']
    pyautogui.press(key)

if __name__ == '__main__':
    try:
        print('Starting remote desktop agent...')
        print(f'Connecting to {SERVER_URL}')
        sio.connect(SERVER_URL)
        sio.wait()
    except KeyboardInterrupt:
        print('\nShutting down agent...')
        sio.disconnect()
    except Exception as e:
        print(f'Error: {e}')
        print('Make sure the server is running and SERVER_URL is correct')
