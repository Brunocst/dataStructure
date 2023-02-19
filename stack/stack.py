from node import Node

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elem):
        
        node = Node(elem)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        
        if self.top:
            node = self.top
            self.top = self.top.next
            return self.top.data
        raise IndexError('The stack is empty')

    def peek(self):
        
        if self.top:
            return self.top.data
        raise IndexError('The stack is empty')

    def __len__(self):
        return self._size

    def __repr__(self):
        r = ""
        pointer = self.top
        while pointer:
            r = r + str(pointer.data) + '/n'
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