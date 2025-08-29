"""Wrapper around constructing Pump.fun buy instructions and sending txs.

NOTE: Pump.fun's exact instruction layout must be implemented here. The function
`build_pumpfun_buy_ix` is intentionally a placeholder with clear TODOs.
"""
import asyncio
from solana.rpc.async_api import AsyncClient
from solana.transaction import Transaction
from solana.publickey import PublicKey
from solana.system_program import SYS_PROGRAM_ID
from solana.rpc.types import TxOpts
from solana.rpc.commitment import Confirmed
from solana.rpc.core import RPCException


async def build_pumpfun_buy_ix(buyer_pubkey: PublicKey, mint_pubkey: PublicKey, sol_lamports: int):
    """
    Build the Pump.fun "buy" instruction.

    **TODO**: Replace this placeholder with the real Pump.fun accounts + args.

    Return: a `TransactionInstruction` object ready to be added to a Transaction.
    """
    from solana.transaction import TransactionInstruction

    # Placeholder: a simple system transfer to the program id (won't actually buy tokens)
    # Replace with Pump.fun's proper CPI instruction (accounts + data)
    program_id = PublicKey("PumpFun111111111111111111111111111111111")
    data = sol_lamports.to_bytes(8, 'little')  # placeholder
    keys = [
        # Example accounts - change as needed
        {"pubkey": buyer_pubkey, "is_signer": True, "is_writable": True},
        {"pubkey": mint_pubkey, "is_signer": False, "is_writable": True},
        {"pubkey": SYS_PROGRAM_ID, "is_signer": False, "is_writable": False},
    ]
    ix = TransactionInstruction(keys=keys, program_id=program_id, data=data)
    return ix


async def send_buy_tx(client: AsyncClient, payer, ix):
    tx = Transaction().add(ix)
    try:
        sig = await client.send_transaction(tx, payer, opts=TxOpts(skip_preflight=False, preflight_commitment=Confirmed))
        await client.confirm_transaction(sig['result'])
        return sig['result']
    except Exception as e:
        raise e
