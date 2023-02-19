from node import Node

class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def push(self, elem):

        node = Node(elem)
        if self.first is None:
            self.first = node

        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node
        
    def pop(self):
        if self.first is not None:
            elem = self.first.data
            self.first = self.first.next
            return elem

        raise IndexError("The stack is empty")
        
    def peek(self):
        
        if self.first:
            return self.first.data
        raise IndexError('The stack is empty')

    def __len__(self):
        return self._size

    def __repr__(self):
        r = ""
        pointer = self.first
        while pointer:
            r = r + str(pointer.data) + ''
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()



if __name__ == '__main__':

    lista = LinkedList()
    lista.append(3)
    lista.append(5)
    lista.append(7)
    print(len(lista))