import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_add_exists_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 5)
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 5

    def test_set_book_rating_no_book_not_setted(self):
        collector = BooksCollector()
        collector.set_book_rating('Гордость и предубеждение и зомби', 5)
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == None

    def test_get_book_rating_exist_book_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 5)
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 5

    def test_get_books_with_specific_rating_valid_rating_valid_films(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 5)
        collector.add_new_book('Кот Джек')
        collector.set_book_rating('Кот Джек', 5)
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 6)

        result = collector.get_books_with_specific_rating(5)
        assert len(result) == 2

    def test_get_books_rating_two_books_len_two(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 5)
        collector.add_new_book('Кот Джек')
        collector.set_book_rating('Кот Джек', 6)

        result = collector.get_books_rating()
        assert len(result) == 2

    def test_add_book_in_favorites_book_exists_book_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        result = collector.get_list_of_favorites_books()

        assert len(result) == 1

    def test_delete_book_from_favorites_book_in_favorites_book_removed(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        result = collector.get_list_of_favorites_books()

        assert len(result) == 0

    def test_get_list_of_favorites_books_two_books_in_favorites_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_new_book('Кот Джек')
        collector.add_book_in_favorites('Кот Джек')

        result = collector.get_list_of_favorites_books()

        assert len(result) == 2
