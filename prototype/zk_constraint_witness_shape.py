"""Prototype documentaire de validation de witness ZK.

Avant de lancer un prover, on vérifie la cardinalité et la séparation des
entrées publiques et privées. Cela aide à repérer les circuits sous-contraints.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class WitnessShape:
    public_count: int
    private_count: int


def validate_shape(shape: WitnessShape, public: list[int], private: list[int]) -> None:
    if shape.public_count != len(public):
        raise ValueError("nombre d'entrées publiques inattendu")
    if shape.private_count != len(private):
        raise ValueError("nombre d'entrées privées inattendu")
    if shape.public_count < 0 or shape.private_count < 0:
        raise ValueError("cardinalité négative")


def public_projection(public: list[int]) -> tuple[int, ...]:
    """Projection immuable utilisée pour comparer les annonces de circuit."""
    return tuple(public)


if __name__ == "__main__":
    validate_shape(WitnessShape(1, 2), [42], [3, 4])
    print("witness shape accepted")
