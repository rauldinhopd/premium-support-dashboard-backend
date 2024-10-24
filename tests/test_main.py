import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from unittest.mock import patch
import redis
from main import app

# Sync test client for non-async endpoints
client = TestClient(app)


""" # Mock Redis for testing without a real Redis instance
@pytest.fixture
def mock_redis(mocker):
    mocker.patch("main.redis.Redis", return_value=redis.StrictRedis())
 """


# Test root endpoint "/"
def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}


# Test "/overview" endpoint
def test_get_overview():
    response = client.get("/overview")
    assert response.status_code == 200
    assert "data" in response.json()  # Adjust based on your mock data


# Test "/health" endpoint
def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "external_api": "ok", "database": "ok"}


""" 
# Test "/redis" endpoint with mocked Redis
def test_redis(mock_redis):
    response = client.get("/redis")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from Redis!"}
 """
