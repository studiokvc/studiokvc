# Index et références

## Parcours

1. Architecture : GUIDE-BASE-CREATION.md et GUIDE-HYPEREVM-INTEROPERABILITE.md.
2. Invariants : prototype/base_deposit_check.py:valid, prototype/hyperevm_replay_guard.py:ReplayGuard.accept.
3. Confidentialité : prototype/zk_claim_check.py:verify et prototype/fhe_policy_check.py:Policy.allow.
4. Limites : GUIDE-ZK-PRODUCTION.md et GUIDE-FHE-CONFIANCE.md.

## Matrice

| Domaine | Garantie illustrée | Hypothèse critique | Rejet clé |
|---|---|---|---|
| Base | dépôt sur la bonne chaîne | dérivation/données disponibles | montant nul ou chain ID incorrect |
| HyperEVM | anti-rejeu | nonce et domaine fiables | clé déjà consommée |
| ZK | claim lié au contexte | verifier et statement authentiques | preuve absente ou mauvais verifier |
| FHE | accès finalisé | politique et clé valides | purpose non autorisé |
