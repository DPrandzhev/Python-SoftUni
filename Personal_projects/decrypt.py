import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Prompt the user for the encrypted message
encrypted_message = input("Enter the encrypted message: ")

# Prompt the user for the password
password = input("Enter the password: ").encode()

# Use the password and the same salt to recreate the key
salt = b'salt_'
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256,
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))

# Use the key to decrypt the message
f = Fernet(key)
decrypted_message = f.decrypt(encrypted_message).decode()

# Print the decrypted message
print(decrypted_message)
