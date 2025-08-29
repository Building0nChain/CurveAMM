import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

RPC_URL = os.getenv('RPC_URL')
DEV_KEYPAIR_PATH = os.getenv('DEV_KEYPAIR_PATH')
SPENDABLE_THRESHOLD_SOL = float(os.getenv('SPENDABLE_THRESHOLD_SOL', '0.01'))
FEE_BUFFER_SOL = float(os.getenv('FEE_BUFFER_SOL', '0.002'))
RUN_INTERVAL_SECONDS = int(os.getenv('RUN_INTERVAL_SECONDS', '900'))
PUMPFUN_PROGRAM_ID = os.getenv('PUMPFUN_PROGRAM_ID')
TOKEN_MINT_ADDRESS = os.getenv('TOKEN_MINT_ADDRESS')
MAX_SPEND_PERCENT = float(os.getenv('MAX_SPEND_PERCENT', '1.0'))
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

def read_keypair(path: str):
    from solders.keypair import Keypair
    from pathlib import Path
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Keypair path not found: {path}")
    import json
    arr = json.loads(p.read_text())
    return Keypair.from_secret_key(bytes(arr))

