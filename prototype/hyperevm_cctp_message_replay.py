"""Prototype documentaire de garde anti-rejeu pour un message CCTP.

Il décrit le contrôle local d'un message inter-chaînes; il ne contacte aucun
réseau et ne remplace pas la vérification d'attestation du protocole.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class MessageKey:
    source_domain: int
    nonce: int
    message_hash: str


class ReplayRegistry:
    def __init__(self) -> None:
        self._consumed: set[MessageKey] = set()

    def accept_once(self, key: MessageKey) -> bool:
        if key in self._consumed:
            return False
        self._consumed.add(key)
        return True

    def consumed(self, key: MessageKey) -> bool:
        return key in self._consumed


if __name__ == "__main__":
    registry = ReplayRegistry()
    key = MessageKey(0, 7, "attested-message-hash")
    print(registry.accept_once(key), registry.accept_once(key))
