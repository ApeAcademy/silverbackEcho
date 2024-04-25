# @version 0.3.1

event Received:
    sender: indexed(address)
    amount: uint256
    message: Bytes[160]

OWNER: immutable(address)

@externalex
def __init__():
    OWNER = msg.sender

@external
@payable
def __default__():
    """
    Fallback function to receive ETH and emit the Received event.
    Recieve method
    """
    log Received(msg.sender, msg.value, slice(msg.data, 0, 160))

@external
def withdraw():
    """
    Send eth method
    """
    send(OWNER, self.balance)