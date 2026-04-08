import multiprocessing
from itertools import product
from algorithms import hashlib_algos, crypt_algos

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


def verify_password(task):
    password, target_hash, algorithm = task
    if algorithm in HASHLIB_ALGORITHMS:
        if hashlib_algos.verify(password, target_hash, algorithm):
            return password
    elif algorithm in CRYPT_ALGORITHMS:
        if crypt_algos.verify(password, target_hash, algorithm):
            return password
    return None

def krunch_init(pattern, strings=""):
    total_passwords = 1
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
            total_passwords *= len(ALL_CHARSET)
            charsets.append(ALL_CHARSET)
        else:
            charsets.append(char)

    print(f"Total number of passwords will be checked: {total_passwords}")
    
    return charsets

def crack_hash(target_hash, wordlist_path, algorithm, threads=1):
    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as file:
            if threads <= 1:
                # Single thread
                for line in file:
                    password = line.strip()
                    if not password:
                        continue
                    print(f"Trying: {password:<30}", end="\r")
                    if verify_password((password, target_hash, algorithm)):
                        print(" " * 50, end="\r")
                        return password
            else:
                # Multi Thread with creation of task
                tasks = []
                for line in file:
                    password = line.strip()
                    if password:
                        # Collecting data into a single task
                        new_task = (password, target_hash, algorithm)
                        tasks.append(new_task)
                
                with multiprocessing.Pool(processes=threads) as pool:
                    for result in pool.imap_unordered(verify_password, tasks, chunksize=1000):
                        if result:
                            pool.terminate()
                            return result
    except FileNotFoundError:
        print(f"Wordlist file not found: {wordlist_path}")
    return None

def crack_hash_pattern(target_hash, pattern, algorithm, threads=1):
    charsets = krunch_init(pattern)
    combinations = product(*charsets)

    # Single Thread
    if threads <= 1:
        for combo in combinations:
            password = "".join(combo)
            print(f"Trying: {password:<30}", end="\r")
            if verify_password((password, target_hash, algorithm)):
                print(" " * 50, end="\r")
                return password
    else:
        # Multi Thread
        tasks = []
        for combo in combinations:
            password = "".join(combo)
            new_task = (password, target_hash, algorithm)
            tasks.append(new_task)
            
        with multiprocessing.Pool(processes=threads) as pool:
            for result in pool.imap_unordered(verify_password, tasks, chunksize=1000):
                if result:
                    pool.terminate()
                    return result
    return None