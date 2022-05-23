#!/usr/bin/python3
# nu11secur1ty 2022
from passlib.hash import bcrypt
from libs import pingo
import sys
from colorama import init, Fore, Back, Style
init(convert=True)
import requests

print(Fore.BLUE + "\n******************************************************")
print("Bcrypt-forcer - Password cracker tool for bcrypt hash")
print("******************************************************")
print(Style.RESET_ALL)

print(Fore.YELLOW)
options = input('\nYou want to crack? y/n: ')
print(Style.RESET_ALL)

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
    print(Fore.YELLOW+"\n\nPassword found!")
    print(Style.RESET_ALL)
    print(Fore.GREEN+"Results:", correct_word)
    print(Style.RESET_ALL)
else:
    print(Fore.RED+"\n\nUnfortunately, password not found.")
    print(Style.RESET_ALL)
