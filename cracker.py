from algorithms import hashlib_algos, crypt_algos

HASHLIB_ALGORITHMS = {
    "md5", "sha1", "sha224", "sha256", "sha512",
    "sha3_256", "sha3_512", "blake2b", "blake2s"
}

CRYPT_ALGORITHMS = {
    "bcrypt", "md5crypt", "sha256crypt", "sha512crypt",
    "argon2", "ntlm", "pbkdf2_sha256", "pbkdf2_sha512"
}


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
                if verify_password(password, target_hash, algorithm):
                    return password
    except FileNotFoundError:
        print(f"Wordlist file not found: {wordlist_path}")
        return None
    return None