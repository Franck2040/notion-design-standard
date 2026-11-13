# Cinq compositions mobile-first à prototyper

Les ordres ci-dessous sont des cibles natives, pas des captures ni des parcours déjà validés. Les états et cas d’essai doivent être adaptés au brief.

## M01

**Capture à une main** — « Nouvelle note » → corps ou titre → sauvegarde → retour à la file « À classer ». N08 si l’action est disponible et prouvée. Afficher l’accès à la fiche créée ou à la file, sans imposer une catégorie lorsqu’elle peut être déterminée plus tard. Exemple : idée saisie en transit, enrichie sur bureau. Vide : « Rien à classer ». Si l’ajout échoue, garder le texte autant que le canal le permet et vérifier la base avant de retenter. **Test** : saisir une idée, interrompre puis rouvrir, et constater une seule fiche avec le texte attendu. Tester hors ligne séparément. Repli : ouvrir une page locale préchargée si cette stratégie a été validée, puis transférer une seule fois vers Inbox.

## M02

**File compacte** — titre « À traiter » → liste avec libellé et priorité/échéance → ouvrir une fiche → revenir à la liste. N10 + N25 + N26. Sur bureau le calendrier ou le board peut rester utile; sur téléphone le tri rend la prochaine action immédiatement visible. Vide : différencier « aucune tâche due » et « aucune fiche accessible ». **Test** : hier, aujourd’hui, demain, sans date et terminé, puis titre sur deux lignes et retour à la file. Repli : lien nommé vers une vue enregistrée, sans tableau horizontal.

## M03

**Lecture et reprise** — reprendre le document actif → titre et état → contenu → détails facultatifs → lien retour. N06 + N05 + N20/N28. Éviter d’ouvrir un panneau latéral à tout prix. Laisser la provenance visible et ne pas cacher un avertissement indispensable. Vide : « Aucun document commencé » et lien vers la collection. **Test** : ouvrir un contenu long avec un média et un lien, lire avec texte agrandi, revenir à la collection. Repli : pleine page sans couverture lourde et lien vers la source.

## M04

**Formulaire sur clavier tactile** — expliquer le résultat et l’accès aux données → une petite série de questions dans l’ordre naturel → envoyer → vérifier la confirmation. N16. Distinguer une question obligatoire d’une question facultative, sans imposer de recherche dans une grande liste à la première étape. L’état vide doit expliquer quoi saisir, l’erreur doit permettre de corriger. **Test** : champ requis manquant, changement de clavier, rotation ou interruption, retour et nouvelle soumission; contrôler la ligne et les droits de lecture. Ne pas présumer que les réponses survivent à toute interruption. Repli : formulaire linéaire ou fiche guidée pour un rôle autorisé.

## M05

**Base volumineuse** — question métier → une vue liée filtrée sur le sous-ensemble utile → entrée « Rechercher / Voir les archives » → fiche. N25/N26. Séparer actif, archive et sans classification dans des vues de la même source. Ne pas promettre une recherche universelle ou une pagination contrôlée par CSS. Vide : préciser le filtre en cours et offrir un chemin vers les données autorisées. **Test** : comparer 0, quelques et un volume représentatif (exemple synthétique 300 fiches), chercher un élément en dehors du sous-ensemble, tester droits et réseau lent. Noter la taille réelle et les temps observés si mesurés. Repli : index de vues filtrées; une table exhaustive reste un outil de bureau.
