"""Contrôle d un claim ZK de bornes publiques."""

def in_range(claim, lower, upper):
    return isinstance(claim,dict) and claim.get("statement") == "range" and claim.get("value", lower-1) >= lower and claim.get("value", upper+1) <= upper and bool(claim.get("proof"))

if __name__ == "__main__":
    assert in_range({"statement":"range","value":7,"proof":"p"},0,10)
    assert not in_range({"statement":"range","value":11,"proof":"p"},0,10)
