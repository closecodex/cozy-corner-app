def test_puzzle_page_loads(client):
    response = client.get("/puzzle")
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    # Test default image is present
    assert "puzzle_default.jpg" in html
    # Test puzzle size options (12 / 20 / 30) are available
    assert "12" in html
    assert "20" in html
    assert "30" in html
