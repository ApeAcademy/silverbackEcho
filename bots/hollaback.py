from ape import convert, project
from silverback import SilverbackApp

from ape_farcaster import Warpcast
import os

app = SilverbackApp()
client = Warpcast(app.signer)
my_contract = project.Echo.at(os.environ["ECHO_CONTRACT"])


@app.on_(my_contract.Received)
def payment_received(log):
    
    # convert is an ape method to compare log.amount in wei vs wei 
    if log.amount >= convert(".1 ether", int):
        response = client.post_cast(text="AHHHHHHHHH")
        print(client.get_healthcheck())
