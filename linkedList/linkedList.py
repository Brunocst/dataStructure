from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0


    def append(self, elem):
        if self.head:
            pointer = self.head
            while pointer.next :
                pointer = pointer.next
            pointer.next = Node(elem)

        else:
            self.head = Node(elem)
        self._size = self._size+1

    def __len__(self):
        return self._size

    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        return pointer

    def set(self, index):
        return

    def __getitem__(self, index):
        pointer = self._getnode(index)
        if pointer:
            return pointer.data
        raise IndexError

    def __setitem__(self, index, elem):
        pointer = self._getnode(index)
        if pointer:
            pointer.data = elem
        else:
            raise IndexError

    def index(self, elem):
        pointer = self.head
        i=0
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i = i+1
        raise ValueError(f"{elem} is not in list")

    def insert(self, index, elem):
        node = Node(elem)
        if index == 0:
            node.next = self.head()
            self.head = node
        else:
            pointer = self._getnode(index-1)
            node.next = pointer.next
            pointer.next = node
        self._size = self._size + 1

    def remove(self, elem):

        if self.head is None:
            raise ValueError(f"{elem} is not in list")

        elif self.head.data == elem:
            self.head = self.head.next
            self._size = self._size - 1
            return True

        else:
            node_a = self.head
            pointer = self.head.next
            while pointer:
                if pointer.data == elem:
                    node_a.next = pointer.next
                    
                node_a = pointer
                pointer = pointer.next
            self._size = self._size - 1
            return True

        raise ValueError(f"{elem} is not in list")

    def __repr__(self):
        r = ""
        pointer = self.head
        while pointer:
            r = r + str(pointer.data) + '->'
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


