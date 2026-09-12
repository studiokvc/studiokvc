# RISC Zero : frontière guest et host

Le host prépare les entrées, choisit l image du guest et vérifie la receipt. Le guest exécute une logique déterministe et produit un journal engagé.

La vérification doit lier la receipt à l image attendue et au journal attendu. Une receipt valide ne suffit pas à garantir la correction du statement métier si le programme ou ses entrées sont incorrects.

Cette note complète `risc_zero_receipt_check.py` et `risc_v_isa_trace.py`. Aucune preuve n est générée localement.
