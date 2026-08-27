"""
Unit tests for the Flask app
Tests use pytest framework
"""

import pytest
from app import app, add, subtract


@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# ===== Tests for app.py functions =====

def test_add():
    """Test the add function"""
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0


def test_subtract():
    """Test the subtract function"""
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-5, -3) == -2


# ===== Tests for Flask endpoints =====

def test_home(client):
    """Test the home endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['status'] == 'running'
    assert '🚀' in response.json['message']


def test_health(client):
    """Test the health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'


def test_info(client):
    """Test the info endpoint"""
    response = client.get('/api/info')
    assert response.status_code == 200
    assert response.json['version'] == '1.0'
    assert response.json['app'] == 'DevOps CI/CD Demo'


def test_404_error(client):
    """Test that non-existent endpoint returns 404"""
    response = client.get('/nonexistent')
    assert response.status_code == 404
