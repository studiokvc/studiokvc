"""Validation de contexte pour un claim ZK."""

def verify(claim, expected_statement, verifier_id):
    return isinstance(claim, dict) and claim.get("statement") == expected_statement and claim.get("verifier_id") == verifier_id and bool(claim.get("proof"))

if __name__ == "__main__":
    c = {"statement":"age>=18","verifier_id":"v1","proof":"opaque"}
    assert verify(c,"age>=18","v1")
    assert not verify(c,"age>=21","v1")
    assert not verify(c,"age>=18","v2")
