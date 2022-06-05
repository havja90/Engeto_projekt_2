"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Jan Haviernik
email: haviernikjan@gmail.com
"""

# import knihovny
import random
import time

# promenne
oddelovac = "-" * 50
pocet_pokusu = 0

# pozdrav
print(
    "Hi there!",
    oddelovac,
    "I've generated a random 4 digit number for you.",
    "Let's play a bulls and cows game.",
    oddelovac,
    "Enter a number: ",
    oddelovac,
    sep="\n"
)


# funkce vracejici list s cislem
def listCisel(cislo) -> list:
    return [int(i) for i in str(cislo)]


# funkce hodnitici, zdeli jsou v cisle duplikace
def bezDuplikaci(cislo) -> bool:
    cislo_li = listCisel(cislo)
    if len(cislo_li) == len(set(cislo_li)):
        return True
    else:
        return False


# funkce pro generovani nahodneho 4-ciferného cisla
def generovatCislo() -> int:
    while True:
        cislo = random.randint(1000, 9999)
        if bezDuplikaci(cislo):
            return cislo


# funkce vracejici list spravne uhodnutych
# pozic (bulls) a cisel (cows) v 4-cifernem cisle
def pocetBullsCows(cislo, pokus) -> list:
    bull_cow = [0, 0]
    cislo_li = listCisel(cislo)
    pokus_li = listCisel(pokus)

    for i, j in zip(cislo_li, pokus_li):
        if j in cislo_li:
            if j == i:
                bull_cow[0] += 1
            else:
                bull_cow[1] += 1
    return bull_cow

# funkce prevadejici sekundy na HH:MM:SS format
def prevodCasu(sekundy):
    return time.strftime("%H:%M:%S", time.gmtime(doba))

# hadane 4-mistne cislo
cislo = generovatCislo()
start = time.time()

# while smycka pro samotny prubeh hry
while True:
    pokus = input(">>> ")
    if not pokus.isnumeric():
        print("Enter numbers only.")
        print(oddelovac)
        pocet_pokusu += 1
        continue
    if not bezDuplikaci(pokus):
        print("Number cannot contain repeated digits.")
        print(oddelovac)
        pocet_pokusu += 1
        continue
    if int(pokus) < 1000 or int(pokus) > 9999:
        print("Enter 4-digit number only.")
        print(oddelovac)
        pocet_pokusu += 1
        continue

    bull_cow = pocetBullsCows(cislo, pokus)
    if bull_cow[0] == 1 and bull_cow[1] == 1:
        print(f"{bull_cow[0]} bull, {bull_cow[1]} cow")
        print(oddelovac)
        pocet_pokusu += 1
    elif bull_cow[0] == 1:
        print(f"{bull_cow[0]} bull, {bull_cow[1]} cows")
        print(oddelovac)
        pocet_pokusu += 1
    elif bull_cow[1] == 1:
        print(f"{bull_cow[0]} bulls, {bull_cow[1]} cow")
        print(oddelovac)
        pocet_pokusu += 1
    else:
        print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
        print(oddelovac)
        pocet_pokusu += 1
    if bull_cow[0] == 4:
        print(
              "Correct, you've guessed the right number",
              f"in {pocet_pokusu} guesses!",
              sep="\n"
              )
        konec = time.time()
        break

# vyhodnoceni poctu pokusu
if pocet_pokusu < 4:
    print(oddelovac)
    print("That's amazing!")
elif pocet_pokusu > 8:
    print(oddelovac)
    print("That's not so good :-(")
else:
    print(oddelovac)
    print("That's average.")

# pocitani casu
doba = konec - start
print(f"Your time was: {prevodCasu(doba)} (time format: HH:MM:SS)")
