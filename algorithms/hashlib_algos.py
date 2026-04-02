import hashlib


def verify(password, target_hash, algorithm):
    if algorithm == "md5":
        return hashlib.md5(password.encode()).hexdigest() == target_hash
    elif algorithm == "sha1":
        return hashlib.sha1(password.encode()).hexdigest() == target_hash
    elif algorithm == "sha224":
        return hashlib.sha224(password.encode()).hexdigest() == target_hash
    elif algorithm == "sha256":
        return hashlib.sha256(password.encode()).hexdigest() == target_hash
    elif algorithm == "sha512":
        return hashlib.sha512(password.encode()).hexdigest() == target_hash
    elif algorithm == "sha3_256":
        return hashlib.sha3_256(password.encode()).hexdigest() == target_hash
    elif algorithm == "sha3_512":
        return hashlib.sha3_512(password.encode()).hexdigest() == target_hash
    elif algorithm == "blake2b":
        return hashlib.blake2b(password.encode()).hexdigest() == target_hash
    elif algorithm == "blake2s":
        return hashlib.blake2s(password.encode()).hexdigest() == target_hash
    else:
        return None