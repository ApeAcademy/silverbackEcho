from ape import accounts, networks, project

# Replace with the actual contract address after deployment
CONTRACT_ADDRESS = "0xYourContractAddressHere"

# The sender and receiver addresses
SENDER_ADDRESS = ""
RECEIVER_ADDRESS = ""

# The amount to send (in wei)
AMOUNT_TO_SEND = 1e18  # Sending 1 ETH as an example

def main():
    # Load the account of the sender
    sender_account = accounts.load("my-sepolia-account")  # Use the correct alias for your account

    # Connect to the Sepolia network
    with networks.parse_network_choice("ethereum:sepolia") as provider:
        # Load the contract
        my_contract = project.MyContract.at(CONTRACT_ADDRESS)

        # Check the contract's balance
        contract_balance = my_contract.balance()
        print(f"Contract balance before sending: {contract_balance} wei")

        # Send ETH from the contract to the receiver
        tx = my_contract.sendETH(RECEIVER_ADDRESS, AMOUNT_TO_SEND, sender=sender_account)
        receipt = tx.wait_for_receipt()
        print(f"Transaction receipt: {receipt}")

        # Check the contract's balance again
        contract_balance = my_contract.balance()
        print(f"Contract balance after sending: {contract_balance} wei")

if __name__ == "__main__":
    main()