wynik = 0
Computerwynik = 0
while wynik != 3 and Computerwynik != 3:
    YourChose = input("Wybierz(1 = kamien),(2 = papier),(3 = nozyczki): ")
    YourChose = int(YourChose)

    if YourChose == 1:
        print("Wybrales: Kamien")
    elif YourChose == 2:
        print("Wybrales: Napier")
    elif YourChose == 3:
        print("Wybrales: Nozyczki")
    import random
    Computer = random.choice([1,2,3])
    if Computer == 1:
        print("Komputer wybrał: Kamien")
    elif Computer == 2:
        print("Komputer wybrał: Papier")
    elif Computer == 3:
        print("Komputer wybrał: Nozyczki")
    if YourChose == 1:
        if Computer == 2:
            print("Przegrales")
            Computerwynik += 1
        elif Computer == 3:
            print("Wygrales")
            wynik += 1
        else:
            print("Remis!") 
    if YourChose == 2:
        if Computer == 3:
            print("Przegrales")

            Computerwynik += 1
        elif Computer == 1:
            print("Wygrales")
            wynik += 1
        else:
            print("Remis!")
    if YourChose == 3:
        if Computer == 1:
            print("Przegrales")
            Computerwynik += 1
        elif Computer == 2:
            print("Wygrales")
            wynik += 1
        else:
            print("Remis!")
print("Twoj Wynik: ", wynik,",  Wynik Komputera: ", Computerwynik)
if Computerwynik == 3:
    print("Przegrales!!!!")
elif wynik == 3:
    print("Wygrales!!!!")