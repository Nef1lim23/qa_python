**# README.md**

**Тестирование класса для работы с жанрами и книгами**

В этом документе описаны тесты, которые проверяют функциональность класса для работы с жанрами и книгами. Каждый тест включает в себя краткое описание его цели.

**1. test_init_add_new_genre_added_new_genre**  
Проверяет, что при инициализации класса можно добавить новый жанр в список `genre`.

**2. test_add_new_books**  
Проверяет, что метод `add_new_book` добавляет книгу в словарь `books_genre`.

**3. test_set_book_genre_one_book_added_genre**  
Проверяет, что метод `set_book_genre` правильно присваивает жанр книге.

**4. test_get_book_genre_one_genre_genre_received**  
Проверяет, что метод `get_book_genre` возвращает правильный жанр для книги.

**5. test_get_books_with_specific_genre_three_books_get_two_books**  
Проверяет, что метод `get_books_with_specific_genre` возвращает список книг с указанным жанром.

**6. test_get_books_genre_two_books_with_genre_two_books_in_dictionary**  
Проверяет, что словарь `books_genre` содержит книги с правильными жанрами.

**7. test_get_books_for_children_three_books_one_has_been_added**  
Проверяет, что метод `get_books_for_children` возвращает список книг, которые подходят для детей.

**8. test_add_book_in_favorites_two_books_books_added**  
Проверяет, что метод `add_book_in_favorites` добавляет две книги в список `favorites` и возвращает список из двух книг.

**9. test_delete_book_from_favorites_two_book_one_was_deleted**  
Проверяет, что метод `delete_book_from_favorites` удаляет одну книгу из списка `favorites` и возвращает список, содержащий только оставшуюся книгу.

**10. test_get_list_of_favorites_books_received_list**  
Проверяет, что метод `get_list_of_favorites_books` возвращает список с добавленными в него книгами.
