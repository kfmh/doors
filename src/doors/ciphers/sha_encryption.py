import hashlib

class SHA256:
    def __init__(self):
        pass

    def encryption(self, message):
        hash_object = hashlib.sha256()
        hash_object.update(message.encode())

        hex_dig = hash_object.hexdigest()

        return hex_dig