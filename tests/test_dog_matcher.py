def test_dog_matcher_page_loads(client):
    response = client.get("/dog-matcher")
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert "How energetic are you" in html  # check that questions are rendered

def test_dog_matcher_submit_valid(client):
    # Valid answers based on dog_logic.py QUESTIONS
    data = {
        "energy": "low",
        "social": "shy",
        "routine": "chill",
        "mess": "tidy",
        "conflict": "avoid",
        "weather": "rain",
        "planning": "organized",
        "humor": "dry",
        "comfort": "blanket",
        "focus": "deep"
    }
    response = client.post("/dog-matcher", data=data)
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    
    # We should see a dog result (e.g. Border Collie, Cavalier, etc.)
    # Result must contain name, description, and an image path loosely verified by checking the img tag or text.
    assert "image_filename" not in html # make sure raw objects aren't printed
    assert "<img" in html
    assert ".svg" in html

def test_dog_matcher_submit_incomplete(client):
    data = {
        "energy": "low"
        # missing other fields
    }
    response = client.post("/dog-matcher", data=data)
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    
    # Handled gracefully, should show error message
    assert "Please answer all questions" in html

def test_dog_matcher_result_content():
    # Test the logic directly to ensure name, description, image path exist
    from services.dog_logic import evaluate_dog_match
    answers = {
        "energy": "high",
        "social": "outgoing",
        "routine": "adventure",
        "mess": "chaotic",
        "conflict": "popcorn",
        "weather": "snow",
        "planning": "spontaneous",
        "humor": "goofy",
        "comfort": "snacks",
        "focus": "scatter"
    }
    match = evaluate_dog_match(answers)
    assert hasattr(match, "name")
    assert hasattr(match, "description")
    assert hasattr(match, "image_filename")
    assert match.name
    assert match.description
    assert ".svg" in match.image_filename
