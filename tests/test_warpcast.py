import os
from ape_farcaster import Warpcast
from ape import accounts
import requests
import os
import base64


STABILITY_KEY= os.environ.get("STABILITY_KEY") 

warper = accounts.load("warpNinjagod")
client = Warpcast(warper)

print(client.get_healthcheck())

response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/generate/ultra",
    headers={
        "authorization": STABILITY_KEY,
        "accept": "image/*"
    },
    files={"none": ''},
    data={
        "prompt": "Ape Scream: AHHHHHHHHHHHH",
        "output_format": "jpeg",
    },
)

client.post_cast(text="AHHHH",embeds=[base64.b64encode(open("./ApeScream.jpeg", 'rb').read())])

with open("./ApeScream.jpeg", 'r') as file:
    #breakpoint()
    image = "https://ipfs.decentralized-content.com/ipfs/bafkreieraqfkny7bttxd7h7kmnz6zy76vutst3qbjgjxsjnvrw7z3i2n7i"
client.post_cast(text="AHHHH",embeds=[base64.b64encode(open("./ApeScream.jpeg", 'r'))])
    