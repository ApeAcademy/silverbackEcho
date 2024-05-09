import os
from farcaster import Warpcast

caster = mnemonic=os.environ.get("caster")

FARCASTER_TOKEN=os.environ.get("FARCASTER_TOKEN")
client = Warpcast(mnemonic=FARCASTER_TOKEN)

print(client.get_healthcheck())