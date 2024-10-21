import pytest
from unittest.mock import MagicMock
from ape import project
from silverback import SilverbackBot
import os

@pytest.fixture
def silverback_app():
    app = SilverbackBot()
    return app

@pytest.fixture
def mock_contract():
    # Create a mock contract for the Echo contract
    contract = MagicMock()
    contract.Received = MagicMock()  # Mock the Received event
    return contract

@pytest.fixture
def mock_client():
    client = MagicMock()
    return client

@pytest.fixture
def mock_env_vars(monkeypatch):
    monkeypatch.setenv("STABILITY_KEY", "mock-stability-key")
    monkeypatch.setenv("PINATA_API_KEY", "mock-pinata-key")
    monkeypatch.setenv("PINATA_SECRET_API_KEY", "mock-pinata-secret")
    monkeypatch.setenv("ECHO_CONTRACT", "0xMockContractAddress")

@pytest.fixture
def mock_create_image(monkeypatch):
    def mock_create_image_func(prompt):
        return "/path/to/mock_image.jpeg"
    monkeypatch.setattr("main.createImage", mock_create_image_func)

@pytest.fixture
def mock_upload_to_pinata(monkeypatch):
    def mock_upload_func(image):
        return "mockIpfsHash"
    monkeypatch.setattr("main.uploadToPinata", mock_upload_func)
