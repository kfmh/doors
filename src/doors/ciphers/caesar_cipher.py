# Function that takes text and key and returns cipher


class Caeser_Cipher:
    def __init__(self):
        pass

    def encryption(self, text:str, key:int):
        result = ''
        for char in text:
            if char.isalpha():
                shift = key % 26
                if char.islower():
                    result += chr((ord(char) - 97 + shift) % 26 + 97)
                else:
                    result += chr((ord(char) - 97 + shift) % 26 + 65)

        return result

    def decryption(self, text:str, key:int):
        result = ""

        for char in text:
            if char.isalpha():  # Check if the character is a letter
                shift = key % 26  # Ensure the key always falls within the alphabet range
                if char.islower():
                    # Shift character backward for lowercase
                    result += chr((ord(char) - 97 - shift) % 26 + 97)
                else:
                    # Shift character backward for uppercase
                    result += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                # Keep the character as is (space, punctuation, etc.)
                result += char
        return result