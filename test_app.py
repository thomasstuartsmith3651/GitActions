from app import app
import json

def test_multiply():
    with app.test_client() as client:
        response = client.post('/multiply', json={'number': 5})
        data = json.loads(response.data)
        assert response.status_code == 200
        assert data['result'] == 50