import os
os.system("cls")
print("Cześć jestem kalkulator")
try:
    x = int(input("Podaj liczbe: "))
except:
    print("To nie jest liczba")
try:
    y = int(input("Podaj drugą liczbe: "))
except:
    print("To nie jest liczba")

z = input("Podaj działanie matemtyczne + ,- ,* , /: ")


if (z == "+"):
    print("Wynik dodawania to: ",x+y)
elif (z == "-"):
    print("Wynik odejmowania to: ",x+y)
elif (z == "*"):
    print("Wynik mnożenia to: ",x*y)
elif (z == "/"):
    print("Wynik dzielenia to: ",x/y)
else:
    print("Nie obsluguje takiego dzialania")