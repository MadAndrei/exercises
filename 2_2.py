# -*- coding: utf-8 -*-

class Element:
    def __init__(self, value):
        self.value = value
        self.next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, elem):
        self.__next = elem

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class RingBuffer:
    def __init__(self, buffer_size):
        if not isinstance(buffer_size, int):
            raise TypeError("Размер буфера должен быть целым числом")
        if buffer_size <= 0:
            raise ValueError("Размер буфера должен быть положительным числом")
        self.__start = Element(None)
        first_elem = self.__start
        for _ in range(buffer_size - 1):
            tmp = Element(None)
            self.__start.next = tmp
            self.__start = tmp
        self.__start.next = first_elem
        self.__end = self.__start
        self.__is_empty = True # Переменная, которая позволяет отдельно обрабатывать пустой буфер

    def push(self, value):
        if self.__start == self.__end:
            if not self.__is_empty:
                raise IndexError("Буфер переполнен")
            self.__is_empty = False
        self.__end.value = value
        self.__end = self.__end.next

    def pop(self):
        if self.__is_empty:
            raise IndexError("Буфер пуст")
        deleted_value = self.__start.value
        self.__start.value = None
        self.__start = self.__start.next
        if self.__start == self.__end:
            self.__is_empty = True
        return deleted_value


def test():
    rb = RingBuffer(3)
    rb.push(5)
    rb.push(7)
    print rb.pop()
    print rb.pop()
    rb.push(1)
    rb.push(2)
    rb.push(3)
    print rb.pop()
    rb.push(4)
    print rb.pop()
    print rb.pop()
    print rb.pop()


if __name__ == '__main__':
    test()


# Во второй версии хранение буфера реализовано через собственный класс Element 
# (каждый объект класса хранит ссылку на следующий элемент буфера по кругу),
# а взаимодействие происходит через ссылки на первый и последний элемент буфера.

# Плюсы: более гибкая реализация.
