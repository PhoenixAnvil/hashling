import hashlib


def hash_file(filepath, hashalg, chunk_size=4096):
    """
    Calculate the cryptographic hash of a file.

    Args:
        filepath (str): Path to the file to hash.
        hashalg (str): Hashing algorithm to use (e.g., 'sha256').
        chunk_size (int): Number of bytes to read at a time. Default is 4096.

    Returns:
        str: Hex digest of the file's hash.
    """
    hasher = hashlib.new(hashalg.lower())
    with open(filepath, "rb") as f:
        while chunk := f.read(chunk_size):
            hasher.update(chunk)
    return hasher.hexdigest()
