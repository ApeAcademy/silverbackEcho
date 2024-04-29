from ape import accounts, networks, project, Contract

# Replace with the actual contract address after deployment
# 0x4B3605c1f1089b33838538E6FabE5984100CB9ae
# 0xE435d0ED21afeE7b46d03E92977F08a3155FAfa1
CONTRACT_ADDRESS = "0xE435d0ED21afeE7b46d03E92977F08a3155FAfa1"

# The sender and receiver addresses
SENDER_ADDRESS = accounts.load("sepDev2")
RECEIVER_ADDRESS = accounts.load("sepDev")

# The amount to send (in wei)
AMOUNT_TO_SEND = 10000

def main():
    # Load the account of the sender
    sender_account = accounts.load("sepDev2")  # Use the correct alias for your account

    # Connect to the Sepolia network
    with networks.parse_network_choice("ethereum:sepolia") as provider:
        # Load the contract
        my_contract = Contract(CONTRACT_ADDRESS)


        # Check the contract's balance
        sender_balance = sender_account.balance
        print(f"Sender balance before sending: {sender_balance / 1e18} eth")

        # Send ETH from the contract to the receiver
        try:
            sender_account.transfer(my_contract, ".001 ether",gas_limit=50_000) 
            tx = my_contract.withdraw(value = .01 sender=sender_account)
        except Exception as e:
            print(e)

        # Check the contract's balance again
        sender_balance = sender_account.balance
        print(f"Sender balance before sending: {sender_balance / 1e18} eth")

if __name__ == "__main__":
    main()