"""
    Zadanie (1.pkt)
    Napisać funkcje ktora przyjmuje liste liczb i zwraca ich iloczyn
    Przykład
    [1,2,3,4] -> 1*2*3*4
"""
lista = [1,2,3,4]
wynik = 1
for el in lista:
    wynik = wynik * lista[el -1]
print(wynik)

