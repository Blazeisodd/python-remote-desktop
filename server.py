# server.py - Controller Server
from flask import Flask, send_from_directory, request
from flask_socketio import SocketIO, emit
import socket

app = Flask(__name__, static_folder='public')
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return send_from_directory('public', 'client.html')

@socketio.on('connect')
def handle_connect():
    print(f'[+] Client connected: {request.sid}')

@socketio.on('agent_ready')
def handle_ready(data):
    print(f'[+] Agent ready - Screen: {data.get("screen_width")}x{data.get("screen_height")}')
    emit('agent_ready', data, broadcast=True)

@socketio.on('screenshot')
def handle_screenshot(data):
    emit('screenshot', data, broadcast=True)

@socketio.on('mouse_move')
def handle_mouse(data):
    emit('mouse_move', data, broadcast=True)

@socketio.on('mouse_click')
def handle_click(data):
    emit('mouse_click', data, broadcast=True)

@socketio.on('key_press')
def handle_key(data):
    emit('key_press', data, broadcast=True)

@socketio.on('type_text')
def handle_type(data):
    emit('type_text', data, broadcast=True)

@socketio.on('request_screenshot')
def handle_request():
    emit('request_screenshot', broadcast=True)

@socketio.on('start_streaming')
def handle_stream():
    emit('start_streaming', broadcast=True)

if __name__ == '__main__':
    ip = socket.gethostbyname(socket.gethostname())
    print('\n═══════════════════════════════════')
    print('  🎮 REMOTE CONTROL SERVER')
    print('═══════════════════════════════════')
    print(f'[*] Your IP: {ip}')
    print(f'[*] Control Panel: http://{ip}:5000')
    print('[*] Give RemoteAgent.exe to the other person')
    print('[*] Edit agent.py and change SERVER_URL to: http://{ip}:5000')
    print('═══════════════════════════════════\n')
    socketio.run(app, host='0.0.0.0', port=5000, debug=False)
