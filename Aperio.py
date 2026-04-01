import hashlib


def hash_password(password: str, algorithm: str) -> str:
    if algorithm == "md5":
        return hashlib.md5(password.encode()).hexdigest()
    elif algorithm == "sha1":
        return hashlib.sha1(password.encode()).hexdigest()
    else:
        raise ValueError(f"Unsupported algorithm: {algorithm}")


def crack_hash(target_hash: str, wordlist_path: str, algorithm: str) -> str | None:
    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                password = line.strip()
                if not password:
                    continue
                hashed = hash_password(password, algorithm)
                if hashed == target_hash:
                    return password
    except FileNotFoundError:
        print(f"Wordlist file not found: {wordlist_path}")
        return None
    return None


def main():
    target_hash = input("Enter hash: ").strip()
    algorithm = input("Enter algorithm (md5 / sha1): ").strip().lower()
    wordlist_path = input("Enter wordlist path: ").strip()

    print(f"\nStarting crack with algorithm: {algorithm}")

    result = crack_hash(target_hash, wordlist_path, algorithm)

    if result:
        print(f"Password found: {result}")
    else:
        print("Password not found.")


if __name__ == "__main__":
    main()