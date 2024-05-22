import os
from farcaster import Warpcast

FARCASTER_TOKEN = os.environ.get("FARCASTER_TOKEN")

client = Warpcast(mnemonic=FARCASTER_TOKEN)

print(client.get_healthcheck())