# Étape 08 — Concevoir d’abord pour le téléphone

Un écran mobile a son propre ordre de travail. Par exemple, le calendrier éditorial sert à **planifier** sur bureau et à **vérifier la prochaine publication** sur téléphone. On peut fournir deux entrées vers les mêmes données. Ne pas dupliquer une base pour obtenir deux interfaces.

## Concevoir le premier écran

1. Écrire le scénario : où la personne est, temps disponible, une ou deux mains, réseau, ce qu’elle doit décider ou enregistrer.
2. Placer l’action ou la réponse clé dans le flux vertical, **hors des colonnes**. Sur une page de lecture, le document passe avant la capture. Sur une page de capture, faire l’inverse.
3. Prototyper avec une colonne native, un libellé explicite et une vue Liste. Commencer avec **titre et une ou deux propriétés** sur la liste. Laisser le reste à la fiche. Ce sont des budgets de conception, pas des limites Notion.
4. Si l’ordre utile diffère trop entre bureau et téléphone, proposer une page compacte nommée « Capture » ou « Sur le terrain » dans la navigation. Lier les mêmes sources. Ne pas promettre de bascule automatique, de CSS, d’en-tête fixe ou de geste personnalisé dans Notion.
5. Tester le parcours complet, y compris le clavier ouvert et le retour. Comparer le comportement réel à la [recette R07](../implementation-recipes/views-and-layout.md#r07--construire-une-page-lisible-sur-téléphone).

| Parcours | Première surface | À déplacer hors du chemin principal | Repli |
| --- | --- | --- | --- |
| [M01 Capture](patterns.md#m01) | Une action, titre ou texte | Classement et enrichissement | Nouvelle fiche dans la source, ou capture hors ligne préparée |
| [M02 File compacte](patterns.md#m02) | Liste « À traiter » | Table, board, calendrier mensuel | Lien vers une vue enregistrée |
| [M03 Lecture](patterns.md#m03) | Titre, état et contenu | Propriétés secondaires, widgets | Pleine page + retour |
| [M04 Formulaire](patterns.md#m04) | Contexte puis premier champ | Champs facultatifs sans effet immédiat | Formulaire linéaire ou fiche guidée autorisée |
| [M05 Base volumineuse](patterns.md#m05) | Sous-ensemble utile et accès à la recherche | Toutes les propriétés et archives | Index de vues par usage |

## Contrôler sur appareil

- Couvrir au minimum **un téléphone représentatif** et le rôle final. Si seule l’émulation web est disponible, la nommer et laisser l’application native non testée. Une maquette SVG n’est pas un émulateur.
- Tester une largeur étroite, un titre long, le texte agrandi si disponible, le mode clair/sombre, le clavier ouvert, l’état vide, l’accès refusé et une interruption réseau pertinente. Rechercher une lecture sans défilement horizontal sur le parcours principal. Le [critère WCAG Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) sert de repère de conception, pas de déclaration de conformité de Notion.
- Noter appareil/OS, app ou navigateur, rôle, réseau, nombre d’étapes et résultat observé. Pour une création, vérifier **la fiche persistée et l’absence de doublon**. Un seuil de temps est une hypothèse tant qu’il n’a pas été mesuré.
- Le [mode hors ligne](https://www.notion.com/help/use-pages-offline) dépend de l’application et du contenu disponible localement. Préparer et tester avant de promettre un fonctionnement hors ligne, en particulier pour les bases, relations, boutons et formulaires. Ne pas extrapoler au navigateur.

Sources : [Notion mobile](https://www.notion.com/help/notion-for-mobile), [colonnes et titres](https://www.notion.com/help/columns-headings-and-dividers), [vues et filtres](https://www.notion.com/help/views-filters-and-sorts), [formulaires](https://www.notion.com/help/forms).
