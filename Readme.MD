Welcome to CurveAMM


A Functional Automatic Market Maker that automatically collects and reinvests all generated fee revenue back into the bonding curve.


- Periodic (default 15m) scan and automatic purchase of tokens for the value of sol generated
- Deducts fee buffer and optional reserve
- Sends all spendable SOL into Pump.fun buy instruction
- Containerized and testable


1. `cp .env.example .env` and fill values
2. `docker-compose up --build` or run `python -m src.bot`


Open `src/pumpfun_client.py` and implement `build_pumpfun_buy_ix`. The file includes an example instruction layout to guide implementers.


- Test on devnet first.
- Keep keys secure.
