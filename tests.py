import pytest

from main import BooksCollector

@pytest.fixture(scope='function')
def collector():
    return BooksCollector()

@pytest.mark.parametrize ('book_name', ['Маленький принц','Гарри Поттер'])
def test_add_new_book(collector, book_name):
    collector.add_new_book(book_name)
    assert collector.get_books_genre()[book_name] == ''

@pytest.mark.parametrize('invalid_name', ['', 'А' * 41])
def test_add_new_book_invalid_names(collector, invalid_name):
    collector.add_new_book(invalid_name)
    assert invalid_name not in collector.get_book_genre()

def test_set_and_get_book_genre(collector):
    collector.add_new_book('Книга')
    collector.set_book_genre('Книга', 'Фантастика')
    assert collector.get_books_genre('Книга') == 'Фантастика'

def test_set_book_genre_invalid(collector):
    collector.add_new_book('Книга')
    collector.set_book_genre('Книга', 'Неизвестный жанр')
    assert collector.get_books_genre('Книга') == ''

def test_get_books_with_specific_genre(collector):
    collector.add_new_book('Книга 1')
    collector.add_new_book('Книга 2')
    collector.set_book_genre('Книга 1', 'Фантастика')
    collector.set_book_genre('Книга 2', 'Ужасы')
    assert collector.get_books_with_specific_genre('Фантастика') == ['Книга 1']

def test_get_books_for_children_excludes_age_restricted(collector):
    collector.add_new_book('Детская')
    collector.set_book_genre('Детская', 'Комедии')
    collector.add_new_book('Ужастик')
    collector.set_book_genre('Ужастик','Ужасы')
    assert collector.get_books_for_children() == ['Детская']

def test_add_book_in_favorites_once(collector):
    collector.add_new_book('Книга')
    collector.add_book_in_favorites('Книга')
    collector.add_book_in_favorites('Книга')
    assert collector.get_list_of_favorites_books() == ['Книга']

def test_delete_book_from_favorites(collector):
    collector.add_new_book('Книга')
    collector.add_book_in_favorites('Книга')
    collector.delete_book_from_favorites('Книга')
    assert collector.get_list_of_favorites_books() == []

def test_get_list_of_favorites_books(collector):
    collector.add_new_book('Книга 1')
    collector.add_new_book('Книга 2')
    collector.add_book_in_favorites('Книга 1')
    collector.add_book_in_favorites('Книга 2')
    assert set(collector.get_list_of_favorites_books()) == {'Книга 1', 'Книга 2'}
