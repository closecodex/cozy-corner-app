from services.book_service import search_books

def test_books_page_initial_load(client):
    response = client.get("/books")
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert "choose a genre" not in html.lower()  # It's an empty form

def test_books_submit_empty_genre(client):
    response = client.post("/books", data={"genre": "", "keywords": "magic"})
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert "Please choose a genre" in html

def test_books_suggestions_from_database(client):
    response = client.post("/books", data={"genre": "fantasy", "keywords": ""})
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    # The output should contain books from the internal database
    # Since we can't reliably predict the exact book, we just check no errors and results exist.
    assert "No matches found" not in html
    assert "Please choose a genre" not in html

def test_search_books_returns_valid_fields():
    results = search_books("fantasy", "")
    assert isinstance(results, list)
    assert len(results) > 0
    for book in results:
        assert "title" in book
        assert "author" in book
        assert "description" in book
        assert len(book["title"]) > 0

def test_book_empty_search_no_crash(client):
    # Passing empty fields for both
    response = client.post("/books", data={"genre": "", "keywords": ""})
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert "Please choose a genre" in html
