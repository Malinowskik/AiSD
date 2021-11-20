# # Zadanie 1 i 3
# class Square:
#     side : int
#     square : int
#     def __init__(self, side: int) -> None:
#         self.side = side
#         self.square = side * side
#
#     def area(self) -> int:
#         return self.side * self.side
#     def primeter(self) -> int:
#         return self.side * 4
#
# lista = []
# for i in range(0,10):
#     x = Square(i+10)
#     lista.append(x)
# for i in lista:
#     print(f'Pole kwadratu wynosi: {i.area()}, obwód kwadratu wynosi: {i.primeter()}')



# # Zadanie 2 i 3
# class Triangle:
#     side: float
#     height: float
#     def __init__(self, side: float, height: float) -> None:
#         self.side = side
#         self.height = height
#
#     def area(self) -> float:
#         return self.side * self.height / 2
#
#     def perimeter(self) -> float:
#         return self.side * 2 + self.height
#
# lista = []
# for i in range(0,25):
#     for i in range(0, 5):
#         x = Triangle(float(6+i),float(15+i))
#         lista.append(x)
# for i in lista:
#     print(f'Pole kwadratu wynosi: {i.area()}, obwód kwadratu wynosi: {i.perimeter()}')

# # Zadanie 4
# class Tree:
#     name: str
#     height: float
#     leafs: int
#     def __init__(self, name: str, height: float, leafs: int) -> None:
#         self.name = name
#         self.height = height
#         self.leafs = leafs
#
#
#
#     def grow_up(self, a) -> float:
#         self.height += a
#     def grow_wide(self, liscie) -> int:
#         self.leafs = liscie
#
#     def show(self) -> str:
#         return f'Nazwa drzewa: {self.name}, wysokość w metrach: {self.height}, liczba liści: {self.leafs}'
# drzewo1 = Tree('dąb', 15.6, 10)
# zmiana = float(input("Podaj o ile urosło drzewo (w metrach): "))
# nowe_liscie = int(input('Podaj nową liczbę liści: '))
# drzewo1.grow_up(zmiana)
# drzewo1.grow_wide(nowe_liscie)
# print(Tree.show(drzewo1))