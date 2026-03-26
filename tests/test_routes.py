def test_home_page(client):
    # Arrange & Act
    response = client.get("/")
    # Assert
    assert response.status_code == 200

def test_dog_matcher_page(client):
    response = client.get("/dog-matcher")
    assert response.status_code == 200

def test_cat_corner_page(client):
    response = client.get("/cats")
    assert response.status_code == 200

def test_book_nook_page(client):
    response = client.get("/books")
    assert response.status_code == 200

def test_puzzle_time_page(client):
    response = client.get("/puzzle")
    assert response.status_code == 200

def test_daily_drawing_prompt_page(client):
    response = client.get("/drawing-prompt")
    assert response.status_code == 200

def test_about_me_page(client):
    response = client.get("/about")
    assert response.status_code == 200

def test_bonus_section_page(client):
    response = client.get("/bonus")
    assert response.status_code == 200
