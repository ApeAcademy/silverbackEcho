import requests

from ape import chain
from silverback import SilverbackApp
import os
from farcaster import Warpcast
from dotenv import load_dotenv # can be installed with `pip install python-dotenv`

app = SilverbackApp()

FARCASTER_TOKEN=os.environ.get("FARCASTER_TOKEN")
client = Warpcast(mnemonic=FARCASTER_TOKEN)

print(client.get_healthcheck())



# Define the endpoint URL of your FastAPI server
ENDPOINT = "http://localhost:8000/hello"

@app.on_(chain.blocks)
def send_html_request():
    # Send an HTTP GET request to the FastAPI endpoint
    try:
        response = requests.get(ENDPOINT)
        if response.status_code == 200:
            print(response.text)
        else:
            print(f"Failed to get response. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    app.run()