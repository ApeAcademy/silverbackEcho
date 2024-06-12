import requests
import os

PINATA_API_KEY= os.environ.get("PINATA_API_KEY")
PINATA_SECRET_KEY= os.environ.get("PINATA_SECRET_KEY")

def uploadToPinata():
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"

    headers = {
    'pinata_api_key': PINATA_API_KEY,
    'pinata_secret_api_key': PINATA_SECRET_KEY,
    }

    files = {'file': ("ApeScream", open("./ApeScream.jpeg", 'rb')),
    }
    
    response = requests.request("POST", url, files=files, headers=headers)
    print(response.text)


uploadToPinata()