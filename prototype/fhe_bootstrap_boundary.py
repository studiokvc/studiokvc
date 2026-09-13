"""Prototype documentaire de frontière de bootstrapping FHE.

Le modèle suit un budget abstrait de bruit et refuse les transitions de
paramètres incohérentes. Il ne chiffre aucune donnée réelle.
"""

from dataclasses import dataclass


@dataclass
class CiphertextBudget:
    remaining_noise: int
    bootstrap_cost: int

    def consume(self, cost: int) -> None:
        if cost < 0:
            raise ValueError("coût négatif")
        self.remaining_noise -= cost

    def needs_bootstrap(self) -> bool:
        return self.remaining_noise < self.bootstrap_cost

    def bootstrap(self, refreshed_noise: int) -> None:
        if refreshed_noise < self.bootstrap_cost:
            raise ValueError("budget rafraîchi insuffisant")
        self.remaining_noise = refreshed_noise


if __name__ == "__main__":
    budget = CiphertextBudget(10, 4)
    budget.consume(7)
    if budget.needs_bootstrap():
        budget.bootstrap(10)
    print(budget.remaining_noise)
