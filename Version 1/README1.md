# 🖥️ System Update - Hacking Simulation (Version 1 — legacy)

> ⚠️ EDUCATIONAL SIMULATION — LEGACY COPY

This is the Version 1 copy of the hacking/ransomware visual simulation. It is kept for reference; Version 2/ contains the canonical, up-to-date implementation. Behavior is the same as described in the root README: these scripts are visual simulations and are not intended to perform real attacks.

Quick notes specific to Version 1:
- Entrypoint: `Version 1/hacker_sim.py` (reference)
- Build helper: `Version 1/build_with_reqs.py`
- Requirements: The app uses only Python standard library modules for core behavior (tkinter, time, random, sys, os). `pyinstaller` and `pillow` may be used for packaging/optional icons.

Run from this directory:

```bash
cd "Version 1"
python hacker_sim.py
```

Safety: do not run on production systems. Use a VM or disposable environment.
