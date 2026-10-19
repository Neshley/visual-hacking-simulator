# 🖥️ System Update - Hacking Simulation (Version 2 — current)

> ⚠️ EDUCATIONAL SIMULATION — USE THIS VARIANT

This is the canonical Version 2 README. It documents the accurate runtime behavior and how to run or package the simulation.

Key points (accurate):
- The app is a local Tkinter GUI demo. It does not encrypt or delete user files, does not add persistence, and does not transmit data to remote servers.
- Some text in the UI shows example exploit scripts; those examples are stored as strings and are displayed only.
- The app looks up the local host IP with `socket.gethostbyname(socket.gethostname())` (to display a "real IP" string). This does not open remote connections in normal environments.
- Typing `neshley` while the app has focus triggers the cancellation sequence which clears the UI and exits.

Run & build (Version 2):

```bash
cd "Version 2"
python -m venv venv
# Activate the venv, then:
pip install -r requirements.txt
python hacker_sim.py
# Optional packaging
python build.py
```

If you distribute a built executable, include a short note that the program is a visual simulation and does not perform real attacks.

Safety reminder: run demos in disposable machines or VMs and inspect code before distribution.
