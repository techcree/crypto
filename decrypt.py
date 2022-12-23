#ssk TechCree 2022
def encrypt(message, key):
    encrypted_message = input("Entschlüsseln von: ")
    
    for char in message:
    ascii_val = ord(char)

    encrypted_char = chr(ascii_val + key)

    encrypted_message += encrypted_char

  return encrypted_message

def decrypt(encrypted_message, key):
    message = ""

    for char in encrypted_message:
        ascii_val = ord(char)

    decrypted_char = chr(ascii_val - key)

    message += decrypted_char

  return message

message = ""
key = 3
encrypted_message = encrypt(message, key)
decrypted_message = decrypt(encrypted_message, key)
print(decrypted_message)