import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    def test_init_add_new_genre_added_new_genre(self):
        collector = BooksCollector()
        collector.genre.append('Документалка')
        assert collector.genre[-1] == 'Документалка'

    @pytest.mark.parametrize('name', ['Гарри Поттер и Филосовский камень',
                                      '1894',
                                      'Гарри Поттер и Узник Азкабана'])
    def test_add_new_books(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.books_genre

    def test_set_book_genre_one_book_added_genre(self):
        collector = BooksCollector()

        collector.add_new_book("Ржавый котел")
        collector.set_book_genre('Ржавый котел', 'Фантастика')

        assert collector.books_genre == {'Ржавый котел': 'Фантастика'}

    def test_get_book_genre_one_genre_genre_received(self):
        name_genre = 'Гарри Поттер и Узник Азкабана'
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер и Узник Азкабана')
        collector.set_book_genre('Гарри Поттер и Узник Азкабана', 'Фантастика')

        assert collector.get_book_genre(name_genre) == 'Фантастика'

    def test_get_books_with_specific_genre_three_books_get_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер и Узник Азкабана')
        collector.set_book_genre('Гарри Поттер и Узник Азкабана', 'Фантастика')

        collector.add_new_book('Гарри Поттер и Орден Феникса')
        collector.set_book_genre('Гарри Поттер и Орден Феникса', 'Фантастика')

        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Гарри Поттер и Узник Азкабана',
                                                                         'Гарри Поттер и Орден Феникса']

    def test_get_books_genre_two_books_with_genre_two_books_in_dictionary(self):
        collector = BooksCollector()

        collector.add_new_book('Лжец')
        collector.set_book_genre('Лжец', 'Комедии')

        collector.add_new_book('Доктор Сон')
        collector.set_book_genre('Доктор Сон', 'Ужасы')

        assert collector.get_books_genre() == {'Лжец': 'Комедии',
                                         'Доктор Сон': 'Ужасы'}

    def test_get_books_for_children_three_books_one_has_been_added(self):
        collector = BooksCollector()

        collector.add_new_book('Доктор Сон')
        collector.set_book_genre('Доктор Сон', 'Ужасы')

        collector.add_new_book('Последнее дело Холмса')
        collector.set_book_genre('Последнее дело Холмса', 'Детективы')

        collector.add_new_book('Гарри Поттер и Узник Азкабана')
        collector.set_book_genre('Гарри Поттер и Узник Азкабана', 'Фантастика')

        assert collector.get_books_for_children() == ['Гарри Поттер и Узник Азкабана']

    def test_add_book_in_favorites_two_books_books_added(self):
        collector = BooksCollector()

        collector.add_new_book('Доктор Сон')
        collector.add_new_book('Последнее дело Холмса')

        collector.add_book_in_favorites('Доктор Сон')
        collector.add_book_in_favorites('Последнее дело Холмса')
        collector.add_book_in_favorites('Адский рай')

        assert collector.favorites == ['Доктор Сон', 'Последнее дело Холмса']

    def test_delete_book_from_favorites_two_book_one_was_deleted(self):
        collector = BooksCollector()

        collector.add_new_book('Доктор Сон')
        collector.add_new_book('Последнее дело Холмса')

        collector.add_book_in_favorites('Доктор Сон')
        collector.add_book_in_favorites('Последнее дело Холмса')

        collector.delete_book_from_favorites('Доктор Сон')

        assert collector.favorites == ['Последнее дело Холмса']

    def test_get_list_of_favorites_books_received_list(self):
        collector = BooksCollector()

        collector.add_new_book('Доктор Сон')
        collector.add_new_book('Последнее дело Холмса')

        collector.add_book_in_favorites('Доктор Сон')
        collector.add_book_in_favorites('Последнее дело Холмса')

        assert collector.get_list_of_favorites_books() == ['Доктор Сон', 'Последнее дело Холмса']