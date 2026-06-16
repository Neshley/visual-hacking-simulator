@echo off
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
if not exist "%ProgramFiles%\SystemUpdate" mkdir "%ProgramFiles%\SystemUpdate"
copy /Y "%~dp0SystemUpdate.exe" "%ProgramFiles%\SystemUpdate\" >nul 2>&1

if %errorlevel% neq 0 (
    echo [ERROR] Failed to copy files
    pause
    exit /b 1
)

echo [*] Creating Desktop shortcut...
powershell -Command "$WS = New-Object -ComObject WScript.Shell; $SC = $WS.CreateShortcut('%USERPROFILE%\Desktop\SystemUpdate.lnk'); $SC.TargetPath = '%ProgramFiles%\SystemUpdate\SystemUpdate.exe'; $SC.WorkingDirectory = '%ProgramFiles%\SystemUpdate'; $SC.Save()" >nul 2>&1

echo [*] Creating Start Menu shortcut...
powershell -Command "$WS = New-Object -ComObject WScript.Shell; $SM = [Environment]::GetFolderPath('Programs'); $SC = $WS.CreateShortcut($SM + '\SystemUpdate.lnk'); $SC.TargetPath = '%ProgramFiles%\SystemUpdate\SystemUpdate.exe'; $SC.WorkingDirectory = '%ProgramFiles%\SystemUpdate'; $SC.Save()" >nul 2>&1

echo.
echo ==========================================
echo   Installation Complete!
echo ==========================================
echo.
echo Installed to: %ProgramFiles%\SystemUpdate\
echo.
echo Shortcuts on Desktop and Start Menu
echo.
pause
