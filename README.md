Тесты для проекта BooksCollector Этот файл содержит описание автоматических тестов, покрывающих функциональность класса BooksCollector. Тесты написаны с использованием pytest и используют фикстуру collector() для создания нового экземпляра класса в каждом тесте. 

Фикстура
python
@pytest.fixture(scope='function')
def collector():
    return BooksCollector()

test_add_new_book
Что проверяет:

Книга с допустимым названием добавляется в словарь books_genre.
У книги по умолчанию пустой жанр ('')

test_add_new_book_invalid_names
Что проверяет:

Книга с недопустимым названием (пустая строка или длина > 40 символов) не добавляется в словарь books_genre.


test_set_and_get_book_genre
Что проверяет:

Установленный жанр сохраняется для книги.
Метод get_book_genre корректно возвращает этот жанр.

test_set_book_genre_invalid
Что проверяет:

Если жанр не входит в список допустимых (genre), он не устанавливается.
Жанр книги остаётся пустым ('').

test_get_books_with_specific_genre
Что проверяет:

Метод get_books_with_specific_genre возвращает список книг, у которых установлен указанный жанр.

test_get_books_for_children_excludes_age_restricted
Что проверяет:

Книги с жанрами из списка genre_age_rating не попадают в результат get_books_for_children.
Возвращаются только безопасные для детей книги.

test_add_book_in_favorites_once
Что проверяет:

Книга добавляется в favorites только один раз, даже при повторных попытках.

test_delete_book_from_favorites
Что проверяет:

Книга корректно удаляется из списка избранных, если она там была.

test_get_list_of_favorites_books
Что проверяет:

Метод get_list_of_favorites_books возвращает полный список избранных книг после добавления нескольких.

