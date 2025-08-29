from src.utils import lamports_to_sol, sol_to_lamports

def test_conversion():
    assert lamports_to_sol(1_000_000_000) == 1.0
    assert sol_to_lamports(1.5) == 1_500_000_000
