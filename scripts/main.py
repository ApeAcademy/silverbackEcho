from ape import accounts, networks, project, Contract

# Replace with the actual contract address after deployment
CONTRACT_ADDRESS = "0xBfb007831CA2aB2a7f28d19dC8668597D58ab6B4"

# The sender and receiver addresses
SENDER_ADDRESS = accounts.load("sepDev")
RECEIVER_ADDRESS = accounts.load("sepDev")

# The amount to send (in wei)
AMOUNT_TO_SEND = 10

def main():
    # Load the account of the sender
    sender_account = accounts.load("sepDev")  # Use the correct alias for your account

    # Connect to the Sepolia network
    with networks.parse_network_choice("ethereum:sepolia") as provider:
        # Load the contract
        my_contract = Contract(CONTRACT_ADDRESS)


        # Check the contract's balance
        sender_balance = sender_account.balance
        print(f"Sender balance before sending: {sender_balance / 1e18} wei")

        # Send ETH from the contract to the receiver
        try: 
            tx = my_contract.sendETH(RECEIVER_ADDRESS, str(AMOUNT_TO_SEND), sender=sender_account)
            receipt = tx.wait_for_receipt()
            print(f"Transaction receipt: {receipt}")
        except Exception as e:
            print(e)

        # Check the contract's balance again
        sender_balance = sender_account.balance
        print(f"Sender balance before sending: {sender_balance / 1e18} wei")

if __name__ == "__main__":
    main()