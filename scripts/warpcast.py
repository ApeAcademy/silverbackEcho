import os
from farcaster import Warpcast
from dotenv import load_dotenv # can be installed with `pip install python-dotenv`

caster = mnemonic=os.environ.get("caster")

load_dotenv()

client = Warpcast()

print(client.get_healthcheck())