def caesar_cipher(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            is_upper = char.isupper()  # Check if the letter is uppercase
            char = char.lower()  # Convert to lowercase for simplicity
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            
            if is_upper:
                shifted_char = shifted_char.upper()  # Convert back to uppercase if it was uppercase in the original text
            
            encrypted_text += shifted_char
        else:
            encrypted_text += char  # Keep non-alphabet characters unchanged
    
    return encrypted_text

def caesar_decipher(encrypted_text, shift):
    return caesar_cipher(encrypted_text, -shift)  # Deciphering is just shifting in the opposite direction


print(caesar_decipher("Neon145",2))