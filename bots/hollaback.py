from ape import convert, Contract
from silverback import SilverbackApp

from . import farcaster
import os


caster = mnemonic=os.environ.get("caster")
FARCASTER_TOKEN=os.environ.get("FARCASTER_TOKEN")
client = Warpcast(mnemonic=FARCASTER_TOKEN)

app = SilverbackApp()

my_contract = Contract(os.environ["ECHO_CONTRACT"])

@app.on_(my_contract.Received)
def payment_received(log):
    # convert is an ape method to compare log.amount in wei vs wei 
    if log.amount >= convert(".1 ether", int):
        response = client.post_cast(text="AHHHHHHHHH")
        print(client.get_healthcheck())

