import hashlib
from modules.exceptions import InvalidInputParameter

def get_unique_hash(content):
    if not content or not isinstance(content, (str, bytes)):
        raise InvalidInputParameter()
    return hashlib.sha256(content).hexdigest()
