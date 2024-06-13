from math import log10, floor

from ape import project, accounts
from silverback import SilverbackApp
from ape_farcaster import Warpcast

import os
import tempfile
import requests

from wonderwords import RandomWord

STABILITY_KEY= os.environ.get("STABILITY_KEY")
PINATA_API_KEY= os.environ.get("PINATA_API_KEY")
PINATA_SECRET_API_KEY= os.environ.get("PINATA_SECRET_API_KEY")

app = SilverbackApp()
warper = accounts.load("warpNinjagod")
client = Warpcast(warper)
my_contract = project.Echo.at(os.environ.get("ECHO_CONTRACT"))

def create_prompt(number_adj:int) -> str:
    w = RandomWord()
    adjectives = w.random_words(number_adj, include_categories=["adjective"])
    adjectives_string = ", ".join(adjectives)
    prompt = f"An {adjectives_string} ape that is screaming AHHHHH."
    
    return prompt
    
@app.on_(my_contract.Received)
def payment_received(log):
    print(log)
    prompt = create_prompt(max(floor(log10(log.amount))- 12, 1))
    for _ in range(10):
        print(f"\n{prompt}\n")
        # create image from AI using scream
        try:
            fileName = createImage(prompt)
            break
        except Exception as e:
            print(e)
            prompt = create_prompt(max(floor(log10(log.amount))- 12, 1))
        

    # open the created image
    print(fileName + " has beeen created")
    image = open(fileName, 'rb')
    # upload image to Pinata
    ipfsHash = uploadToPinata(image)
    # cast the message with the scream and ipfs link
    ipfsLink = "https://jade-slow-pigeon-687.mypinata.cloud/ipfs/" + ipfsHash
    warpcast_text =  f"A picture of {log.sender}:\n"
    client.post_cast(text=warpcast_text, embeds=[ipfsLink])


def createImage(prompt):
    
    response = requests.post(
    "https://api.stability.ai/v2beta/stable-image/generate/ultra",
    headers={
        "authorization": STABILITY_KEY,
        "accept": "image/*"
    },
    files={"none": ''},
    data={
        "prompt": prompt,
        "output_format": "jpeg",
   },
)

    if response.status_code == 200:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpeg") as fp:
            fp.write(response.content)
    else:
        raise Exception(str(response.json()))
        
    return fp.name

def uploadToPinata(image):
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"

    headers = {
    'pinata_api_key': PINATA_API_KEY,
    'pinata_secret_api_key': PINATA_SECRET_API_KEY,}

    files = {'file': ("ApeScream", image)}
    response = requests.request("POST", url, files=files, headers=headers)
    
    response.raise_for_status()
    return response.json()["IpfsHash"]