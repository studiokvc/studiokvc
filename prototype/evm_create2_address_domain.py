"""Prototype documentaire du domaine d'adresse CREATE2.

Le calcul est local et déterministe: aucune transaction ni déploiement n'est
réalisé. L'objectif est de rendre visibles les entrées qui doivent rester liées.
"""

import hashlib


CREATE2 = b"\xff"


def create2_address(deployer: bytes, salt: bytes, init_code: bytes) -> bytes:
    if len(deployer) != 20:
        raise ValueError("deployer doit contenir 20 octets")
    if len(salt) != 32:
        raise ValueError("salt doit contenir 32 octets")
    digest = hashlib.sha3_256(CREATE2 + deployer + salt + hashlib.sha3_256(init_code).digest()).digest()
    return digest[-20:]


def same_deployment_domain(left: tuple[bytes, bytes, bytes], right: tuple[bytes, bytes, bytes]) -> bool:
    """Détecte si deux annonces correspondent exactement au même domaine."""
    return left == right


if __name__ == "__main__":
    address = create2_address(b"\x01" * 20, b"\x02" * 32, b"init-code")
    print(address.hex())
