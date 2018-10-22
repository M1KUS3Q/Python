lista = [1,2,-3]
lepszaLista = []
for x in range(0,len(lista)-1):
   
    if lista[x] > 0:
        lepszaLista.append(lista[x])
    else:
        print("index",x, "nie może zostać dodany")
print("lista: ",lista)
print("lista bez liczb ujemnych: ",lepszaLista)
wynik = 0
for el in lepszaLista:
    wynik = wynik + el
print("suma dodatnich liczb z listy: ",wynik)