### README.md

# Ape Scream (Silverback Farcast Project)

This project demonstrates the use of Silverback in a fun way by integrating it with a simple Vyper contract and a Warpcast service for broadcasting messages. The goal of this project is to trigger an action to scream into the void when a specific condition is met in the contract.

## Project Setup

* pip install -r requirements.txt
* you should have silverback and wonderwords installed with requirements
* ape plugins install . or ape plugins install ape-config.yaml

the ape plugins and ape should be 0.8.x or higher

* you should have your Warcaster account

### Contract (Echo.vy)

The `Echo.vy` file contains a simple Vyper contract that emits a `Received` event when ETH is received and provides a `withdraw` method to send ETH to the contract owner.

### hollaback.py

The `hollaback.py` file sets up a SilverbackApp to watch for events on the contract. When a payment is received that exceeds 0.01 ETH, it triggers a message to be broadcasted using the Warpcast service.

### Holla.py

The `Holla.py` file initializes the network connection, loads the contract, transfers ETH to the contract, and triggers the contract's `withdraw` method.

## Getting Started

1. Ensure you have the necessary accounts set up in your Ape environment
2. Deploy the Vyper contract `Echo.vy` to the desired network and note the contract address.

3. Update the `CONTRACT_ADDRESS` variable in `Holla.py` and `hollaback.py` with the deployed contract address.

4. Run the SilverbackApp by executing `silverback run bots.hollaback:app` in one terminal.

5. Run the `Holla.py` script by executing `ape run holla` in another terminal to interact with the contract and trigger the event.

Note if you get an error about no provider found. Try it multiple times it might not work the first time