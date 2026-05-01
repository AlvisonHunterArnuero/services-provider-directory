"""
Service Provider Directory API

This module provides a Flask-based RESTful API and UI for a service provider directory.
It uses Flask-SQLAlchemy for database management and integrates with PostgreSQL via Neon Tech.
The application supports CRUD operations for service providers and allows visitors to
submit reviews, which are restricted to one per IP address.

Endpoints:
    GET  / : Renders the home page UI containing the list of all providers.
    GET  /api-docs : Renders the OpenAPI-style API documentation UI.
    GET  /profile/<int:pro_id> : Renders the detail page UI for a specific provider.
    
    GET  /providers : Returns a JSON list of all service providers.
    POST /providers : Creates a new service provider.
    GET  /providers/<int:pro_id> : Returns JSON data for a specific provider.
    PUT  /providers/<int:pro_id> : Updates an existing provider.
    DELETE /providers/<int:pro_id> : Deletes a provider and cascades to their reviews.
    
    GET  /providers/<int:pro_id>/reviews : Returns JSON list of reviews for a provider.
    POST /providers/<int:pro_id>/reviews : Submits a new review for a provider.
"""

import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure SQLAlchemy
# Ensure the database URL from .env is properly read.
db_url = os.environ.get("DATABASE_URL")
if db_url and db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)

if not db_url:
    raise ValueError("No DATABASE_URL set for Flask application")

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_pre_ping': True,
    'pool_recycle': 300,
}

from models import db, Provider, Review

db.init_app(app)

# Ensure database tables are created before processing first request
with app.app_context():
    db.create_all()

# --- UI Endpoints ---

@app.route('/', methods=['GET'])
def index():
    """
    Root route that queries all providers and renders the home page UI.
    
    Returns:
        Rendered HTML template 'index.html'.
    """
    providers = Provider.query.all()
    return render_template('index.html', providers=providers)

@app.route('/api-docs', methods=['GET'])
def api_docs():
    """
    API Documentation route that renders an OpenAPI-style page.
    
    Returns:
        Rendered HTML template 'api_docs.html'.
    """
    return render_template('api_docs.html')

@app.route('/profile/<int:pro_id>', methods=['GET'])
def profile(pro_id):
    """
    Profile route that renders detailed information and reviews for a specific provider.
    
    Args:
        pro_id (int): The unique identifier of the provider.
        
    Returns:
        Rendered HTML template 'profile.html' or a 404 error if not found.
    """
    pro = db.session.get(Provider, pro_id)
    if not pro:
        return "Provider not found", 404
    reviews = Review.query.filter_by(pro_id=pro_id).all()
    return render_template('profile.html', pro=pro, reviews=reviews)

# --- API Provider Endpoints ---

@app.route('/providers', methods=['GET'])
def get_all_providers():
    """
    Retrieve a list of all service providers.
    
    Returns:
        A JSON response containing a list of all providers and a 200 status code.
    """
    providers = Provider.query.all()
    return jsonify([p.to_dict() for p in providers]), 200

@app.route('/providers', methods=['POST'])
def add_pro():
    """
    Create a new service provider profile.
    
    Expects a JSON payload containing at least 'name' and 'trade'.
    
    Returns:
        A JSON response containing the newly created provider and a 201 status code,
        or a 400 status code if required fields are missing.
    """
    data = request.get_json()
    if not data or not data.get('name') or not data.get('trade'):
        return jsonify({"error": "Missing required fields: 'name' and 'trade'"}), 400
        
    new_pro = Provider(
        name=data.get('name'),
        trade=data.get('trade'),
        phone=data.get('phone'),
        email=data.get('email'),
        photo_url=data.get('photo_url'),
        location=data.get('location'),
        experience_years=data.get('experience_years'),
        is_verified=data.get('is_verified', False),
        starting_rate=data.get('starting_rate'),
        bio=data.get('bio')
    )
    
    db.session.add(new_pro)
    db.session.commit()
    
    return jsonify(new_pro.to_dict()), 201

@app.route('/providers/<int:pro_id>', methods=['GET'])
def get_pro(pro_id):
    """
    Retrieve detailed information for a specific provider.
    
    Args:
        pro_id (int): The unique identifier of the provider.
        
    Returns:
        A JSON response containing the provider's details and a 200 status code,
        or a 404 status code if the provider does not exist.
    """
    pro = db.session.get(Provider, pro_id)
    if not pro:
        return jsonify({"error": "Provider not found"}), 404
    return jsonify(pro.to_dict()), 200

@app.route('/providers/<int:pro_id>', methods=['PUT'])
def edit_pro(pro_id):
    """
    Update an existing service provider profile.
    
    Args:
        pro_id (int): The unique identifier of the provider.
        
    Expects a JSON payload with the fields to be updated.
    
    Returns:
        A JSON response containing the updated provider and a 200 status code,
        or error payloads (400, 404) on failure.
    """
    pro = db.session.get(Provider, pro_id)
    if not pro:
        return jsonify({"error": "Provider not found"}), 404
        
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
        
    pro.name = data.get('name', pro.name)
    pro.trade = data.get('trade', pro.trade)
    pro.phone = data.get('phone', pro.phone)
    pro.email = data.get('email', pro.email)
    pro.photo_url = data.get('photo_url', pro.photo_url)
    pro.location = data.get('location', pro.location)
    
    if 'experience_years' in data:
        pro.experience_years = data['experience_years']
        
    if 'is_verified' in data:
        pro.is_verified = data['is_verified']
        
    if 'starting_rate' in data:
        pro.starting_rate = data['starting_rate']
        
    pro.bio = data.get('bio', pro.bio)
    
    db.session.commit()
    return jsonify(pro.to_dict()), 200

@app.route('/providers/<int:pro_id>', methods=['DELETE'])
def remove_pro(pro_id):
    """
    Delete a specific service provider and cascade delete their reviews.
    
    Args:
        pro_id (int): The unique identifier of the provider.
        
    Returns:
        A JSON success message with a 200 status code, or a 404 if not found.
    """
    pro = db.session.get(Provider, pro_id)
    if not pro:
        return jsonify({"error": "Provider not found"}), 404
        
    db.session.delete(pro)
    db.session.commit()
    return jsonify({"message": "Profile deleted successfully"}), 200

# --- API Review Endpoints ---

@app.route('/providers/<int:pro_id>/reviews', methods=['GET'])
def get_reviews(pro_id):
    """
    Retrieve all reviews associated with a specific provider.
    
    Args:
        pro_id (int): The unique identifier of the provider.
        
    Returns:
        A JSON array containing the reviews and a 200 status code, 
        or a 404 if the provider does not exist.
    """
    # Verify the provider exists first
    pro = db.session.get(Provider, pro_id)
    if not pro:
        return jsonify({"error": "Provider not found"}), 404
        
    reviews = Review.query.filter_by(pro_id=pro_id).all()
    return jsonify([r.to_dict() for r in reviews]), 200

@app.route('/providers/<int:pro_id>/reviews', methods=['POST'])
def add_review(pro_id):
    """
    Submit a new review for a service provider.
    
    Validates that the reviewer's IP address has not already submitted a review
    for this specific provider to prevent spam.
    
    Args:
        pro_id (int): The unique identifier of the provider.
        
    Expects a JSON payload containing at least a 'rating' (integer 1-5).
    
    Returns:
        A JSON representation of the new review and a 201 status code on success,
        or various error codes (400, 403, 404) depending on the validation failure.
    """
    # Verify the provider exists first
    pro = db.session.get(Provider, pro_id)
    if not pro:
        return jsonify({"error": "Provider not found"}), 404
        
    # Extract client IP
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    # Check if a review already exists for this IP and provider
    if client_ip:
        existing_review = Review.query.filter_by(pro_id=pro_id, ip_address=client_ip).first()
        if existing_review:
            return jsonify({"error": "You have already submitted a review for this provider."}), 403
            
    data = request.get_json()
    if not data or 'rating' not in data:
        return jsonify({"error": "Missing required field: 'rating'"}), 400
        
    try:
        rating = int(data.get('rating'))
        if rating < 1 or rating > 5:
            return jsonify({"error": "Rating must be between 1 and 5"}), 400
    except ValueError:
         return jsonify({"error": "Rating must be an integer"}), 400
        
    new_review = Review(
        pro_id=pro_id,
        rating=rating,
        comment=data.get('comment'),
        ip_address=client_ip
    )
    
    db.session.add(new_review)
    db.session.commit()
    
    return jsonify(new_review.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
