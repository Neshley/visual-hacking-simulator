#!/usr/bin/env python3
"""
Build Script for System Update
Creates standalone executable with virtual environment
"""

import os
import sys
import subprocess
import shutil
import venv

def check_python():
    """Verify Python version"""
    print("[*] Checking Python version...")
    if sys.version_info < (3, 6):
        print("[ERROR] Python 3.6 or higher required!")
        input("Press Enter to exit...")
        sys.exit(1)
    print(f"[OK] Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")

def create_virtual_environment():
    """Create isolated Python environment"""
    print("\n[*] Creating virtual environment...")
    
    venv_path = os.path.join(os.getcwd(), 'venv')
    
    if os.path.exists(venv_path):
        print("[*] Removing old virtual environment...")
        try:
            shutil.rmtree(venv_path)
        except:
            print("[WARNING] Could not remove old venv, continuing...")
    
    try:
        venv.create(venv_path, with_pip=True)
        print(f"[OK] Virtual environment created: venv")
    except Exception as e:
        print(f"[ERROR] Failed to create venv: {e}")
        sys.exit(1)
    
    # Get paths
    if sys.platform == 'win32':
        python_path = os.path.join(venv_path, 'Scripts', 'python.exe')
        pip_path = os.path.join(venv_path, 'Scripts', 'pip.exe')
    else:
        python_path = os.path.join(venv_path, 'bin', 'python')
        pip_path = os.path.join(venv_path, 'bin', 'pip')
    
    return venv_path, python_path, pip_path

def install_pyinstaller(python_path, pip_path):
    """Install PyInstaller directly"""
    print("\n[*] Installing PyInstaller...")
    
    try:
        # Try to upgrade pip first (ignore errors)
        print("  Upgrading pip...")
        subprocess.run([python_path, '-m', 'pip', 'install', '--upgrade', 'pip'],
                      capture_output=True, timeout=30)
        print("  Done")
    except:
        print("  Skipping pip upgrade (continuing anyway)")
    
    try:
        # Install PyInstaller directly
        print("  Installing PyInstaller...")
        subprocess.check_call([python_path, '-m', 'pip', 'install', 'pyinstaller'],
                             timeout=120)
        print("[OK] PyInstaller installed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[WARNING] Venv install failed, trying system install...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyinstaller'],
                                 timeout=120)
            print("[OK] PyInstaller installed globally")
            return True
        except:
            print("[ERROR] Failed to install PyInstaller")
            return False

def build_executable(python_path):
    """Build standalone .exe"""
    print("\n[*] Building executable...")
    
    # Check for source file
    if not os.path.exists('hacker_sim.py'):
        print("[ERROR] hacker_sim.py not found!")
        files = os.listdir('.')
        print(f"Files here: {files}")
        return False
    
    # Clean old builds
    for folder in ['build', 'dist']:
        if os.path.exists(folder):
            try:
                shutil.rmtree(folder)
                print(f"  Cleaned: {folder}")
            except:
                print(f"  Could not clean: {folder}")
    
    # Remove old spec files
    for f in os.listdir('.'):
        if f.endswith('.spec'):
            try:
                os.remove(f)
            except:
                pass
    
    print("  Running PyInstaller (this may take 1-2 minutes)...")
    
    # Try building with venv python
    cmd = [
        python_path, '-m', 'PyInstaller',
        '--onefile',
        '--windowed',
        '--name=SystemUpdate',
        '--clean',
        '--noconfirm',
        '--hidden-import=tkinter',
        '--hidden-import=_tkinter',
        '--hidden-import=tkinter.font',
        '--hidden-import=tkinter.scrolledtext',
        '--hidden-import=tkinter.messagebox',
        '--hidden-import=socket',
        'hacker_sim.py'
    ]
    
    try:
        subprocess.check_call(cmd, timeout=300)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        print("[WARNING] Venv build failed, trying with system Python...")
        cmd[0] = sys.executable  # Use system Python instead
        try:
            subprocess.check_call(cmd, timeout=300)
        except:
            print("[ERROR] Build failed!")
            return False
    
    # Verify output
    exe_path = os.path.join('dist', 'SystemUpdate.exe')
    if os.path.exists(exe_path):
        size = os.path.getsize(exe_path) / (1024 * 1024)
        print(f"\n[SUCCESS] Build complete!")
        print(f"  File: SystemUpdate.exe")
        print(f"  Size: {size:.1f} MB")
        print(f"  Location: {os.path.abspath(exe_path)}")
        return True
    else:
        print("[ERROR] Build failed - executable not created!")
        return False

def create_installer_bat():
    """Create Windows installer batch file"""
    print("\n[*] Creating installer...")
    
    installer = """@echo off
title System Update - Installation
color 0A
echo ==========================================
echo   System Update - Installation
echo ==========================================
echo.

net session >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARNING] Run as Administrator for best results
    echo.
    timeout /t 2 >nul
)

echo [*] Installing System Update...
if not exist "%ProgramFiles%\\SystemUpdate" mkdir "%ProgramFiles%\\SystemUpdate"
copy /Y "%~dp0SystemUpdate.exe" "%ProgramFiles%\\SystemUpdate\\" >nul 2>&1

if %errorlevel% neq 0 (
    echo [ERROR] Failed to copy files
    pause
    exit /b 1
)

echo [*] Creating Desktop shortcut...
powershell -Command "$WS = New-Object -ComObject WScript.Shell; $SC = $WS.CreateShortcut('%USERPROFILE%\\Desktop\\SystemUpdate.lnk'); $SC.TargetPath = '%ProgramFiles%\\SystemUpdate\\SystemUpdate.exe'; $SC.WorkingDirectory = '%ProgramFiles%\\SystemUpdate'; $SC.Save()" >nul 2>&1

echo [*] Creating Start Menu shortcut...
powershell -Command "$WS = New-Object -ComObject WScript.Shell; $SM = [Environment]::GetFolderPath('Programs'); $SC = $WS.CreateShortcut($SM + '\\SystemUpdate.lnk'); $SC.TargetPath = '%ProgramFiles%\\SystemUpdate\\SystemUpdate.exe'; $SC.WorkingDirectory = '%ProgramFiles%\\SystemUpdate'; $SC.Save()" >nul 2>&1

echo.
echo ==========================================
echo   Installation Complete!
echo ==========================================
echo.
echo Installed to: %ProgramFiles%\\SystemUpdate\\
echo.
echo Shortcuts on Desktop and Start Menu
echo.
pause
"""
    
    with open('install.bat', 'w') as f:
        f.write(installer)
    
    print("[OK] install.bat created")

def create_readme():
    """Create README file"""
    print("\n[*] Creating README...")
    
    readme = """# System Update

## Quick Start
Double-click SystemUpdate.exe

## To Exit
Type: neshley (anywhere in the window)

## Force Quit
Win+D to show desktop, then close terminal
OR Ctrl+Alt+Delete > Task Manager > End Python

## Note
This is an educational simulation. No real hacking occurs.
"""
    
    with open('README.txt', 'w') as f:
        f.write(readme)
    
    print("[OK] README.txt created")

def create_zip():
    """Create distribution ZIP"""
    print("\n[*] Creating distribution package...")
    
    import zipfile
    
    zip_name = "SystemUpdate_v1.0.zip"
    
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zf:
        if os.path.exists('dist/SystemUpdate.exe'):
            zf.write('dist/SystemUpdate.exe', 'SystemUpdate.exe')
            print("  + Added: SystemUpdate.exe")
        if os.path.exists('install.bat'):
            zf.write('install.bat', 'install.bat')
            print("  + Added: install.bat")
        if os.path.exists('README.txt'):
            zf.write('README.txt', 'README.txt')
            print("  + Added: README.txt")
        if os.path.exists('hacker_sim.py'):
            zf.write('hacker_sim.py', 'hacker_sim.py')
            print("  + Added: hacker_sim.py (source)")
    
    if os.path.exists(zip_name):
        size = os.path.getsize(zip_name) / (1024 * 1024)
        print(f"\n[OK] Package created: {zip_name} ({size:.1f} MB)")
    else:
        print("[ERROR] Failed to create ZIP")

def main():
    print("=" * 55)
    print("  SYSTEM UPDATE - BUILD SYSTEM")
    print("=" * 55)
    print()
    
    try:
        # Step 1: Check Python
        check_python()
        
        # Step 2: Create venv
        venv_path, python_path, pip_path = create_virtual_environment()
        
        # Step 3: Install PyInstaller
        if not install_pyinstaller(python_path, pip_path):
            print("\n[ERROR] Could not install PyInstaller!")
            print("Please run manually: pip install pyinstaller")
            input("Press Enter to exit...")
            sys.exit(1)
        
        # Step 4: Build executable
        success = build_executable(python_path)
        
        if not success:
            print("\n[ERROR] Build failed!")
            input("Press Enter to exit...")
            sys.exit(1)
        
        # Step 5: Create installer
        create_installer_bat()
        
        # Step 6: Create README
        create_readme()
        
        # Step 7: Create ZIP
        create_zip()
        
        print("\n" + "=" * 55)
        print("  BUILD COMPLETE!")
        print("=" * 55)
        print(f"""
  Your executable:
    {os.path.abspath('dist/SystemUpdate.exe')}

  To share: Send SystemUpdate_v1.0.zip
  OR just: dist\\SystemUpdate.exe
""")
        
    except KeyboardInterrupt:
        print("\n\nBuild cancelled.")
    except Exception as e:
        print(f"\n[ERROR] {e}")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()