import hashlib
from pathlib import Path

# get hash value to check integrity
def calculate_sha256(file_path: Path):
    data = file_path.read_bytes()
    return hashlib.sha256(data).hexdigest()