from algorithms import hashlib_algos, crypt_algos
from itertools import product

HASHLIB_ALGORITHMS = {
    "md5", "sha1", "sha224", "sha256", "sha512",
    "sha3_256", "sha3_512", "blake2b", "blake2s"
}

CRYPT_ALGORITHMS = {
    "bcrypt", "md5crypt", "sha256crypt", "sha512crypt",
    "argon2", "ntlm", "pbkdf2_sha256", "pbkdf2_sha512"
}

# CHARSETS
LOW_CHARSET = "abcdefghijklmnopqrstuvwxyz"
UPP_CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUM_CHARSET = "0123456789"
SYM_CHARSET = "!@#$%^&*()-_+=~`[]{}|\\:;\"'<>,.?/"
ALL_CHARSET = (LOW_CHARSET + UPP_CHARSET + NUM_CHARSET + SYM_CHARSET)


def krunch_init(pattern, strings=""):
    total_passwords = 1
    password_length = len(pattern)
    charsets = []

    for char in pattern:
        if char == "@":
            total_passwords *= len(strings)
            charsets.append(strings)
        elif char == "%":
            total_passwords *= len(NUM_CHARSET)
            charsets.append(NUM_CHARSET)
        elif char == "^":
            total_passwords *= len(SYM_CHARSET)
            charsets.append(SYM_CHARSET)
        elif char == "!":
            total_passwords *= len(LOW_CHARSET + UPP_CHARSET)
            charsets.append(LOW_CHARSET + UPP_CHARSET)
        elif char == "$":
            total_passwords *= len(LOW_CHARSET)
            charsets.append(LOW_CHARSET)
        elif char == "&":
            total_passwords *= len(UPP_CHARSET)
            charsets.append(UPP_CHARSET)
        elif char == "*":
            charsets.append(ALL_CHARSET)
        else:
            charsets.append(char)

    print(f"Total number of passwords will be generated: {total_passwords}")
    
    return charsets

def verify_password(password, target_hash, algorithm):
    if algorithm in HASHLIB_ALGORITHMS:
        return hashlib_algos.verify(password, target_hash, algorithm)
    elif algorithm in CRYPT_ALGORITHMS:
        return crypt_algos.verify(password, target_hash, algorithm)
    else:
        raise ValueError(f"Unsupported algorithm: {algorithm}")


def crack_hash(target_hash, wordlist_path, algorithm):
    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                password = line.strip()
                if not password:
                    continue
                print(f"Trying: {password:<30}", end="\r")
                if verify_password(password, target_hash, algorithm):
                    print(" " * 50, end="\r")
                    return password
    except FileNotFoundError:
        print(f"Wordlist file not found: {wordlist_path}")
        return None
    return None

def crack_hash_pattern(target_hash, pattern, algorithm):
    charsets = krunch_init(pattern)
    count = 0

    for password in product(*charsets):
        print(f"Trying: {password:<30}", end="\r")
        if verify_password(password, target_hash, algorithm):
            print(" " * 50, end="\r")
            return password