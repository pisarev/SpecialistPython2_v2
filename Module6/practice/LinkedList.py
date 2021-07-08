class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.__count = 0
        self.__index = -1

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = 'LinkedList [' + str(current.value) + (',' if current.next is not None else '')
            while current.next is not None:
                current = current.next
                out += str(current.value) + (',' if current.next is not None else '')
            return out + ']'
        return 'LinkedList []'

    @property
    def count(self):
        return self.__count

    def clear(self):
        current = self.first
        while current.next is not None:
            temp = current
            current = current.next
            del temp
        self.__init__()

    def add(self, value):
        """
        Добавляем новое значение value в конец списка
        """
        new_node = Node(value, None)  # Создаем новый узел
        if self.first is None:  # Если список был пуст
            # self.first и self.last будут указывать на один и тотже узел, т.к. он единственный
            self.last = new_node
            self.first = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.__count += 1

    def push(self, value):
        """
        Добавляет элемент со значением value в начало списка
        """
        if self.first is None:  # Если список был пуст
            # self.first и self.last будут указывать на один и тотже узел
            self.last = self.first = Node(value, None)
        else:
            new_node = Node(value, self.first)
            self.first = new_node
        self.__count += 1

    def insert(self, value, index):
        i = 0
        prev = None
        next = None
        while True:
            if next is None:
                next = self.first
            else:
                next = next.next

            if i == index:
                new_node = Node(value, next)
                if prev is None:
                    self.first = new_node
                else:
                    prev.next = new_node
                if next is None:
                    self.last = new_node
                return
            i += 1

            prev = next
            if prev is None and next is None:
                break
        self.__count += 1

    def find(self, value):
        current = self.first
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    def len(self):
        return self.count
        """
        # TODO: сделать более быструю реализацию, т.к. каждый раз проходка по всем элементам - долго
        length = 0
        if self.first is not None:
            current = self.first
            while current.next is not None:
                current = current.next
                length += 1
        return length + 1  # +1 для учета self.first
        """
    def __iter__(self):
        self.__index = -1
        return self
    def __next__(self):
        self.__index += 1
        i = 0
        current = self.first
        while current is not None:
            if i == self.__index:
                break
            i += 1
            current = current.next
        if current is None:
            raise StopIteration
        return current
    def __getitem__(self, index):
        i = 0
        current = self.first
        while current is not None:
            if i == index:
                break
            i += 1
            current = current.next
        if current is None:
            raise IndexError
        return current

if __name__ == "__main__":
    L = LinkedList()
    print("empty list = ", L)
    L.add(1)
    L.add(2)
    L.add(3)

    print("list = ", L)

    L.insert(100, 3)

    print("list = ", L)
    print(L.find(100))

    # L.clear()

    print("list = ", L)

    for value in L:
        print(value.value)

    L[1].value = 444
    L[2].value = 555

    for value in L:
        print(value.value)
""""
    # TODO: реализовать интерфейс итерации
    # for el in L:
    #     print(el)
    # Напомню принцип работы итератора:
    # iterator_L = iter(L) L.__iter__()
    # next(iterator_L) it.__next__()
    # next(iterator_L)
    # next(iterator_L)
    # next(iterator_L)

    # TODO: реализовать обращение по индексу и изменение значение по индексу
    # print(L[0])
    # L[0] = "new"
    # print(L[0])

    # TODO: реализовать создание нового списка с задание начальных элементов
    # L = LinkedList(2, 4, 6, -12)
    # print(L)
"""
