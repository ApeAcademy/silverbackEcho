from math import log2, floor

from ape import convert, project
from silverback import SilverbackApp

#from ape_farcaster import Warpcast
from farcaster import Warpcast
import os

app = SilverbackApp()
FARCASTER_TOKEN = os.environ.get("FARCASTER_TOKEN")
client = Warpcast(mnemonic=FARCASTER_TOKEN)
#client = Warpcast(app.signer)
my_contract = project.Echo.at("0xE8116A0Fb2D4Ee04F570fbEA4460F9C7B0121D76")

#my_contract = project.Echo.at(os.environ["ECHO_CONTRACT"])


@app.on_(my_contract.Received)
def payment_received(log):
    response = client.post_cast(text="A" + "H" * floor(log2(log.amount)))
    print(response.cast.hash)
    #print(client.get_healthcheck())
