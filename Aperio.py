import argparse
import sys
from cracker import crack_hash, crack_hash_pattern, HASHLIB_ALGORITHMS, CRYPT_ALGORITHMS

ALL_ALGORITHMS = HASHLIB_ALGORITHMS | CRYPT_ALGORITHMS


def parse_args():
    parser = argparse.ArgumentParser(
        prog="aperio",
        description="Hash cracker using wordlist-based bruteforce (Multi-processing enabled)"
    )

    parser.add_argument("-H", "--hash", required=True, help="Target hash to crack")
    parser.add_argument(
        "-a", "--algorithm",
        required=True,
        type=str.lower,
        choices=ALL_ALGORITHMS,
        metavar="ALGORITHM",
        help=f"Hashing algorithm. Available: {', '.join(sorted(ALL_ALGORITHMS))}"
    )
    parser.add_argument("-w", "--wordlist", help="Path to wordlist file")
    parser.add_argument("-p", "--pattern", help="Pattern for Krunch on-the-fly")
    
    # Новый аргумент для многопроцессорности
    parser.add_argument(
        "-t", "--threads",
        type=int,
        default=1,
        help="Number of processes to use (default: 1)"
    )

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    
    args = parser.parse_args()
 
    if args.wordlist and args.pattern:
        print("Error: use either -w or -p, not both.\n")
        sys.exit(1)
 
    if (not args.wordlist) and (not args.pattern):
        print("Error: you must specify either -w or -p.\n")
        sys.exit(1)

    return args


def main():
    args = parse_args()

    print(f"Hash:      {args.hash}")
    print(f"Algorithm: {args.algorithm}")
    print(f"Processes: {args.threads}")
 
    if args.wordlist:
        print(f"Wordlist:  {args.wordlist}")
        print(f"\nStarting crack...\n")
        result = crack_hash(args.hash, args.wordlist, args.algorithm, args.threads)
    else:
        print(f"Pattern:   {args.pattern}")
        print(f"\nStarting crack...\n")
        result = crack_hash_pattern(args.hash, args.pattern, args.algorithm, args.threads)
    
    if result:
        print(f"Password found: {result}")
    else:
        print("Password not found.")


if __name__ == "__main__":
    main()