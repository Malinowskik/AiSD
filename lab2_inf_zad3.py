from lab2_inf_zad1 import LinkedList


class Queue:
    def __init__(self):
        self.storage = LinkedList()

    def enqueue(self, element):
        return self.storage.append(element)

    def len(self):
        return self.storage.len()

    def peek(self):
        i = self.storage.head.value
        return i

    def dequeue(self):
        return self.storage.pop()

    def print(self):
        return self.storage.print()



que = Queue()
que.enqueue(2)
que.enqueue(3)
que.enqueue(4)
que.enqueue(5)
que.enqueue(6)

print(que.peek())
# print(que.dequeue())
que.print()
