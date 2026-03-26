from services.drawing_prompt_service import generate_prompt, init_db, save_prompt_if_new, get_recent_prompts
import os

def test_drawing_prompt_page_loads(client):
    response = client.get("/drawing-prompt")
    assert response.status_code == 200
    assert b"Draw" in response.data

def test_generate_prompt_returns_text():
    prompt = generate_prompt()
    assert isinstance(prompt, str)
    assert len(prompt) > 0
    assert "Draw" in prompt
    assert "style" in prompt

def test_recent_prompts_empty(app):
    # Test empty state doesn't crash
    # Using the in-memory DB defined in conftest
    with app.app_context():
        # DB path is :memory:, so we need to initialize it locally for this test
        # Actually generate_prompt and others manually take a path
        init_db(":memory:")
        prompts = get_recent_prompts(":memory:")
        assert isinstance(prompts, list)
        assert len(prompts) == 0
