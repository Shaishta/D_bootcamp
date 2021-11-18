def encrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)

            # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


# def decrypt(ciphertext, s):


text = input("Enter a message to be ciphered")
s = 4
Cipher = encrypt(text, s)

print("Text : " + text)
print("Shift : " + str(s))
print("Cipher: " + encrypt(text, s))

# import string
# alphabet_lowercase = list(string.ascii_lowercase)
# alphabet_uppercase = list(string.ascii_uppercase)
#
# def userCypher(message, shift, encrypt_or_decrypt):
#     cyphered_message = ''
#     extra_chars = [' ', ',', '.', '!', "'", "?"]
#     for letter in message:
#         if letter in extra_chars:
#             cyphered_message += letter
#         else:
#             upper_or_lower = alphabet_uppercase if letter.isupper() else alphabet_lowercase
#             index_of_letter = upper_or_lower.index(letter)
#             if encrypt_or_decrypt == 'encrypt':
#                 cyphered_message += upper_or_lower[index_of_letter - shift]
#             else:
#                 if index_of_letter >= 26 - shift:
#                     new_index = index_of_letter + shift -26
#                     cyphered_message += upper_or_lower[new_index]
#                 else:
#                     cyphered_message += upper_or_lower[index_of_letter + shift]
#         return cyphered_message
# message = "hello! what is up?"
# print(cyphered = userCypher(message, 2, 'encrypt'))
# print(userCypher(cyphered, 2, 'decrypt'))

