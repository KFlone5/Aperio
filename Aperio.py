import hashlib
import bcrypt
from argon2 import PasswordHasher
from passlib.hash import md5_crypt, sha256_crypt, sha512_crypt


def welcome():
    print("""  ___                  _       
 / _ \                (_)      
/ /_\ \_ __   ___ _ __ _  ___  
|  _  | '_ \ / _ \ '__| |/ _ \ 
| | | | |_) |  __/ |  | | (_) |
\_| |_/ .__/ \___|_|  |_|\___/ 
      | |                      
      |_|                      """)
    print(("="*40)+"\nCurrent hashes available\n")
    print("MD5 | SHA-1 | SHA-256 | SHA-512")
    print("bcrypt | md5crypt | sha256crypt | sha512crypt | argon2")


def verify_password(password, target_hash, algorithm):
    try:
        if algorithm == "md5":
            return hashlib.md5(password.encode()).hexdigest() == target_hash
        elif algorithm == "sha1":
            return hashlib.sha1(password.encode()).hexdigest() == target_hash
        elif algorithm == "sha256":
            return hashlib.sha256(password.encode()).hexdigest() == target_hash
        elif algorithm == "sha512":
            return hashlib.sha512(password.encode()).hexdigest() == target_hash
        elif algorithm == "bcrypt":
            return bcrypt.checkpw(password.encode(), target_hash.encode())
        elif algorithm == "md5crypt":
            return md5_crypt.verify(password, target_hash)
        elif algorithm == "sha256crypt":
            return sha256_crypt.verify(password, target_hash)
        elif algorithm == "sha512crypt":
            return sha512_crypt.verify(password, target_hash)
        elif algorithm == "argon2":
            ph = PasswordHasher()
            ph.verify(target_hash, password)
            return True
        else:
            raise ValueError(f"Unsupported algorithm: {algorithm}")
    except Exception:
        return False


def crack_hash(target_hash, wordlist_path, algorithm):
    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                password = line.strip()
                if not password:
                    continue
                if verify_password(password, target_hash, algorithm):
                    return password
    except FileNotFoundError:
        print(f"Wordlist file not found: {wordlist_path}")
        return None
    return None


def main():
    welcome()

    target_hash = input("Enter hash: ").strip()
    algorithm = input("Enter algorithm (md5 / sha1 / sha256 / sha512 / bcrypt / md5crypt / sha256crypt / sha512crypt / argon2): ").strip().lower()
    wordlist_path = input("Enter wordlist path: ").strip()

    print(f"\nStarting crack with algorithm: {algorithm}")

    result = crack_hash(target_hash, wordlist_path, algorithm)

    if result:
        print(f"Password found: {result}")
    else:
        print("Password not found.")


if __name__ == "__main__":
    main()