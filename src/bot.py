"""Main buyback loop"""
import asyncio
import logging
from solana.rpc.async_api import AsyncClient
from solana.publickey import PublicKey
from solders.keypair import Keypair

from .config import (
    RPC_URL,
    DEV_KEYPAIR_PATH,
    SPENDABLE_THRESHOLD_SOL,
    FEE_BUFFER_SOL,
    RUN_INTERVAL_SECONDS,
    TOKEN_MINT_ADDRESS,
)
from .pumpfun_client import build_pumpfun_buy_ix, send_buy_tx
from .utils import lamports_to_sol, sol_to_lamports, retry

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("buyback-bot")

async def run_once():
    client = AsyncClient(RPC_URL)
    keypair = Keypair.from_secret_key(open(DEV_KEYPAIR_PATH, 'rb').read())
    payer_pub = keypair.pubkey()

    # fetch bal
    bal_resp = await client.get_balance(payer_pub)
    lamports = bal_resp['result']['value']
    sol = lamports_to_sol(lamports)
    logger.info(f"Balance: {sol:.6f} SOL")

    spendable = sol - FEE_BUFFER_SOL
    if spendable <= SPENDABLE_THRESHOLD_SOL:
        logger.info("Not enough spendable SOL - skipping")
        await client.close()
        return

    lam_to_spend = sol_to_lamports(spendable)
    mint_pk = PublicKey(TOKEN_MINT_ADDRESS)

    ix = await build_pumpfun_buy_ix(payer_pub, mint_pk, lam_to_spend)

    # send tx with retry
    try:
        sig = await retry(lambda: send_buy_tx(client, keypair, ix), retries=3)
        logger.info(f"Buy tx sent: {sig}")
    except Exception as e:
        logger.error(f"Failed to send buy tx: {e}")

    await client.close()

async def loop():
    while True:
        try:
            await run_once()
        except Exception as e:
            logger.exception(f"Error in buyback loop: {e}")
        await asyncio.sleep(RUN_INTERVAL_SECONDS)

if __name__ == '__main__':
    asyncio.run(loop())
