"""Autorisation explicite avant opération FHE."""

class Policy:
    def __init__(self, grants): self.grants = set(grants)
    def allow(self, subject, purpose, key_id): return (subject, purpose, key_id) in self.grants

if __name__ == "__main__":
    p = Policy({("alice","settlement","key-1")})
    assert p.allow("alice","settlement","key-1")
    assert not p.allow("alice","marketing","key-1")
