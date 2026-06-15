
```markdown
# 🖥️ System Update - Hacking Simulation

> ⚠️ **EDUCATIONAL SIMULATION ONLY** - This software performs NO real hacking, does NOT encrypt files, and does NOT connect to any network. It is a visual simulation for educational/demonstration purposes.

---

## 📋 Table of Contents
- [Description](#description)
- [Features](#features)
- [Timeline](#timeline)
- [Installation](#installation)
- [Usage](#usage)
- [How to Exit](#how-to-exit)
- [Build from Source](#build-from-source)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Safety](#safety)
- [FAQ](#faq)
- [Screenshots](#screenshots)
- [Disclaimer](#disclaimer)

---

## 📖 Description

A dual-panel hacker interface simulation that creates a realistic-looking system breach scenario. Features a terminal with exploit scripts, hacking monitor with live logs, ransomware popup with countdown, fake Blue Screen of Death, and a security override system.

**Built with:** Python 3 + Tkinter (standard library)

---

## ✨ Features

### Main Interface
- 🔴 Fullscreen borderless window (no close/minimize/maximize buttons)
- 💻 Left panel: Fake Kali Linux terminal with scrolling exploit commands
- 📊 Right panel: Hacking monitor with live logs, progress bar, matrix rain
- 🎯 Red crosshair cursor tracking
- 📱 Fake Windows security toast notifications
- 🔄 Scanning progress animations throughout

### Ransomware Popup (appears after 60 seconds)
- 💀 "YOU HAVE BEEN HACKED" header with rotating threats
- 🔐 Files encrypted counter (continuously increasing)
- 💰 Rotating Bitcoin wallet addresses
- 🌐 Shows user's REAL local IP address
- ⏰ 3-minute countdown with dramatic effects
- ⛔ "DO NOT TURN OFF YOUR COMPUTER" warning
- 📁 "ALL YOUR FILES WILL BE PERMANENTLY LOST" warnings
- ❌ Close button runs away from mouse cursor
- 💳 Fake payment button (always rejected)

### Spy Window
- 👁️ "WATCHING YOU" with animated eye
- ⌨️ Keystroke counter
- 🖱️ Click counter
- 📁 Files encrypted counter
- ⚠️ Escape attempt tracker

### Blue Screen of Death (after countdown)
- 💙 Authentic Windows BSOD appearance
- 📜 40+ scrolling error codes
- 🔁 Cycles continuously forever
- 💡 Hidden "Override code required" hints
- 🔔 System tray notifications during BSOD
- 📊 Progress bar animation
- 🔄 Scanning animations

### Cancellation Sequence (on password entry)
- ✅ Emergency shutdown with typing effect
- 🔌 Terminating connections display
- 📤 Canceling data exfiltration
- 🔓 Decrypting files simulation
- 🧹 Removing malware
- 🛡️ Restoring system security
- ✨ Flashing completion messages

---

## ⏱️ Timeline

| Time | Event |
|------|-------|
| **0:00** | Main hacking interface launches fullscreen |
| **0:00 - 1:00** | Terminal commands, exploit scripts, logs, matrix rain |
| **1:00** | Ransomware popup appears with 3-minute countdown |
| **1:00 - 4:00** | Countdown runs, spy window tracks activity |
| **4:00** | Countdown reaches 00:00 |
| **4:03** | Fake BSOD appears with scrolling errors |
| **BSOD runs forever** | Until password is entered |
| **Anytime** | Type `neshley` for cancellation and exit |

### Countdown Effects
| Time Remaining | Effect |
|----------------|--------|
| 3:00 - 1:00 | Normal red countdown |
| 1:00 - 0:30 | Brighter red |
| 0:30 - 0:10 | Bold red, intense warnings |
| 0:10 - 0:00 | Flashing white/red (emergency) |

---

## 💿 Installation

### Option 1: Run Standalone Executable (Easiest)
1. Double-click `SystemUpdate.exe`
2. No Python installation required
3. Works on Windows 7/10/11

### Option 2: Install with Shortcuts
1. Right-click `install.bat` → Run as Administrator
2. Creates Desktop and Start Menu shortcuts
3. Installs to `C:\Program Files\SystemUpdate\`

### Option 3: Run from Source
```bash
# Clone or download the project
cd hacker_simulation

# Create virtual environment (optional)
python -m venv venv
venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Run
python hacker_sim.py
```

---

## 🎮 Usage

1. **Launch** the program
2. **Wait** 60 seconds for the ransomware popup
3. **Watch** the 3-minute countdown
4. **Type** `neshley` anywhere to cancel and exit

### Interactions
- **Move mouse**: Red crosshair follows cursor
- **Click anywhere**: Triggers alert in logs
- **Type anything**: Keystrokes are logged and counted
- **Hover close button**: Button runs away, warning appears
- **Click Pay button**: Shows "PAYMENT REJECTED"
- **Try to close popup**: Time penalty added (+45 seconds)

---

## 🔑 How to Exit

### Normal Exit
- **Type**: `neshley` (anywhere, anytime during the simulation)
- Shows cancellation sequence with decryption progress
- Cleanly exits after 5 seconds

### Force Quit (if stuck)
- **Windows**: `Win + D` → close terminal window
- **Task Manager**: `Ctrl + Alt + Delete` → End Python process
- **Alt+Tab**: Switch away, then close terminal

---

## 🔨 Build from Source

### Prerequisites
- Python 3.6 or higher
- Git (optional)

### Build Steps
```bash
# 1. Navigate to project folder
cd hacker_simulation

# 2. Run build script
python build.py
```

The build script will:
1. Check Python version
2. Create isolated virtual environment (`venv/`)
3. Install PyInstaller
4. Build standalone `SystemUpdate.exe`
5. Create `install.bat` for Windows
6. Package everything into `SystemUpdate_v1.0.zip`

### Manual Build
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name="SystemUpdate" hacker_sim.py
```

Output: `dist/SystemUpdate.exe`

---

## 📁 Project Structure

```
hacker_simulation/
│
├── hacker_sim.py              # Main source code
├── build.py                   # Build script (creates .exe)
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── install.bat                # Windows installer
│
├── venv/                      # Virtual environment (created by build)
│   ├── Scripts/
│   │   ├── python.exe
│   │   ├── pip.exe
│   │   └── activate.bat
│   └── Lib/
│
├── dist/                      # Output folder (created by build)
│   └── SystemUpdate.exe       # Standalone executable
│
├── build/                     # Temporary build files
│
└── SystemUpdate_v1.0.zip      # Distribution package
```

---

## 📋 Requirements

### Runtime (standalone .exe)
- **Windows 7/10/11** (64-bit recommended)
- **No Python required**
- **No internet required**
- **~15 MB disk space**

### Development (from source)
- **Python 3.6+**
- **Tkinter** (included with Python on Windows)
- **PyInstaller** (for building .exe)

### Python Imports Used
```python
import tkinter          # GUI framework (standard library)
from tkinter import font, scrolledtext, messagebox
import time             # Timing functions
import random           # Random generation
import sys, os          # System operations
import socket           # Get local IP only
from datetime import datetime
```

---

## 🛡️ Safety

### What This Program DOES
- ✅ Displays text and graphics on screen
- ✅ Shows your local network IP (192.168.x.x)
- ✅ Logs keystrokes to on-screen display only

### What This Program DOES NOT DO
| ❌ Does NOT | Details |
|-------------|---------|
| **Encrypt files** | Never touches any user files |
| **Delete data** | No files are deleted or modified |
| **Access internet** | No network connections made |
| **Steal information** | All data stays on your PC |
| **Install malware** | No software installed anywhere |
| **Modify registry** | Windows registry untouched |
| **Access webcam** | Webcam never activated |
| **Access microphone** | Microphone not used |
| **Affect boot sector** | Computer boots normally after |

### Verification
- Check Task Manager: Only one Python process
- No unusual network activity
- No new files outside project folder
- No startup entries added

---

## ❓ FAQ

**Q: Is this real malware?**
A: No. It's a Python Tkinter GUI that displays scary text and animations. Completely harmless.

**Q: Will it encrypt my files?**
A: No. The "Files encrypted" counter is just a number increasing in a variable.

**Q: Does it actually hack anything?**
A: No. All IP addresses are randomly generated. No real network connections.

**Q: Can I close it without the password?**
A: Yes. Use Task Manager (`Ctrl+Alt+Delete`) or close the terminal.

**Q: Why does it show my real IP?**
A: It shows your local network IP (192.168.x.x), which is useless to actual hackers.

**Q: Does it need internet?**
A: No. Works completely offline.

**Q: Can I run it on Mac/Linux?**
A: The .exe is Windows-only. Source code works on any OS with Python and Tkinter.

**Q: How do I share it?**
A: Send `SystemUpdate_v1.0.zip` or just `SystemUpdate.exe`

---

## 📸 Screenshots

### Main Interface
- Dual-panel layout
- Left: Terminal with exploit commands
- Right: Hacking monitor with logs
- Matrix rain effect
- Red crosshair cursor

### Ransomware Popup
- Fullscreen with red glow
- "YOU HAVE BEEN HACKED" header
- 3-minute countdown
- Bitcoin wallet addresses
- Real IP display
- File encryption counter
- DO NOT TURN OFF warning

### Spy Window
- Bottom-right corner
- Eye animation
- Activity monitoring
- Escape attempt counter

### Blue Screen of Death
- Authentic Windows BSOD
- Scrolling error codes
- Progress bar
- Hidden hints

### Cancellation Sequence
- Green-on-black terminal style
- Typing effect
- Decryption progress
- System restore confirmation

---

## ⚠️ Disclaimer

```
THIS SOFTWARE IS FOR EDUCATIONAL PURPOSES ONLY.

This program is a VISUAL SIMULATION designed to demonstrate
what a hacking/ransomware interface might look like. It does
NOT perform any actual hacking, does NOT encrypt files, does
NOT steal data, and does NOT connect to any external servers.

The author is not responsible for any misuse of this software.
Use only on your own computer or with explicit permission.

By using this software, you agree to use it responsibly and
only for educational/demonstration purposes.
```

---

## 📄 License

This project is provided for **educational purposes only**. 

---

## 👤 Author

Created for classroom demonstration and educational use.

---

## 🔗 Links

- [Python Download](https://www.python.org/downloads/)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [PyInstaller Documentation](https://pyinstaller.org/)

---

**Remember:** Type `neshley` to exit! 🔑

---
