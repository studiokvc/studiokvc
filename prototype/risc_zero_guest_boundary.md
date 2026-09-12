# RISC Zero : frontière guest / host

Le host prépare les entrées, sélectionne l image du guest et demande une preuve d exécution. Le guest exécute une logique déterministe et publie un journal engagé.

Le vérificateur doit lier la receipt à l image attendue et au journal attendu. Une receipt valide ne garantit pas à elle seule que le statement métier est correct si le programme vérifié, ses entrées ou son interprétation sont mauvais.

Références internes : `risc_zero_receipt_check.py` et `risc_v_isa_trace.py`. Cette note est documentaire ; aucune preuve n est générée localement.
