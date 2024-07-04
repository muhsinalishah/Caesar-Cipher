print()
print (" ***        Ceaser Cyfer Encryption       ***  ")
print()
user_in = input("Please enter Your Text to Encrypt :")
user_key = int(input("Please enter Your key : "))
encrypt_message = ""

for i in user_in:
    add = ord(i)+user_key
    chat = chr(add)
    encrypt_message += chat
print(encrypt_message)


print()
print(" ****     Decryption Of Text      ****")
print()

user_in_2 = input("Please enter Your Encrypted Text :")
user_key_2 = int(input("Please enter Your key : "))
decrypt_message = ""
for x in user_in_2:
    asci = ord(x)-user_key_2
    alphabet = chr(asci)
    decrypt_message += alphabet

print(decrypt_message)