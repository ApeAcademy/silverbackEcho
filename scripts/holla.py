from ape import accounts, networks, Contract

# Replace with the actual contract address after deployment
CONTRACT_ADDRESS = "0xE8116A0Fb2D4Ee04F570fbEA4460F9C7B0121D76"

# The amount to send (in wei)
AMOUNT_TO_SEND = 10000000000000000 # .01 eth


with networks.parse_network_choice("ethereum:sepolia"):
    # Load the contract
    my_contract = Contract(CONTRACT_ADDRESS)

sender_account = accounts.load("sepDev")  # Use the correct alias for your account

def main():
    
    sender_balance = sender_account.balance
    print(f"Sender balance before sending: {sender_balance / 1e18} eth")

    # Send ETH from the contract to the receiver
    try:
        # transfer eth to contract
        tx_transfer = sender_account.transfer(my_contract, "0.01 ether",gas_limit=100_000)
        print(tx_transfer)
    except Exception as e:
        print(e)

receiver_account = accounts.load("sepDev2")  # Use the correct alias for your account

def withdraw_contract_balance():
    try:
        # withdraw money from contract
        print("Echo contract balance before withdraw: " + my_contract.balance)
        tx_withdraw = my_contract.withdraw(sender=receiver_account, gas_limit=100_000)
        print(tx_withdraw)
        print("Echo contract balance after withdraw: " + my_contract.balance)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()