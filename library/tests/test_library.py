import pytest
from app import library

# Test data for clients
test_client_existing = {"first_name": "first_name1", "last_name": "last_name1"}
test_client_new = {"first_name": "John", "last_name": "Doe"}


def test_client_exist():
    # Existing client should return True
    assert library.client_exist(test_client_existing) is True
    
    # Non-existing client should return False
    assert library.client_exist(test_client_new) is False
