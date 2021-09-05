# Simple-Encryptor

This is a simple message encrypter made using the cryptography module.
It encrypts the message with a special key and it can only decrypt that message with the same key. 

```gen_key()``` Creates a key and saves it to a file call key.txt

```get_key()``` and ```get_message()``` both read their respective files and get the message/key inside them and returns them

```encrypt(get_key())``` Asks you for a message, and uses the key to encrypt the message. Then it saves the message to a file.

```decrypt(get_key(), get_message())``` Gets encrypted message and key and uses key to decrypt the message.
