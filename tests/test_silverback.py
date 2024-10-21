import pytest
from main import create_prompt, payment_received

def test_create_prompt():
    prompt = create_prompt(3)
    assert "ape" in prompt
    assert "screaming" in prompt

def test_payment_received(echo_contract, warpcast_client, log):
    # Simulate a log entry from the Received event
    log.sender = "0xSenderAddress"
    log.amount = 1000000000000000000  # Example amount in wei
    
    # Test the payment received function with the real contract
    payment_received(log)
    
    # Assertions
    warpcast_client.post_cast.assert_called_once()
    assert warpcast_client.post_cast.call_args[1]['text'] == f"A picture of {log.sender}:\n"
    assert "https://jade-slow-pigeon-687.mypinata.cloud/ipfs/IpfsHash" in warpcast_client.post_cast.call_args[1]['embeds'][0]

# def test_image_creation(image):
#     prompt = "An angry ape that is screaming AHHHHH."
#     file_path = create_image(prompt)
#     assert file_path == "/path/to/_image.jpeg"

# def test_upload_to_pinata(image):
#     ipfs_hash = upload_to_pinata(image)
#     assert ipfs_hash == "IpfsHash"
