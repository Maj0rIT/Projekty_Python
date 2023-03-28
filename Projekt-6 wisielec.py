import random

slowa = ["komputer", "programowanie", "statystyka", "eksperyment", "matematyka", "algorytm", "sztuczna inteligencja", "neuron", "cyfrowy", "symulacja"]

slowo = random.choice(slowa)

poprawne_litery = ""

pruby = 12

def display_slowo(slowo, poprawne_litery):
    display = ""
    for litery in slowo:
        if litery in poprawne_litery:
            display += litery
        else:
            display += "_"
        return display

while pruby > 0:
    print(display_slowo(slowo, poprawne_litery))

    gosc = input("Zgadnij litery: ").lower()

    if gosc in slowo:
        poprawne_litery += gosc
        print("Dobrze!")
    else:
        pruby -= 1
        print("Nie ma takiej litery")
        print("Pozostało {} prób. ".format(pruby))

    if "_" not in display_slowo(slowo, poprawne_litery):
        print("Brawo Wygrałeś ")
        break

if pruby == 0:
    print("Niestety przegrałeś szukane słowo to {}.".format(slowo))

input()
