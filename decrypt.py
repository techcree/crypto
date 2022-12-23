#ssk TechCree2022
def encrypt(message, key):
  # Create an empty string to store the encrypted message
  encrypted_message = input("Entschlüsseln von: ")

  # Loop through each character in the message
  for char in message:
    # Get the ASCII value of the character
    ascii_val = ord(char)

    # Encrypt the character by adding the key to the ASCII value
    encrypted_char = chr(ascii_val + key)

    # Add the encrypted character to the encrypted message
    encrypted_message += encrypted_char

  return encrypted_message

def decrypt(encrypted_message, key):
  # Create an empty string to store the decrypted message
  message = ""

  # Loop through each character in the encrypted message
  for char in encrypted_message:
    # Get the ASCII value of the character
    ascii_val = ord(char)

    # Decrypt the character by subtracting the key from the ASCII value
    decrypted_char = chr(ascii_val - key)

    # Add the decrypted character to the message
    message += decrypted_char

  return message

# Test the cipher
message = ""
key = 3
encrypted_message = encrypt(message, key)
#print(encrypted_message)
decrypted_message = decrypt(encrypted_message, key)
print(decrypted_message)
