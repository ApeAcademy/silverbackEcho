# @version 0.3.10

event Received:
    sender: indexed(address)
    amount: uint256

OWNER: immutable(address)

@external
def __init__():
    OWNER = msg.sender

@external
@payable
def __default__():
    """
    Fallback function to receive ETH and emit the Received event.
    Recieve method
    """
    log Received(msg.sender, msg.value)

@external
def withdraw():
    """
    Send eth method
    """
    send(OWNER, self.balance)