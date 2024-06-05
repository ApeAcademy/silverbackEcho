### README.md

Project is created by Ninjagod1251

# Ape Scream (Silverback Farcast Project)

This project demonstrates the use of Silverback in a fun way by integrating it with a simple Vyper contract and a Warpcast service for broadcasting messages. The goal of this project is to trigger an action to scream into the void when a specific condition is met in the contract.

## Project Setup

### Contract (Echo.vy)

The `Echo.vy` file contains a simple Vyper contract that emits a `Received` event when ETH is received and provides a `withdraw` method to send ETH to the contract owner.

### bots/hollaback.py

The `hollaback.py` file sets up a Silverback bot to watch for events on the contract. When a payment is received that exceeds 0.01 ETH, it triggers a message to be broadcasted using the Warpcast service.

### scripts/holla.py

The `Holla.py` loads the contract, transfers ETH to the contract, and calls the contract's `withdraw` method to withdraw eth to the contract reciever.

## Getting Started

1. Ensure you have the necessary accounts set up in your Ape environment
* Farcast Account
* testnet account for (sepolia)
2. pip install -r requirements for the right plugins

3. Double Check the `ape-config.yaml` for the right network default connections. You need to have a sepolia node. Setting up [etherscan](https://github.com/ApeWorX/ape-etherscan?tab=readme-ov-file#set-up-the-environment)

4. Deploy the Vyper contract `Echo.vy` to the desired network and note the contract address.

5. Update the `CONTRACT_ADDRESS` variable in `Holla.py` and `hollaback.py` with the deployed contract address.

6. Run the SilverbackApp by executing `silverback run scripts.hollaback:app --network ethereum:sepolia` in one terminal.

7. Run the `Holla.py` script by executing `ape run holla` in another terminal to interact with the contract and trigger the event.

8. Check your cast on Warpcast and tag us with @apeworx