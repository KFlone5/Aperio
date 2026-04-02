import hashlib


def verify(password, target_hash, algorithm):
    if algorithm == "md5":
        return hashlib.md5(password.encode()).hexdigest() == target_hash
    elif algorithm == "sha1":
        return hashlib.sha1(password.encode()).hexdigest() == target_hash
    elif algorithm == "sha256":
        return hashlib.sha256(password.encode()).hexdigest() == target_hash
    elif algorithm == "sha512":
        return hashlib.sha512(password.encode()).hexdigest() == target_hash
    else:
        return None
