import requests
import os

STABILITY_KEY= os.environ.get("STABILITY_KEY") 

response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/generate/ultra",
    headers={
        "authorization": STABILITY_KEY,
        "accept": "image/*"
    },
    files={"none": ''},
    data={
        "prompt": "Ape Scream: AHHHHHHHHHHHH",
        "output_format": "webp",
    },
)

if response.status_code == 200:
    with open("./ApeScream.webp", 'wb') as file:
        file.write(response.content)
else:
    raise Exception(str(response.json()))