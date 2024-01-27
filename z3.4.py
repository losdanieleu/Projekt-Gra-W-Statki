from random import randint
#Ten komentarz został dodany na poczet zadania z NI
#Ten komnetarz został dodany jako drógi na poczet zadania narzędzi inżynierskich przez W.Zimną
# plansza ktora widzi gracz
plansza = []
# plansza do testow komputera
plansza_hidden = []

# wypelnienie obu plansz pustymi miejscami
def stworz_plansze():
    for x in range(5):
        plansza.append([" "] * 5)
        plansza_hidden.append([" "] * 5)

# wypisanie planszy uwzgledniajac tablice utworzona wyzej
def wypisz_plansze():
    print("     1"+"     2"+"     3"+"     4"+"     5")

    for i in range(5):
        print("  "+("+"+"-----") * 5 + "+")
        print("{} | ".format(i+1),"  |  ".join(plansza[i])," |")

    print("  "+("+"+"-----") * 5 + "+")

# wypisanie cheat table z odpowiedziami - planszy komputera
def wypisz_plansze_hidden():
    print("     1"+"     2"+"     3"+"     4"+"     5")

    for i in range(5):
        print("  "+("+"+"-----") * 5 + "+")
        print("{} | ".format(i+1),"  |  ".join(plansza_hidden[i])," |")

    print("  "+("+"+"-----") * 5 + "+")

# zastapienie pustych pol statkami w postaci - "X"
def spawn_statki():

    statki = 0

    while statki < 3:
        row = randint(0, len(plansza_hidden) - 1)
        col = randint(0, len(plansza_hidden[0]) - 1)

        if plansza_hidden[row][col] != "X":
            plansza_hidden[row][col] = "X"
            statki+=1

# sprawdzanie czy statek znajduje sie na podanej przez gracza pozycji jak i czy gracz juz strzelal w podane miejsce
def check_for_statek(wiersz,kolumna):

    statki = 3

    if plansza[wiersz][kolumna] == "0" or plansza[wiersz][kolumna] == "X":
        print("Juz raz wybrales to pole.")
        return False

    elif plansza_hidden[wiersz][kolumna] == "X":
        statki -= 1
        plansza[wiersz][kolumna] = "X"
        print("Trafiles statek wroga!")

        if statki <= 0:
            print("Zatopiles wszystki statki wroga wygrales!!!")
            exit(1)
        return True

    else:
        plansza[wiersz][kolumna] = "0"
        print("Tym razem pudlo.")
        return True

# rozgrywka
tura=0
stworz_plansze()
spawn_statki()

print("Witaj w grze w statki!\n"
      "Zatop statki wroga, aby strzelic w statek podaj jego koordynaty na planszy,\n"
      "pierw wiersz, a nastepnie kolumne! \n"
      "Oto plansza. ")

wypisz_plansze()
# wypisz_plansze_hidden()
while tura<6:

    print("Tura {}!".format(tura+1))

    try:
        guess_wiersz = int(input("podaj wiersz: "))
        guess_kolumna = int(input("podaj kolumne: "))

    except ValueError as error:
        guess_wiersz = -1
        guess_kolumna = -1

    if (0 < guess_wiersz <= 5) and (0 < guess_kolumna <= 5):
        if check_for_statek(guess_wiersz-1,guess_kolumna-1):
            tura+=1
        wypisz_plansze()

    else:
        print("Bledne koordynaty!!! Sprobuj uzyc liczby od 1 do 5!")


print("Skonczyly ci sie tury. Powodzenia nastepnym razem!")
#Komentarz przez W.Zimną Bardzo Ładny Kod <3
