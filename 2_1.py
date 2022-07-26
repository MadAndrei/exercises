# -*- coding: utf-8 -*-

class RingBuffer:
    def __init__(self, buffer_size):
        if not isinstance(buffer_size, int):
            raise TypeError("Размер буфера должен быть целым числом")
        if buffer_size <= 0:
            raise ValueError("Размер буфера должен быть положительным числом")

        self.__buffer_size = buffer_size
        self.__buffer = [None] * buffer_size
        self.__start_index = self.__end_index = 0
        self.__is_empty = True # Переменная, которая позволяет отдельно обрабатывать пустой буфер

    def push(self, elem):
        if self.__end_index == self.__start_index:
            if not self.__is_empty:
                raise IndexError("Буфер переполнен")
            self.__is_empty = False

        self.__buffer[self.__end_index] = elem
        self.__end_index += 1
        if self.__end_index == self.__buffer_size:
            self.__end_index = 0

    def pop(self):
        if self.__is_empty:
            raise IndexError("Буфер пуст")

        deleted_value = self.__buffer[self.__start_index]

        self.__buffer[self.__start_index] = None
        self.__start_index += 1
        if self.__start_index == self.__buffer_size:
            self.__start_index = 0

        if self.__start_index == self.__end_index:
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
    
# В первой версии хранение буфера реализовано через list фиксированного размера, а взаимодействие с элементами
# происходит через индексы начала и конца буфера.

# Плюсы: удобнее реализовывать (в процессе разработки можно легко посмотреть что лежит в списке),
# Работает значительно быстрее, использует меньше памяти.
