from math import log2, floor

from ape import project, accounts
from silverback import SilverbackApp

from ape_farcaster import Warpcast
import os
import datetime
import requests

app = SilverbackApp()
warper = accounts.load("warpNinjagod")
client = Warpcast(warper)
my_contract = project.Echo.at("0xE8116A0Fb2D4Ee04F570fbEA4460F9C7B0121D76")
STABILITY_KEY= os.environ.get("STABILITY_KEY") 

@app.on_(my_contract.Received)
def payment_received(log):
    if log.amount >= 10000000000000000: # .01 eth
        cast_image(log)
        #response = client.post_cast(text="A" + "H" * floor(log2(log.amount)))
        #print(response.cast.hash)

def cast_image(log):
    scream="A" + "H" * floor(log2(log.amount))
    response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/generate/ultra",
    headers={
        "authorization": STABILITY_KEY,
        "accept": "image/*"
    },
    files={"none": ''},
    data={
        "prompt": f"Ape Scream: +{scream}",
        "output_format": "jpeg",
   },
)
    if response.status_code == 200:
        image = "https://ipfs.decentralized-content.com/ipfs/bafkreieraqfkny7bttxd7h7kmnz6zy76vutst3qbjgjxsjnvrw7z3i2n7i"
        #image = f"./image_{datetime.now()}.jpeg"
        with open(image, 'wb') as file:
            client.post_cast(text=scream, embeds=[file])
    else:
        raise Exception(str(response.json()))