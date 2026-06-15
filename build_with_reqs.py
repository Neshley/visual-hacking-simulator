import os, sys, subprocess, shutil

def check_python():
    print("[*] Checking Python...")
    if sys.version_info < (3, 6):
        print("[ERROR] Python 3.6+ required!")
        sys.exit(1)
    print(f"[OK] Python {sys.version_info.major}.{sys.version_info.minor}")

def install_reqs():
    print("\n[*] Installing requirements...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyinstaller'])
    print("[OK] Done")

def build():
    print("\n[*] Building executable...")
    
    # Clean old builds
    for d in ['build', 'dist']:
        if os.path.exists(d):
            shutil.rmtree(d)
    
    # Build command
    cmd = [
        sys.executable, '-m', 'PyInstaller',
        '--onefile',
        '--windowed',
        '--name=SystemUpdate',
        '--clean',
        '--noconfirm',
        '--hidden-import=tkinter',
        '--hidden-import=_tkinter',
        '--hidden-import=tkinter.font',
        '--hidden-import=tkinter.scrolledtext',
        'hacker_sim.py'
    ]
    
    subprocess.check_call(cmd)
    
    if os.path.exists('dist/SystemUpdate.exe'):
        size = os.path.getsize('dist/SystemUpdate.exe') / (1024*1024)
        print(f"\n[SUCCESS] Built: dist/SystemUpdate.exe ({size:.1f} MB)")
    else:
        print("\n[ERROR] Build failed!")

if __name__ == "__main__":
    print("=" * 50)
    print("  Building SystemUpdate.exe")
    print("=" * 50)
    
    if not os.path.exists('hacker_sim.py'):
        print("[ERROR] hacker_sim.py not found in this folder!")
        print("Please run this script from the folder containing hacker_sim.py")
        sys.exit(1)
    
    check_python()
    install_reqs()
    build()
    
    print("\nDone! Your .exe is in the 'dist' folder.")
    input("Press Enter to exit...")