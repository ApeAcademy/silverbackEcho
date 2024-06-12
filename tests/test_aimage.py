import requests
import os
import time

STABILITY_KEY= os.environ.get("STABILITY_KEY") 
PINATA_API_KEY= os.environ.get("PINATA_API_KEY")
PINATA_SECRET_KEY= os.environ.get("PINATA_SECRET_KEY")

def uploadToPinata(image):
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"

    headers = {
    'pinata_api_key': PINATA_API_KEY,
    'pinata_secret_api_key': PINATA_SECRET_KEY,
    }


    files = {'file': ("ApeScream1", image),
    }
    
    response = requests.request("POST", url, files=files, headers=headers)
    print(response.text)


response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/generate/ultra",
    headers={
        "authorization": STABILITY_KEY,
        "accept": "image/*"
    },
    files={"none": ''},
    data={
        "prompt": "Ape Scream: AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH",
        "output_format": "jpeg",
    },
)

if response.status_code == 200:
    with open("./ApeScream1.jpeg", 'wb') as file:
        file.write(response.content)   
else:
    raise Exception(str(response.json()))

file = open("./ApeScream1.jpeg", 'rb')
uploadToPinata(file)