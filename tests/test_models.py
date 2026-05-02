import pytest
from models import Provider, Review

def test_provider_model(init_database):
    """Test that the Provider model instantiates and saves correctly."""
    pro = Provider.query.filter_by(name="Test Engineer").first()
    
    assert pro is not None
    assert pro.trade == "Automated Tester"
    assert pro.is_verified is True
    assert pro.starting_rate == 100.0

def test_provider_to_dict(init_database):
    """Test the to_dict method of the Provider model."""
    pro = Provider.query.filter_by(name="Test Engineer").first()
    pro_dict = pro.to_dict()
    
    assert isinstance(pro_dict, dict)
    assert pro_dict["name"] == "Test Engineer"
    assert pro_dict["trade"] == "Automated Tester"

def test_review_model_relationship(init_database):
    """Test the relationship between Review and Provider models."""
    pro = Provider.query.filter_by(name="Test Engineer").first()
    
    # Provider should have 1 review from the init_database fixture
    assert len(pro.reviews) == 1
    
    review = pro.reviews[0]
    assert review.rating == 5
    assert review.comment == "100% test coverage!"
    assert review.provider.name == "Test Engineer"

def test_review_to_dict(init_database):
    """Test the to_dict method of the Review model."""
    review = Review.query.first()
    review_dict = review.to_dict()
    
    assert isinstance(review_dict, dict)
    assert review_dict["rating"] == 5
    assert "id" in review_dict
