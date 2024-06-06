from math import log2, floor

from ape import project, accounts
from silverback import SilverbackApp
from scripts.holla import withdraw_contract_balance

from ape_farcaster import Warpcast
import os

app = SilverbackApp()
warper = accounts.load("warpNinjagod")
client = Warpcast(warper)
my_contract = project.Echo.at(os.environ("ECHO_CONTRACT"))

@app.on_(my_contract.Received)
def payment_received(log):
    if log.amount >= 10000000000000000: # .01 eth
        response = client.post_cast(text="A" + "H" * floor(log2(log.amount)))
        print(response.cast.hash)
    