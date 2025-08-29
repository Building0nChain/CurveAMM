from src.config import SPENDABLE_THRESHOLD_SOL

def test_threshold_default():
    assert isinstance(SPENDABLE_THRESHOLD_SOL, float)

