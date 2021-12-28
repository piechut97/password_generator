import sys
import random
import string

password = []
characters_left = -1

def update_characters_left(number_of_characters):
    global characters_left

    if number_of_characters > characters_left or number_of_characters < 0:
        print("Liczba znaków spoza przedziału 0,", characters_left)
        return 1
    else:
        characters_left -= number_of_characters
        print("Pozostało znaków:", characters_left)

password_length = int(input("Jak długie ma być hasło? "))

while (password_length <5):
    print("Hasło musi mieć minimum 5 znaków, spróbuj jeszcze raz.")
    password_length = int(input("Jak długie ma być hasło? "))

characters_left = password_length

while 1:
    try:
        lowercase_letters = int(input("Ile małych liter ma mieć hasło? "))
        break
    except:
        print("Błąd danych, proszę o podanie liczby.")

if update_characters_left(lowercase_letters) == 1:
    lowercase_letters = int(input("Ile małych liter ma mieć hasło? "))

while 1:
    try:
        uppercase_letters = int(input("Ile dużych liter ma mieć hasło? "))
        break
    except:
        print("Błąd danych, proszę o podanie liczby.")

if update_characters_left(uppercase_letters) == 1:
    uppercase_letters = int(input("Ile dużych liter ma mieć hasło? "))

while 1:
    try:
        special_characters = int(input("Ile znaków specjalnych ma mieć hasło? "))
        break
    except:
        print("Błąd danych, proszę o podanie liczby.")

if update_characters_left(special_characters) == 1:
    special_characters = int(input("Ile znaków specjalnych ma mieć hasło? "))

while 1:
    try:
        digits = int(input("Ile cyfr ma mieć hasło? "))
        break
    except:
        print("Błąd danych, proszę o podanie liczby.")

if update_characters_left(digits) == 1:
    digits = int(input("Ile cyfr ma mieć hasło? "))

if characters_left > 0:
    print("Nie wszystkie znaki zostały wykorzystane, hasło zostanie uzupełnione małymi literami.")
    lowercase_letters += characters_left

print()
print("Długość hasła:", password_length)
print("Małe litery:", lowercase_letters)
print("Duże litery:", uppercase_letters)
print("Znaki specjalne:", special_characters)
print("Cyfry:", digits)

for _ in range(password_length):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1

    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1

    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1

    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1

random.shuffle(password)

print("Wygenerowane hasło:", "".join(password))