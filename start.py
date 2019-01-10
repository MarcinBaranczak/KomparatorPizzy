import math


# ----- pobiera ilość wykonań -----
def start():
    ilosc = int(input("Podaj ilość pizz do porównania: "))

    tabPola = []
    for i in range(ilosc):
        tabPola.append(pobierzDane())
    # endFor

    for i in tabPola:
        obliczPizze(i)
    # endFor


# ----- oblicza i wyświetla dane -----
def obliczPizze(r):
    print("pole (", 2 * r, "\bcm ):", obliczPole(r))


# ----- pobiera dane pizzy -----
def pobierzDane():
    return float(input("podaj wielkość pizzy: ")) / 2


# ----- oblicza pole koła PI*r^2
def obliczPole(r):
    return int(math.pi * (r ** 2))


# ----- program główny -----

start()
