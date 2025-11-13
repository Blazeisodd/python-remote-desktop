# 🖥️ Python Remote Desktop

Control any computer remotely through your browser! Send someone a single .EXE file and control their PC instantly.

## ✨ Features
- 🌐 Web-based controller (no software needed on your end)
- 🖱️ Full mouse and keyboard control
- 📺 Real-time screen streaming
- 📦 Single .EXE file for the remote computer
- 🚀 Super easy setup

## 🎯 Quick Start

### For the Controller (YOU):

1. **Clone and setup:**
```bash
git clone https://github.com/Blazeisodd/python-remote-desktop.git
cd python-remote-desktop
pip install -r requirements.txt
```

2. **Run your server:**
```bash
python server.py
```
You'll see your IP address (like `192.168.1.100`)

3. **Open browser:**
Go to `http://YOUR_IP:5000`

### For the Remote Computer (THEM):

**Option A: Run Python directly**
1. Edit `agent.py` line 8:
   - Change `SERVER_URL = 'http://YOUR_IP_HERE:5000'`
   - Put YOUR IP address there
2. Install requirements: `pip install -r requirements.txt`
3. Run: `python agent.py`

**Option B: Create single .EXE file (Recommended!)**

1. Edit `agent.py` first (put your IP on line 8)
2. Install PyInstaller:
```bash
pip install pyinstaller
```

3. Build the .EXE:
```bash
pyinstaller --onefile --noconsole --name RemoteAgent agent.py
```

4. **Send them `dist/RemoteAgent.exe`**
   - They just double-click it
   - That's it!

## 📁 Project Files

- `server.py` - Controller server (runs on YOUR computer)
- `agent.py` - Remote agent (runs on THEIR computer)
- `public/client.html` - Web control interface
- `requirements.txt` - Python dependencies

## 🚀 How It Works

```
Your PC (Controller)          Remote PC (Agent)
      |
      | 1. Run server.py
      | 2. Open http://localhost:5000
      |
      |------------------------>  3. Run RemoteAgent.exe
      |<------------------------  4. Agent connects
      |
      | 5. You see their screen!
      | 6. Control mouse/keyboard
      |------------------------>  7. Commands execute
```

## 🎮 Usage Tips

- **Start Stream**: Click to see their screen in real-time (10 FPS)
- **Mouse Control**: Move your mouse over the screen image
- **Click**: Left-click on the image to click on their PC
- **Right-click**: Right-click for context menus
- **Keyboard**: Type normally - it works!

## 🔧 Troubleshooting

**Can't connect?**
- Make sure both computers are on the same WiFi
- Check Windows Firewall (click "Allow" when asked)
- Make sure you put the right IP in agent.py

**How do I find my IP?**
- The server shows it when you run `python server.py`
- Or run: `ipconfig` (Windows) / `ifconfig` (Mac/Linux)

**Agent.exe flagged as virus?**
- PyInstaller .exes sometimes trigger false positives
- It's safe - you built it yourself!
- Add exclusion in Windows Defender if needed

## 🌐 Use Over Internet

To control computers outside your WiFi:

1. Install ngrok: https://ngrok.com
2. Run: `ngrok http 5000`
3. Use the ngrok URL in agent.py instead of your IP

## ⚠️ Important Notes

- No password protection by default (add your own!)
- Only for computers you have permission to access
- Works best on same WiFi network
- Requires Python 3.7+ installed

## 📝 License

MIT - Do whatever you want with it!

## 🤝 Contributing

Pull requests welcome! Feel free to improve this.
