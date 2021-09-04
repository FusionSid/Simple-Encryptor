from cryptography.fernet import Fernet

# Generate Key
def gen_key():
    key = Fernet.generate_key()
    with open('key.txt', 'wb') as f:
        f.write(key)

# Open File With Key
def get_key():
    with open('key.txt', 'rb') as f:
        key = f.read() # get key and save as key
    return key


# Encrypt Message
def encrypt(key):
    message = input("Message: ").encode() # get message
    f = Fernet(key)
    encrypted = f.encrypt(message)
    with open('encrypted.txt', 'wb') as f:
        f.write(encrypted)


# Get File With Message 
def get_msg():
    with open('encrypted.txt', 'rb') as f:
        encrypted = f.read() # get encrypted message
    return encrypted

# Decrypt Message
def decrypt(key, encrypted):
    f = Fernet(key)
    decrypted = f.decrypt(encrypted).decode()
    return decrypted


# gen_key()
# encrypt(get_key())

message = decrypt(get_key(), get_msg())

print(message)