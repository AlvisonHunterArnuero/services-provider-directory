import json

def test_home_page(client, init_database):
    """Test that the home page renders and contains our mock data."""
    response = client.get('/')
    assert response.status_code == 200
    # Check if the HTML contains our mock provider
    html = response.data.decode('utf-8')
    assert "Service Provider Directory" in html
    assert "Jack Reacher" in html

def test_profile_page(client, init_database):
    """Test that a specific provider profile page renders correctly."""
    response = client.get('/profile/1')
    assert response.status_code == 200
    html = response.data.decode('utf-8')
    assert "Jack Reacher" in html
    assert "Senior Software Engineer" in html

def test_profile_page_404(client, init_database):
    """Test that requesting a non-existent profile returns 404."""
    response = client.get('/profile/999')
    assert response.status_code == 404

def test_api_get_providers(client, init_database):
    """Test the GET /providers API endpoint."""
    response = client.get('/providers')
    assert response.status_code == 200
    data = json.loads(response.data)

    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["name"] == "Jack Reacher"

def test_api_create_provider(client, init_database):
    """Test creating a new provider via the API."""
    new_pro = {
        "name": "New Coder",
        "trade": "Backend Dev",
        "bio": "I write APIs."
    }
    response = client.post('/providers', json=new_pro)
    assert response.status_code == 201

    data = json.loads(response.data)
    assert data["name"] == "New Coder"
    assert "id" in data

def test_api_submit_review(client, init_database):
    """Test submitting a review for a provider."""
    # Our init_database already submitted a review from 127.0.0.1,
    # so we should test that a second review from the same IP fails,
    # or test a valid one by spoofing the IP if possible, but let's test the duplicate IP logic!

    review_data = {
        "rating": 4,
        "comment": "Trying to review again."
    }

    # By default, Flask test_client sets REMOTE_ADDR to 127.0.0.1
    response = client.post('/providers/1/reviews', json=review_data)

    # Expecting 403 Forbidden because IP is already recorded
    assert response.status_code == 403
    data = json.loads(response.data)
    assert "already submitted a review" in data["error"]
