from cryptography.fernet import Fernet

def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()

def decrypt_message(encrypted_message):
    """
    Decrypts an encrypted message
    """
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)

    print(decrypted_message.decode())

if __name__ == "__main__":
    decrypt_message(b'gAAAAABesCUIAcM8M-_Ik_-I1-JD0AzLZU8A8-AJITYCp9Mc33JaHMnYmRedtwC8LLcYk9zpTqYSaDaqFUgfz-tcHZ2TQjAgKKnIWJ2ae9GDoea6tw8XeJ4=')