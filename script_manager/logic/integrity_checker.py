import hashlib

# get hash value to check integrity
def calculate_sha256(file_path):
    data = file_path.read_bytes()
    return hashlib.sha256(data).hexdigest()