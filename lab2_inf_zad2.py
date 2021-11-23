from lab2_inf_zad1 import LinkedList

class Stack:
    def __init__(self):
        self.storage = LinkedList()

    def push(self, element):
        self.storage.push(element)

    def pop(self):
        return self.storage.pop()

    def len(self):
        return self.storage.len()

    def print(self):
        return self.storage.print_k()


stack = Stack()
stack.push('pierwszy')
stack.push('drugi')
stack.push(3)
stack.push(43)
stack.push(463)
print(stack.len())
print(stack.pop())
stack.print()
