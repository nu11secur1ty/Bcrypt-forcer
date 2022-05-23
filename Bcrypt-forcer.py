#!/usr/bin/python3

from passlib.hash import bcrypt
from libs import pingo
import sys

print("\n*************************************************")
print("Debcrypt - Password cracker tools for bcrypt hash")
print("*************************************************")
options = input('\nYou want to crack? y/n: ')

if (options == "n"):
    sys.exit()
elif (options != "y" and options != "n"):
    sys.exit('Invalid Option')

passwords = (options == "y")
text_file = open("password-list/testingpass.txt", "r", encoding="cp437")

words = text_file.read().splitlines()

hash = input('Hash to crack: ')
length = len(words)

correct_word = ""
found = 0
for (index, word) in enumerate(words):
    pingo(index, length, prefix='Wait:', suffix='Words complete from the list')
    correct = bcrypt.verify(word, hash)
    if (correct):
        correct_word = word
        found += 1
        break

if (found == 1):
    print("\n\nPassword found!")
    print("Results:", correct_word)
else:
    print("\n\nUnfortunately, password not found.")