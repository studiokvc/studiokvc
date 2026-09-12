# Frontière Base / HyperEVM

Un message inter-réseaux doit lier explicitement chain ID, sender, nonce, montant, destination et expiration.

Contrôles : rejeter une chaîne inattendue, un montant nul, un nonce déjà consommé ou une fenêtre expirée. Cette note décrit un invariant documentaire, sans exécution ni dépendance.
