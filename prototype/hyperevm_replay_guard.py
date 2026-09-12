"""Protection pédagogique contre le rejeu HyperEVM."""

class ReplayGuard:
    def __init__(self): self.seen = set()
    def accept(self, chain_id, sender, nonce, payload):
        key = (chain_id, sender, nonce, payload)
        if key in self.seen: return False
        self.seen.add(key); return True

if __name__ == "__main__":
    g = ReplayGuard()
    assert g.accept(999,"alice",1,"order")
    assert not g.accept(999,"alice",1,"order")
    assert g.accept(999,"alice",2,"order")
