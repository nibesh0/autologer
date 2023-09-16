from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt(credentials, key):
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(credentials.encode())

def decrypt(encrypted_data, key):
    cipher_suite = Fernet(key)
    return cipher_suite.decrypt(encrypted_data).decode()

def store_key(filename, key):
    with open(filename, "wb") as file:
        file.write(key)

def retrieve_key(filename):
    with open(filename, "rb") as file:
        key = file.read()
    return key

def store_credentials(filename, key_filename, username, password):
    credentials = f"{username}:{password}"
    key = retrieve_key(key_filename)
    encrypted_credentials = encrypt(credentials, key)

    with open(filename, "wb") as file:
        file.write(encrypted_credentials)

def retrieve_credentials(filename, key_filename):
    key = retrieve_key(key_filename)
   
    with open(filename, "rb") as file:
        encrypted_credentials = file.read()

    decrypted_credentials = decrypt(encrypted_credentials, key)
    username, password = decrypted_credentials.split(":")
    return username, password

if __name__ == "__main__":
    key_filename = "encryption_key.key"
    filename = "credentials.enc"

    # Generate and store encryption key
    key = generate_key()
    store_key(key_filename, key)
    print("Encryption key stored securely.")

    # Store credentials
    store_credentials(filename, key_filename, id, passwd)

    print("Credentials stored securely.")

    # Retrieve and use credentials
    retrieved_username, retrieved_password = retrieve_credentials(filename, key_filename)
    print(f"Retrieved Username: {retrieved_username}")
    print(f"Retrieved Password: {retrieved_password}")
