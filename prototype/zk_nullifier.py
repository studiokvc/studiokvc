"""Protection contre la double utilisation d une preuve ZK."""

class Nullifiers:
    def __init__(self): self.used=set()
    def consume(self, value):
        if not value or value in self.used: return False
        self.used.add(value); return True

if __name__ == "__main__":
    n=Nullifiers(); assert n.consume("nf-1"); assert not n.consume("nf-1")
