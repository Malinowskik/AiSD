# # Zadanie 1
# def a(imie: str, nazwisko: str):
#     return print(imie + '.' + nazwisko)
#
# i = input("Podaj pierwszą literę imienia: ")
# n = input("Podaj nazwisko: ")
# a(i, n)

# Zadanie 2
# def b(imie: str, nazwisko: str):
#     return print(imie[0].upper() + '.' + nazwisko.capitalize())
#
# i = input("Podaj pierwszą imię: ")
# n = input("Podaj nazwisko: ")
# b(i, n)

# # Zadanie 3
# def d(a: int, b: int, c: int, n : int = 0):
#     n = a*100+b-c
#     return print(f' Twój rok urodzenia to: {n}')
# x = int(input("Podaj 2 pierwsze cyfry bierzącego roku: "))
# y = int(input("Podaj 2 ostatnie cyfry bierzącego roku: "))
# z = int(input("Podaj swój wiek: "))
# d(x,y,z)

# # Zadanie 4
# def e(imie: str, nazwisko: str, funkcja):
#     return funkcja(imie, nazwisko)
# print(e(i,n,b))

# Zadanie 5
# def f(a: float, b: float):
#     if a > 0 and b > 0 and b != 0 :
#         return a/b
#     return "Błędne liczby"
# x = float(input("Podaj 1 liczbę: "))
# z = float(input('Podaj 2 liczbę: '))
# print (f(x,z))

# # Zadanie 6
# def t(x: float, y: float = 0):
#     while y < 100:
#       y = y +x
#       x = float(input("Wprowadź kolejną liczbę: "))
# z = float(input("Wprowadź liczbę: "))
# t(z)

# Zadanie 7
# def u(k: list):
#     return tuple(k)
# k = ["a", "b", "c", "d"]
# print(u(k))

# # Zadanie 8
# def o(j: list):
#     return j
# x = []
# z = int(input("Ile chcesz wprowadzić danych?: "))
# for i in range (0,z):
#         y = input("Podaj wartość: ")
#         x.append(y)
# print(o(x))

# # Zadanie 9
# def p(i: int, l: list):
#     return l[i-1]
# b = ['piniedzialek', 'wtorek', 'sroda', 'czwartek', 'piatek', 'sobota', 'niedziela']
# a = int(input("Podaj liczbę od 1 do 7: "))
# print(p(a,b))

# Zadanie 10
def s(x: str):
    x = x.lower()
    x = x.replace(" ","")
    z = len(x)
    y = 0
    a = []
    b = []
    for k in range (0,z):
        a.append(x[k])
        b.append(x[-(k+1)])
        if a[k] == b[k]: y = y + 1
    if y == z: print("Wprowadzony tekst jest palindromem.")
    else:
        print("Wporwadzony tekst nie jest palindromem.")
i = input("Wprowadź tekst: ")
print(s(i))
