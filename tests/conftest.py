import os
import pytest
from app import create_app

@pytest.fixture
def app():
    # Pass testing config via environment or directly
    app = create_app()
    app.config.update({
        "TESTING": True,
        # Use an in-memory database for testing
        "DATABASE_PATH": ":memory:",
    })
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
