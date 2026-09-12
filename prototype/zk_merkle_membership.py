"""Vérification pédagogique d une appartenance Merkle annoncée."""

def valid_membership(claim):
    fields={"root","leaf","path","index"}
    return isinstance(claim,dict) and fields <= claim.keys() and bool(claim["root"]) and isinstance(claim["path"],list) and claim["index"] >= 0

if __name__ == "__main__":
    assert valid_membership({"root":"r","leaf":"l","path":[],"index":0})
    assert not valid_membership({"root":"","leaf":"l","path":[],"index":0})
