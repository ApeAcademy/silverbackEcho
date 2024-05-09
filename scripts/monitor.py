from ape import chain
from silverback import SilverbackApp

from ape import Contract, networks
import scripts.scream as scream

app = SilverbackApp()

with networks.parse_network_choice("ethereum:sepolia") as provider:
    my_contract = Contract("0xa6647bA51aBE24F4819931d7B29820Ef039A21ef")
 
intial_contract_balance= my_contract.balance / 1e18 
# 2.01 eth

@app.on_(chain.blocks)
def montior_block():
    with networks.parse_network_choice("ethereum:sepolia") as provider:
        # it has withdraw some amount and it si 1 eth
        contract_balance = my_contract.balance / 1e18
        
        if intial_contract_balance - contract_balance >= .001:
            print("contract has used .001 to scream")
            intial_contract_balance = contract_balance
            scream()        
        


if __name__ == "__main__":
    app.run()