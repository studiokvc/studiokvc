"""Invariant minimal pour un dépôt Base."""

def valid(deposit, chain_id=8453):
    fields = {"sender", "amount", "chain_id", "nonce"}
    return isinstance(deposit, dict) and fields <= deposit.keys() and deposit["chain_id"] == chain_id and deposit["amount"] > 0

if __name__ == "__main__":
    assert valid({"sender":"alice","amount":1,"chain_id":8453,"nonce":1})
    assert not valid({"sender":"alice","amount":0,"chain_id":8453,"nonce":1})
