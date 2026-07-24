#!/usr/bin/env python3
# ULTRA OBFUSCATOR - ANTI-DECOMPILE + ANTI-DEBUG 😈
# Base64 + zlib + XOR + marshal + anti-debug
# Ai Generate

import os
import sys
import zlib
import base64
import marshal
import random
import string
import time
import hashlib
from pathlib import Path

def random_name(length=8):
    first = random.choice(string.ascii_lowercase + '_')
    rest = ''.join(random.choice(string.ascii_lowercase + string.digits + '_') for _ in range(length - 1))
    return first + rest

def random_key():
    return random.randint(1, 255)

def xor_encrypt(data, key):
    return bytes([b ^ key for b in data])

def generate_anti_debug_code():
    return '''
# ========== ANTI-DEBUG ==========
import sys, os, time, random

def _anti_debug():
    try:
        # Cek debugger
        if sys.gettrace() is not None:
            print("Debugger detected!")
            sys.exit(1)
        # Cek ptrace (Linux)
        try:
            import fcntl
            fcntl.ioctl(0, 0x8004667e, b'x00'*8)
        except:
            pass
        # Cek environment debug
        if "PYTHONDEBUG" in os.environ or "DEBUG" in os.environ:
            sys.exit(1)
        # Cek IDE
        if "PYCHARM_HOSTED" in os.environ:
            sys.exit(1)
        # Delay acak
        time.sleep(random.random() * 0.5)
    except:
        pass

_anti_debug()
del _anti_debug
'''

def obfuscate_script(script_path):
    if not os.path.exists(script_path):
        print(f"[!] File {script_path} tidak ditemukan!")
        return
    
    with open(script_path, 'r', encoding='utf-8') as f:
        original = f.read()
    
    print(f"[+] Original: {len(original)} bytes")
    
    # ===== LAPISAN 1: COMPRESS =====
    compressed = zlib.compress(original.encode('utf-8'))
    
    # ===== LAPISAN 2: XOR ENCRYPT =====
    key1 = random_key()
    key2 = random_key()
    encrypted1 = xor_encrypt(compressed, key1)
    encrypted2 = xor_encrypt(encrypted1, key2)
    
    # ===== LAPISAN 3: MARSHA L =====
    marshaled = marshal.dumps(encrypted2)
    
    # ===== LAPISAN 4: BASE64 =====
    b64 = base64.b64encode(marshaled).decode('ascii')
    
    # ===== BIKIN VARIABLE ACAK =====
    v1 = random_name(12)
    v2 = random_name(10)
    v3 = random_name(8)
    v4 = random_name(14)
    v5 = random_name(6)
    v6 = random_name(16)
    
    # ===== HASH UNTUK INTEGRITY =====
    hash_val = hashlib.sha256(original.encode()).hexdigest()[:16]
    
    # ===== PAYLOAD =====
    output = f'''#!/usr/bin/env python3
# ULTRA OBFUSCATED - ANTI-DECOMPILE 😈
# Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}

import sys, os, zlib, base64, marshal, time, random, hashlib

# ========== ANTI-DEBUG ==========
{generate_anti_debug_code()}

# ========== PAYLOAD ==========
{v1} = """{b64}"""
{v2} = {key1}
{v3} = {key2}
{v4} = "{hash_val}"

def {v5}():
    try:
        # ===== DECODE =====
        {v6} = base64.b64decode({v1})
        _data = marshal.loads({v6})
        
        # ===== XOR DECRYPT =====
        _data = bytes([b ^ {v3} for b in _data])
        _data = bytes([b ^ {v2} for b in _data])
        
        # ===== DECOMPRESS =====
        _code = zlib.decompress(_data).decode('utf-8')
        
        # ===== INTEGRITY CHECK =====
        _check = hashlib.sha256(_code.encode()).hexdigest()[:16]
        if _check != {v4}:
            print("[!] Integrity check failed!")
            sys.exit(1)
        
        # ===== EXECUTE =====
        exec(_code, globals())
    except Exception as _e:
        print(f"[!] Error: {{_e}}")
        sys.exit(1)

if __name__ == "__main__":
    {v5}()
'''
    
    out_path = Path(script_path).stem + "_ultra_obfuscated.py"
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(output)
    
    print(f"[✓] Obfuscated: {out_path}")
    print(f"[+] Output: {len(output)} bytes")
    print(f"[+] Compression: {(1 - len(output) / len(original)) * 100:.1f}%")
    print(f"[+] XOR Key 1: {key1}")
    print(f"[+] XOR Key 2: {key2}")
    print(f"[+] Integrity Hash: {hash_val}")
    return out_path

def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(r"""
  ██╗   ██╗██╗  ████████╗██████╗  █████╗ 
  ██║   ██║██║  ╚══██╔══╝██╔══██╗██╔══██╗
  ██║   ██║██║     ██║   ██████╔╝███████║
  ██║   ██║██║     ██║   ██╔══██╗██╔══██║
  ╚██████╔╝███████╗██║   ██║  ██║██║  ██║
   ╚═════╝ ╚══════╝╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝
    """)
    print("ULTRA OBFUSCATOR - ANTI-DECOMPILE + ANTI-DEBUG")
    print("="*60)
    print("[!] 4 Lapisan: Base64 + XOR + Marshal + zlib")
    print("[!] Anti-Debug + Integrity Check")
    print("[!] Hasil: script_ultra_obfuscated.py\n")
    
    script = input("[?] Path script Python: ").strip()
    if not script or not os.path.exists(script):
        print("[!] File tidak ditemukan!")
        return
    
    confirm = input(f"[?] Obfuscate {script}? (y/n): ").strip().lower()
    if confirm == 'y':
        obfuscate_script(script)
        print("\n[✓] SELESAI!")
        print("[!] Jalankan: python testlogin_ultra_obfuscated.py")

if __name__ == "__main__":
    main()