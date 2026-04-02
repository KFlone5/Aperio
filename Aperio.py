import argparse
from cracker import crack_hash, HASHLIB_ALGORITHMS, CRYPT_ALGORITHMS

ALL_ALGORITHMS = HASHLIB_ALGORITHMS | CRYPT_ALGORITHMS


def parse_args():
    parser = argparse.ArgumentParser(
        prog="aperio",
        description="Hash cracker using wordlist-based bruteforce"
    )

    parser.add_argument(
        "-H", "--hash",
        required=True,
        help="Target hash to crack"
    )

    parser.add_argument(
        "-a", "--algorithm",
        required=True,
        choices=ALL_ALGORITHMS,
        metavar="ALGORITHM",
        help=f"Hashing algorithm to use. Available: {', '.join(sorted(ALL_ALGORITHMS))}"
    )

    parser.add_argument(
        "-w", "--wordlist",
        required=True,
        help="Path to wordlist file"
    )

    return parser.parse_args()


def main():
    args = parse_args()

    print(f"Hash:      {args.hash}")
    print(f"Algorithm: {args.algorithm}")
    print(f"Wordlist:  {args.wordlist}")
    print(f"\nStarting crack...\n")

    result = crack_hash(args.hash, args.wordlist, args.algorithm)

    if result:
        print(f"Password found: {result}")
    else:
        print("Password not found.")


if __name__ == "__main__":
    main()