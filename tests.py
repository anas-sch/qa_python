import pytest

class TestBooksCollector:

    @pytest.mark.parametrize ('book_name', ['Маленький принц','Гарри Поттер'])
    def test_add_new_book_adds_to_collection(self, collector, book_name):
           collector.add_new_book(book_name)
           assert book_name in collector.get_books_genre()

    @pytest.mark.parametrize('invalid_name', ['', 'А' * 41])
    def test_add_new_book_invalid_names(self, collector, invalid_name):
        collector.add_new_book(invalid_name)
        assert invalid_name not in collector.get_books_genre()

    def test_get_book_genre_returns_empty_for_new_book(self, collector):
        collector.add_new_book('Новая книга')
        assert collector.get_book_genre('Новая книга') == ''

    def test_set_book_genre_invalid(self, collector):
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Неизвестный жанр')
        assert collector.get_book_genre('Книга') == ''

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 1', 'Фантастика')
        collector.set_book_genre('Книга 2', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Книга 1']

    def test_get_books_for_children_excludes_age_restricted(self, collector):
        collector.add_new_book('Детская')
        collector.set_book_genre('Детская', 'Комедии')
        collector.add_new_book('Ужастик')
        collector.set_book_genre('Ужастик','Ужасы')
        assert collector.get_books_for_children() == ['Детская']

    def test_add_book_in_favorites_once(self, collector):
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.add_book_in_favorites('Книга')
        assert collector.get_list_of_favorites_books() == ['Книга']

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.delete_book_from_favorites('Книга')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_book_in_favorites('Книга 1')
        collector.add_book_in_favorites('Книга 2')
        assert set(collector.get_list_of_favorites_books()) == {'Книга 1', 'Книга 2'}

    def test_get_books_genre_shows_current_genres(self, collector):
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Детективы')
        assert collector.get_books_genre()['Книга'] == 'Детективы'

