from random import shuffle
# # Zadanie 1
# def x(a:str):
#     print('Liczba liter wielkich: ', sum(1 for x in a if x.isupper()))
#     print('Liczba liter małych: ', sum(1 for x in a if x.islower()))
#     print('Liczba cyfr: ', sum(1 for x in a if x.isnumeric()))
#     b = 0
#     for i in range (0, len(a)): #funkcja sprawdza czy w haśle jest jakikolwiek znak, również znak spacji
#         if (a[i].isalpha()):
#             continue
#         elif (a[i].isdigit()):
#             continue
#         else:
#             b +=1
#     print('Liczba znaków specjalnych takich jak: !, @, #, $, %, ^, &, *, (, ) itd: ',b )
# z = input("Wprowadź hasło: ")
# x(z)

# # Zadanie 2
# def x (a: str):
#     b = sum(1 for x in a if x.isupper())
#     c = sum(1 for x in a if x.islower())
#     d = sum(1 for x in a if x.isnumeric())
#     e = 0
#     for i in range (0, len(a)):
#         if (a[i].isalpha()):
#             continue
#         elif (a[i].isdigit()):
#             continue
#         else:
#             e +=1
#     if (len(a) < 8  or len(a) > 255 or b < 1 or d < 1 or e < 1):
#         return False
#     else: return True
# z = input("Wprowadź hasło: ")
# p = (x(z))
# if p:
#     print('Hasło spełnia wymagania.')
# else:
#     print('Hasło nie spełnia wymagań!')

# # Zadanie 3
# def l(a:int,b:int,c:int):
#     d = []
#     for i in range(b,c+1):
#         d.append(b)
#         b=b+1
#     for i in range (0, a):
#         random.shuffle(d)
#         print(d)



# x = int(input('Wprowadź liczbę zakładów: '))
# while (x<=0):
#     print('Błąd, podaj liczbę większą od 0')
#     x = int(input('Wprowadź liczbę zakładów: '))

# y = int(input('Wprowadź początek przedziału: '))
# z = int(input('Wprowadź koniec przedziału: '))
# l(x,y,z,)
