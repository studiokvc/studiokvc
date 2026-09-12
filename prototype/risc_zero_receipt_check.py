"""Contrôle de cohérence d une receipt RISC Zero, sans prouver le calcul."""

def valid_receipt(receipt, expected_image, expected_journal):
    required={"image_id","journal","seal"}
    return isinstance(receipt,dict) and required <= receipt.keys() and receipt["image_id"] == expected_image and receipt["journal"] == expected_journal and bool(receipt["seal"])

if __name__ == "__main__":
    r={"image_id":"img-1","journal":"commitment","seal":"opaque"}
    assert valid_receipt(r,"img-1","commitment")
    assert not valid_receipt(r,"img-2","commitment")
