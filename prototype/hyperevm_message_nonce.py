"""Nonce monotone pour un message inter-domaines HyperEVM."""

class NonceBook:
    def __init__(self): self.last={}
    def accept(self, sender, nonce):
        if nonce <= self.last.get(sender, -1): return False
        self.last[sender]=nonce; return True

if __name__ == "__main__":
    b=NonceBook(); assert b.accept("alice",1); assert not b.accept("alice",1); assert b.accept("alice",2)
