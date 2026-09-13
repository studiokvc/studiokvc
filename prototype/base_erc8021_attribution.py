"""Prototype documentaire: validation d'une attribution ERC-8021.

Ce modèle ne signe ni n'envoie de transaction. Il rend explicites les invariants
à contrôler avant d'ajouter des métadonnées d'attribution à un calldata EVM.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Attribution:
    builder: str
    version: str
    suffix: bytes


def validate_attribution(value: Attribution) -> None:
    if not value.builder or len(value.builder) > 64:
        raise ValueError("builder absent ou trop long")
    if not value.version or len(value.version) > 32:
        raise ValueError("version absente ou trop longue")
    if not value.suffix:
        raise ValueError("suffix d'attribution vide")
    if any(byte > 0xFF for byte in value.suffix):
        raise ValueError("octet d'attribution invalide")


def build_record(value: Attribution) -> dict[str, str]:
    """Retourne une représentation stable pour journalisation et audit."""
    validate_attribution(value)
    return {
        "builder": value.builder,
        "version": value.version,
        "suffix_hex": value.suffix.hex(),
    }


if __name__ == "__main__":
    print(build_record(Attribution("studio-kvc", "1", b"base")))
