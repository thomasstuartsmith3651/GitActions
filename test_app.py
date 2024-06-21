import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test the home page for correct HTTP response and HTML content."""
    response = client.get('/')
    assert response.status_code == 200
    assert 'Enter a Number to Multiply by 10' in response.get_data(as_text=True)

def test_multiply(client):
    """Test the multiply functionality."""
    response = client.post('/', data={'number': '5'})
    assert 'Result: 50' in response.get_data(as_text=True)
    assert response.status_code == 200