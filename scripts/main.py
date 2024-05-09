from ape import accounts, networks, project, Contract
import scripts.monitor as monitor

# Replace with the actual contract address after deployment
CONTRACT_ADDRESS = "0xa6647bA51aBE24F4819931d7B29820Ef039A21ef"

# The sender and receiver addresses
SENDER_ADDRESS = accounts.load("sepDev2")
RECEIVER_ADDRESS = accounts.load("sepDev")

# The amount to send (in wei)
AMOUNT_TO_SEND = 10000

def main():
    # Load the account of the sender
    sender_account = accounts.load("sepDev")  # Use the correct alias for your account
    receiver_account = accounts.load("sepDev2")  # Use the correct alias for your account

    # Connect to the Sepolia network
    with networks.parse_network_choice("ethereum:sepolia") as provider:
        # Load the contract
        my_contract = Contract(CONTRACT_ADDRESS)

        # # Check the contract's balance
        # sender_balance = sender_account.balance
        # print(f"Sender balance before sending: {sender_balance / 1e18} eth")

        # # Send ETH from the contract to the receiver
        # try:
        #     # transfer eth to contract
        #     tx_transfer = sender_account.transfer(my_contract, "0.001 ether",gas_limit=50_000)
        #     print(tx_transfer)
        # except Exception as e:
        #     print(e)

        # Check the contract's balance again
        sender_balance = sender_account.balance
        if sender_balance/ 1e18 >= 2:
            print(f"Sender balance before sending: {sender_balance / 1e18} eth which is greater than .001 eth")
            monitor.montior_block()
        try:
            # withdraw money from contract
            tx_withdraw = my_contract.withdraw(sender=receiver_account, gas_limit = 50_000)
            print(tx_withdraw)
        except Exception as e:
            print(e)

        
        

if __name__ == "__main__":
    main()