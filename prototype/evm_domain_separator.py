"""Domaine minimal pour éviter les signatures EVM réutilisées."""

def matches_domain(message, chain_id, contract):
    return isinstance(message, dict) and message.get("chain_id") == chain_id and message.get("verifying_contract") == contract and bool(message.get("nonce")) and bool(message.get("payload"))

if __name__ == "__main__":
    m={"chain_id":8453,"verifying_contract":"0xabc","nonce":3,"payload":"approve"}
    assert matches_domain(m,8453,"0xabc")
    assert not matches_domain(m,1,"0xabc")
