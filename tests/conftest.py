import os
import pytest

# CRITICAL: Set the DATABASE_URL to an in-memory SQLite database
# *BEFORE* importing the Flask app. This prevents tests from modifying the real Neon DB.
os.environ["DATABASE_URL"] = "sqlite:///:memory:"

from main import app as flask_app
from models import db, Provider, Review

@pytest.fixture
def app():
    """Provides the Flask application instance."""
    yield flask_app

@pytest.fixture
def client(app):
    """Provides a test client for making HTTP requests."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """Provides a CLI runner for testing Flask CLI commands."""
    return app.test_cli_runner()

@pytest.fixture
def init_database(app):
    """
    Sets up a clean database and inserts dummy data before each test.
    Cleans up after the test finishes.
    """
    with app.app_context():
        # Clear existing tables (just in case) and create them fresh
        db.drop_all()
        db.create_all()

        # Insert Mock Provider
        provider = Provider(
            name="Jack Reacher",
            trade="Senior Software Engineer",
            bio="I test code automatically.",
            is_verified=True,
            starting_rate=100.0,
            location="Nicaragua",
            phone="+50588993344",
            email="jack@fakepeople.com"
        )
        db.session.add(provider)
        db.session.commit()

        # Insert Mock Review
        review = Review(
            pro_id=provider.id,
            rating=5,
            comment="I highly recommend him for web development",
            ip_address="127.0.0.1"
        )
        db.session.add(review)
        db.session.commit()

        yield db  # Testing happens here

        # Teardown
        db.session.remove()
        db.drop_all()
