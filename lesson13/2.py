"""
Создать класс BookCard, в классе должны быть:

- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title, year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Для года
  издания дополнительно проверить на валидность (> 0, <= текущего года).

Аксессоры реализоваться через property.
"""

from datetime import date

CURRENT_YEAR = date.today().year

class BookCard:
    def __init__(self, author: str, title: str, year: str):
        """
        init для объекта BookCard.

        :param author: автор книги
        :param title: название книги
        :param year: год издания
        """
        self._author = author
        self._title = title
        self._year = year

    # геттер автора
    @property
    def author(self) -> str:
        return self._author
    
    # сеттер автора
    @author.setter
    def author(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Автор должен быть строкой")
        self._author = value

    # геттер названия
    @property
    def title(self) -> str:
        return self._title
    
    # сеттер названия
    @title.setter
    def title(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Название должно быть строкой")
        self._title = value

    # геттер года издания
    @property
    def year(self) -> str:
        return self._year
    
    # сеттер года издания
    @year.setter
    def year(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Год издания должен быть целым числом")
        if value <= 0 or value > CURRENT_YEAR:
            raise ValueError(f"Год издания должен быть больше 0"
                             f" и не больше {CURRENT_YEAR}")
        self._year = value

    # методы сортировки
    def __lt__(self, other):
        if not isinstance(other, BookCard):
            raise TypeError("Сравнение возможно только с объектами Bookcard")
        return self.year < other.year
    
    def __le__(self, other):
        if not isinstance(other, BookCard):
            raise TypeError("Сравнение возможно только с объектами Bookcard")
        return self.year <= other.year
    
    def __gt__(self, other):
        if not isinstance(other, BookCard):
            raise TypeError("Сравнение возможно только с объектами Bookcard")
        return self.year > other.year
    
    def __ge__(self, other):
        if not isinstance(other, BookCard):
            raise TypeError("Сравнение возможно только с объектами Bookcard")
        return self.year >= other.year
    
    def __eq__(self, other):
        if not isinstance(other, BookCard):
            raise TypeError("Сравнение возможно только с объектами Bookcard")
        return self.year == other.year
    
    def __ne__(self, other):
        if not isinstance(other, BookCard):
            raise TypeError("Сравнение возможно только с объектами Bookcard")
        return self.year != other.year
    
# Проверка
if __name__ == "__main__":
    book1 = BookCard("Мартин", "Игра престолов", 2019)
    book2 = BookCard("Толкин", "Сильмариллион", 2016)
    book3 = BookCard("Желязны", "Хроники Амбера", 2022)

    print(book1.year) # 2016
    print(book2.year) # 2019

    book1.year = 2010
    print(book1.year) # стало 2010

    print(book1 < book2) # True
    print(book1 > book2) # False

    try:
        book1.year = -1999 # неправильное значение года
    except ValueError as e:
        print(e) # пишет ошибку

    try:
        book1.year = "2010" # строка вместо целого числа
    except ValueError as e:
        print(e) # пишет ошибку

    # сортировка
    books = [book1, book2, book3]
    for book in sorted(books):
        print(f"Автор: {book.author}, Название: {book.title}, "
              f"Год: {book.year}")