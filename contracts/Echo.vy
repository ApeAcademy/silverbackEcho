# Sample Vyper contract to send and receive ETH on Sepolia testnet

# @version 0.3.1

# Event to log received ETH

event Received:
    sender: indexed(address)
    amount: uint256

@external
@payable
def receive() -> bool:
    """
    Fallback function to receive ETH and emit the Received event.
    """
    log Received(msg.sender, msg.value)
    return True

@external
def sendETH(receiver: address, amount: uint256):
    """
    Function to send ETH to a specified address.

    :param receiver: The address of the recipient
    :param amount: The amount of ETH to send (in wei)
    :return: True if the transaction is successful, otherwise False
    """
    assert self.balance >= amount, "Insufficient balance to send ETH"
    send(receiver, amount)