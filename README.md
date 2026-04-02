# Aperio

A wordlist-based hash cracker written in Python.

## Supported algorithms

**hashlib:** md5, sha1, sha224, sha256, sha512, sha3_256, sha3_512, blake2b, blake2s

**crypt:** bcrypt, md5crypt, sha256crypt, sha512crypt, argon2, ntlm, pbkdf2_sha256, pbkdf2_sha512

## Installation

```
pip install -r requirements.txt
```

## Usage

```
python main.py -H <hash> -a <algorithm> -w <wordlist>
```

### Arguments

| Argument | Description |
|---|---|
| `-H`, `--hash` | Target hash to crack |
| `-a`, `--algorithm` | Hashing algorithm used |
| `-w`, `--wordlist` | Path to wordlist file |

### Examples

```
python main.py -H 5f4dcc3b5aa765d61d8327deb882cf99 -a md5 -w /usr/share/wordlists/rockyou.txt
```

```
python main.py -H 5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8 -a sha1 -w wordlist.txt
```

## Project structure

```
aperio/
├── main.py
├── cracker.py
├── requirements.txt
└── algorithms/
    ├── hashlib_algos.py
    └── crypt_algos.py
```

## Disclaimer

This tool is intended for CTF challenges and testing hashes you own. Do not use it against hashes you are not authorised to crack.
