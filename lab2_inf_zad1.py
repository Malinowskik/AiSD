from typing import Any
class Node:
    def __init__(self, value=Any, next=Any):
        self.value = value   # tzw head, czyli początkowy węzeł
        self.next = next    # kolejny węzeł

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, element): #funkcja dodająca pierwszy element(węzeł)
        node = Node(element, self.head)
        self.head = node

    def append(self, element): #funkcja dodająca wezel na koncu listy
        if self.head is None: #sprawdzamy czy lista posiada pierwszy węzeł, jezeli nie - dodajemy węzeł na początku listy
            node = Node(element, None)
            self.head = node
            return
        i = self.head
        # w pozostałych przypadkach dodajemy na końcu
        while i.next: #póki kolejne pozycje są zajęte przechodzimy do następnej
            i = i.next
        #po uzyskaniu pustego miejsca przypisujemy do niego nowy węzeł
        i.next = Node(element, None)


    def print(self): #funkcja wypisująca wartości wskazanej listy
        i = self.head
        linked_list = str(i.value)
        i = i.next
        while i: #funkcja while będzie działać póki self.head posiada inną wartość niż None
            linked_list += ' --> ' + str(i.value) #do zmiennej dopisujemy wartość danego węzła jako string
            i = i.next  #jeżeli następny węzeł będzie pusty self.head otrzyma wartość None
        print(linked_list)

    def print_k(self): #funkcja wypisująca wartości wskazanej listy (każda wartośc w nowych wierszu)
        i = self.head
        while i:
            print(i.value)
            print('^')
            i = i.next

    def len(self): #funkcja sprawdzająca długość listy
        i = self.head
        count = 0
        while i:
            count += 1 # za każdym razem kiedy sprawdzany węzeł nie jest pusty licznik wzrasta o 1
            i = i.next
        return count #zwrocenie licznika

    def node(self, index): #funcka zwracająca węzeł znajdujacy sie na wskazanej pozycji
        i = self.head
        count = 0
        value = ''
        while i:  #pętla "przemieszcza" się po kojenych węzłach
            if count == index: # póki licznik i wskazany index nie będą sobie równe
                value = i.value #po spełnieniu warunku
            count += 1
            i = i.next
        return print('Wartośc wskazanego indexu: ', value)

    def insert(self, index, element): #funckja wstawiająca nowy węzeł po wskazanym parametrze
        if self.head is None: #warunek sprawdzający czy lista nie jest pusta
            print('Błąd, wskazana lista jest pusta!')
            return

        if index > (self.len()-1): # warunek sprawdzający czy wskazany index nie wykracza poza listę (z wykorzystaniem
            #  funkcji length
            print('Błąd, index wykracza poza listę!')
            return

        i = self.head
        count = 0
        while i:
            if count == index: #warunek zatrzymujący się na wskazanym indexie, po za trzymaniu się dodajemy podany węzeł jako następny
                i.next = Node(element, i.next) #w raznie licznik nie jest równy indexowi, licznik wzrasta o 1 i sprawdza kolejny raz warunek if
                break
            i = i.next
            count += 1
    def pop(self): #funcja usuwa pierwszy węzeł i zwraca wartość tego węzła
        if self.head is None:
            print('Błąd, brak pierwszego elementu - lista jest pusta!')
            return
        value = self.head.value
        self.head = self.head.next
        return value

    def remove_last(self): #funkcja usuwa ostatni węzeł
        i = self.head
        count = 0
        while i:
            if count == self.len()-2:
                i.next = i.next.next
                break
            i = i.next
            count += 1


    def remove(self, index): #funkcja usuwa wskazany węzeł
        i = self.head
        count = 0
        while i:
            if count == index:
                i.next = i.next.next
                break
            i = i.next
            count += 1


lista = LinkedList()
lista2 = LinkedList()
lista3 = LinkedList()
for i in range(10):
    lista3.append(i)
# lista3.print()
# lista3.remove_last()
lista3.print()
lista3.print()