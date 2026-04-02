import bcrypt
from passlib.hash import md5_crypt, sha256_crypt, sha512_crypt
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


def verify(password, target_hash, algorithm):
    try:
        if algorithm == "bcrypt":
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
            return None
    except VerifyMismatchError:
        return False
    except Exception:
        return False
