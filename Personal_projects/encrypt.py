import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Prompt the user for the message to be encrypted
message = input("Enter the message to be encrypted: ")

# Prompt the user for a password
password = input("Enter a password: ").encode()

# Create a salt
salt = b'salt_'

# Use the password and salt to derive the encryption key
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256,
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))

# Use the key to encrypt the message
f = Fernet(key)
encrypted_message = f.encrypt(message.encode())

# Print the encrypted message
print(encrypted_message)
