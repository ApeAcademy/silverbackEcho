import pytest
from ape import project
from silverback import SilverbackApp
from ape_farcaster import Warpcast
import os
from dotenv import load_dotenv

@pytest.fixture(scope="session", autouse=True)
def load_env():
    # Load environment variables from .env file
    load_dotenv()

@pytest.fixture
def silverback_app():
    app = SilverbackApp()
    return app

@pytest.fixture
def echo_contract():
    # Use the actual contract address from the .env file
    contract_address = os.getenv("ECHO_CONTRACT")
    return project.Echo.at(contract_address)

@pytest.fixture
def warpcast_client(silverback_app):
    client = Warpcast(silverback_app.signer)
    return client

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
