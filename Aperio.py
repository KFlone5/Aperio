from cracker import crack_hash

HASHLIB_LIST = "md5 / sha1 / sha224 / sha256 / sha512 / sha3_256 / sha3_512 / blake2b / blake2s"
CRYPT_LIST = "bcrypt / md5crypt / sha256crypt / sha512crypt / argon2 / ntlm / pbkdf2_sha256 / pbkdf2_sha512"


def welcome():
    print("""  ___                  _       
 / _ \                (_)      
/ /_\ \_ __   ___ _ __ _  ___  
|  _  | '_ \ / _ \ '__| |/ _ \ 
| | | | |_) |  __/ |  | | (_) |
\_| |_/ .__/ \___|_|  |_|\___/ 
      | |                      
      |_|                      """)
    print(("=" * 40) + "\nCurrent hashes available\n")
    print(f"[hashlib]  {HASHLIB_LIST}")
    print(f"[crypt]    {CRYPT_LIST}")
    print("=" * 40)


def main():
    welcome()

    target_hash = input("Enter hash: ").strip()
    algorithm = input("Enter algorithm: ").strip().lower()
    wordlist_path = input("Enter wordlist path: ").strip()

    print(f"\nStarting crack with algorithm: {algorithm}")

    result = crack_hash(target_hash, wordlist_path, algorithm)

    if result:
        print(f"Password found: {result}")
    else:
        print("Password not found.")


if __name__ == "__main__":
    main()