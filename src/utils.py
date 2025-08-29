import asyncio
import logging

logger = logging.getLogger(__name__)

def lamports_to_sol(lamports: int) -> float:
    return lamports / 1e9

def sol_to_lamports(sol: float) -> int:
    return int(sol * 1e9)

async def retry(coro_fn, retries=3, backoff=2, *args, **kwargs):
    last = None
    for i in range(retries):
        try:
            return await coro_fn(*args, **kwargs)
        except Exception as e:
            last = e
            logger.warning(f"Attempt {i+1} failed: {e}")
            await asyncio.sleep(backoff * (i+1))
    raise last

