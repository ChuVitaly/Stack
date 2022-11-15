class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self): #  проверка стека на пустоту
        return self.items == []

    def push(self, item): # добавляет новый элемент(последний)
        self.items.append(item)

    def pop(self): # удаляет верхний элемент стека(последний)Стек изменяется
        return self.items.pop()

    def peek(self): # возвращает верхний элемент стека, но не удаляет его. Стек не меняется
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items) #  возвращает количество элементов в стеке


if __name__ == '__main__':
    a = Stack()
    print(a)
    print(a.__dict__)
