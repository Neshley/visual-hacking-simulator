# 🖥️ System Update - Hacking Simulation (Version 2 — canonical)

> ⚠️ EDUCATIONAL SIMULATION — READ THIS FIRST

This repository contains a visual hacking/ransomware simulation implemented in Python + Tkinter for classroom and demonstration use only. The program displays a dual-panel "hacker" interface, a dramatic ransomware popup, a small "spy" window, and a fake Blue Screen of Death. It is intended to **simulate** the appearance and behavior of an attack for demonstration; it is not malware.

## Important runtime behavior (accurate)
- The packaged application is a local Tkinter GUI. It does not perform file encryption, does not install persistence, and does not modify the Windows registry or boot sector.
- The application displays sample exploit scripts and text that look like real attack code; those examples are stored as strings and are displayed in the UI — they are not executed by the application.
- The app obtains a local hostname/IP using socket.gethostbyname(socket.gethostname()) (Version 2) to show the "real IP" label. That call performs a local hostname lookup; it does not open a remote network connection. In atypical DNS configurations this can resolve externally — run in a controlled environment if you have concerns.
- The UI logs keystrokes only to on-screen widgets (the app appends typed characters to GUI text widgets). The program does not write a separate logfile or transmit keystrokes anywhere.
- No network sockets are created by the normal app flow. The only network-related code in the repository is either:
  - calls used to look up the local host IP (safe/local), or
  - string literals containing example exploit scripts (inert, displayed as text).

## What changed and where to run
- Version 2/ is the canonical, actively maintained variant. Use `Version 2/hacker_sim.py` as the primary entrypoint.
- Version 1/ is an earlier variant kept for reference; it contains a similar `hacker_sim.py` and README.

## Build & Run (from source)
1. Create and activate a Python virtual environment (recommended):

```bash
cd "Version 2"
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
# source venv/bin/activate
```

2. Install build tools if you plan to make an .exe (optional):

```bash
pip install -r requirements.txt
```

3. Run the simulation directly (no build required):

```bash
python hacker_sim.py
```

4. To create a Windows executable (optional):

```bash
# from Version 2/
python build.py
# or use pyinstaller directly:
pyinstaller --onefile --windowed --name="SystemUpdate" hacker_sim.py
```

## Files and structure
```
README.md (this file)
Version 1/          # legacy reference variant
  hacker_sim.py     # older variant
  README1.md
Version 2/          # canonical variant (use this)
  hacker_sim.py     # current entrypoint
  build.py          # helper for packaging (pyinstaller)
  install.bat       # optional Windows installer script (packaging output)
  requirements.txt
```

## Safety notes (please read)
- Do not run this on production machines or machines containing critical personal data. Use a disposable machine or VM if you want to demo the UI.
- Inspect the code before building/distributing binaries. While the repository is intended as simulation-only, it contains strings and comments that resemble real attack commands; those are inert unless you deliberately copy them into executable code.
- If you package and distribute an .exe, verify what the build pipeline includes; do not commit a built binary to source control unless you intend to distribute it.

## How to exit during the demo
- Typing the escape word `neshley` anywhere while the app has focus will run the cancellation sequence and exit the program cleanly.
- If the GUI becomes unresponsive, force-quit the Python process via Task Manager (Windows) or kill the process on other OSes.

## License & attribution
Provided for educational/demonstration use only. See repository LICENSE (or contact the author) for reuse policies.

---

_Type `neshley` to exit the demo when running._
