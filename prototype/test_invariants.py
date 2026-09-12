"""Cas nominaux et rejets attendus des prototypes."""
from prototype.base_deposit_check import valid
from prototype.hyperevm_replay_guard import ReplayGuard
from prototype.zk_claim_check import verify
from prototype.fhe_policy_check import Policy

def run():
    assert valid({"sender":"a","amount":1,"chain_id":8453,"nonce":1})
    g=ReplayGuard(); assert g.accept(999,"a",1,"x"); assert not g.accept(999,"a",1,"x")
    assert verify({"statement":"S","verifier_id":"v","proof":"P"},"S","v")
    assert Policy({("a","p","k")}).allow("a","p","k")

if __name__ == "__main__": run(); print("invariants: ok")
