"""
Database Models for the Service Provider Directory

This module defines the SQLAlchemy models for the application.
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Provider(db.Model):
    """
    SQLAlchemy model representing a Service Provider.

    Attributes:
        id (int): Primary key.
        name (str): Full name of the service provider.
        trade (str): The primary profession or trade (e.g., Plumber, Developer).
        phone (str): Contact phone number.
        email (str): Contact email address.
        photo_url (str): URL pointing to the provider's profile picture.
        location (str): General location or service area.
        experience_years (int): Total years of professional experience.
        is_verified (bool): Verification status flag.
        starting_rate (float): Minimum hourly or project rate.
        bio (str): Detailed biography and description of services.
        reviews (list): A list of Review objects associated with this provider.
    """
    __tablename__ = 'providers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    trade = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(50))
    email = db.Column(db.String(120))
    linkedIn_url = db.Column(db.String(255))
    github_url = db.Column(db.String(255))
    photo_url = db.Column(db.String(255))
    location = db.Column(db.String(100))
    experience_years = db.Column(db.Integer)
    is_verified = db.Column(db.Boolean, default=False)
    starting_rate = db.Column(db.Float)
    bio = db.Column(db.Text)

    # Relationship to reviews. If a provider is deleted, their reviews are also deleted.
    reviews = db.relationship('Review', backref='provider', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        """
        Converts the Provider object into a JSON-serializable dictionary.

        Returns:
            dict: The dictionary representation of the provider.
        """
        return {
            "id": self.id,
            "name": self.name,
            "trade": self.trade,
            "phone": self.phone,
            "email": self.email,
            "linkedIn_url": self.linkedIn_url,
            "github_url": self.github_url,
            "photo_url": self.photo_url,
            "location": self.location,
            "experience_years": self.experience_years,
            "is_verified": self.is_verified,
            "starting_rate": self.starting_rate,
            "bio": self.bio
        }

class Review(db.Model):
    """
    SQLAlchemy model representing a Review submitted for a Provider.

    Attributes:
        id (int): Primary key.
        pro_id (int): Foreign key linking to the associated Provider.
        rating (int): A rating out of 5.
        comment (str): The written feedback from the reviewer.
        ip_address (str): The IP address of the reviewer to prevent duplicates.
    """
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    pro_id = db.Column(db.Integer, db.ForeignKey('providers.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    ip_address = db.Column(db.String(45))

    def to_dict(self):
        """
        Converts the Review object into a JSON-serializable dictionary.

        Returns:
            dict: The dictionary representation of the review.
        """
        return {
            "id": self.id,
            "pro_id": self.pro_id,
            "rating": self.rating,
            "comment": self.comment
        }
