import pytest
from unittest.mock import MagicMock
from main import create_prompt, payment_received

def test_create_prompt():
    prompt = create_prompt(3)
    assert "ape" in prompt
    assert "screaming" in prompt

def test_payment_received(silverback_app, mock_contract, mock_client, mock_create_image, mock_upload_to_pinata, mock_env_vars):
    # Simulate a log entry from the Received event
    mock_log = MagicMock()
    mock_log.sender = "0xMockSenderAddress"
    mock_log.amount = 1000000000000000000  # Example amount in wei
    
    # Mocking the behavior of Warpcast client
    silverback_app.client = mock_client
    
    # Test the payment received function
    payment_received(mock_log)
    
    # Assertions
    mock_client.post_cast.assert_called_once()
    assert mock_client.post_cast.call_args[1]['text'] == f"A picture of {mock_log.sender}:\n"
    assert "https://jade-slow-pigeon-687.mypinata.cloud/ipfs/mockIpfsHash" in mock_client.post_cast.call_args[1]['embeds'][0]

def test_image_creation(mock_create_image):
    prompt = "An angry ape that is screaming AHHHHH."
    file_path = mock_create_image(prompt)
    assert file_path == "/path/to/mock_image.jpeg"

def test_upload_to_pinata(mock_upload_to_pinata):
    image = MagicMock()  # Mock image object
    ipfs_hash = mock_upload_to_pinata(image)
    assert ipfs_hash == "mockIpfsHash"
