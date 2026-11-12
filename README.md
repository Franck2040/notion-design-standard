# Notion Design Standard — un manuel pour concevoir, pas pour décorer

> **Version 1.0 — 10 novembre 2026.** Référentiel public d'architecture de l'information, de design produit, de construction Notion et de validation. En français, conçu pour les humains **et** les agents IA.

**Ce dépôt n'est pas un template Notion**, ni un catalogue de recettes « colle trois colonnes et ajoute des couleurs ». C'est un ensemble de connaissances opérationnelles pour concevoir un système adapté à un besoin réel, le rendre plaisant à utiliser, puis en vérifier le fonctionnement. Les exemples sont illustratifs ; ils ne remplacent pas l'étude des données ni les essais dans l'espace cible.

## Parcours de lecture obligatoire pour une IA

Lire les documents dans l'ordre, **sans remplacer les démonstrations par un résumé** :

| Ordre | Document | Ce qu'il faut y apprendre / produire |
|---|---|---|
| 1 | [AGENTS.md](AGENTS.md) | Contrat d'intervention, interdictions, livrables, définition de « terminé » |
| 2 | [01 — Philosophie & UX](docs/01-product-thinking.md) | Diagnostic, anti-patterns, hiérarchie, esthétique utile et arbitrages |
| 3 | [02 — Recherche & références](docs/02-reference-reviews.md) | Anatomie de six systèmes réels, avantages, limites et éléments réutilisables |
| 4 | [03 — Architecture des données](docs/03-information-architecture.md) | PARA, sources uniques, Inbox, relations, règles de migration |
| 5 | [04 — Interfaces & scénarios](docs/04-layout-patterns.md) | Maquettes textuelles, alternatives desktop/mobile, parcours et micro-interactions |
| 6 | [05 — Implémentation native](docs/05-notion-implementation.md) | Boutons, vues, panneaux, thèmes, bilinguisme, limites, widgets |
| 7 | [06 — Qualité & recette](docs/06-acceptance-tests.md) | Checklist mesurable, tests de non-régression, performances, accessibilité |
| 8 | [07 — Éthique, licence & vente](docs/07-commercialization.md) | Copie autorisée ou non, confidentialité, version commerciale, documentation |
| 8 bis | [08 — Exécution, preuves et direction visuelle](docs/08-agent-execution-and-visual-direction.md) | Faisabilité avant promesse, preuve d'exécution, icônes natives, palette non limitée au bleu, erreurs à éviter |
| 9 | [Exemple guidé : du chaos au cockpit](examples/chaos-to-cockpit.md) | Cas pratique complet : besoins → schéma → interface → migration → validation |
| 10 | [Décisions et changements](DECISIONS.md) | Historique des hypothèses, décisions acceptées et questions ouvertes |

**Consigne de transmission** : quand ce dépôt sert de contexte à une autre IA, lui demander de citer les sections utilisées, de montrer le raisonnement **sous forme de décisions vérifiables** (problème, options, choix, contrepartie), de présenter des exemples et de produire un prototype testable. **Ne jamais répondre uniquement par dix slogans.**

## Pourquoi ce référentiel existe

Un dashboard peut être « joli » et inutilisable. Il peut aussi être rigoureusement organisé, mais si austère qu'on n'a plus envie d'y revenir. Le bon système concilie **rapidité, lisibilité, mémoire, plaisir et confiance**.

Le défaut typique est d'empiler des blocs « Études », « Projets », « Finances » qui ne sont que des liens. L'utilisateur ouvre une page, cherche une sous-page, trouve une liste distincte et recommence. Une **interface de travail** montre l'information utile **ici**, à partir d'une **source unique**, et ouvre le détail seulement quand nécessaire.

### Principes de base

1. **L'accueil est un cockpit, pas un plan de site.** Visible au premier écran : focus, événements imminents, capture, travail actif et navigation. Les archives et les configurations sont secondaires.
2. **Une donnée possède une source de vérité.** Une tâche a une fiche, plusieurs vues. « Aujourd'hui », « Projet X » et « En attente » ne sont pas trois copies.
3. **Une page traite une intention.** Une navigation ne doit pas devenir un inventaire infiniment imbriqué.
4. **La beauté peut avoir une fonction émotionnelle.** Une horloge, une couverture, une illustration ou la météo peuvent créer une pause et inviter à revenir. Il faut doser, pas interdire.
5. **L'UX précède la décoration.** Tester cinq actions réelles avant d'ajouter un widget.
6. **Le système évolue.** Les domaines de vie changent pendant des années ; les informations doivent pouvoir être classées et retrouvées sans reconstruire la page d'accueil.
7. **Le mode mobile n'est pas une miniature du desktop.** Réordonner les informations et proposer une capture très rapide.
8. **La documentation est un composant du produit.** Sans instructions claires sur les champs, les filtres et les dépendances, un template est fragile.
9. **Pas de promesses de fonctionnalités inexistantes.** Notion n'est pas React. Vérifier la version, le forfait, les droits et les contraintes avant d'annoncer un bouton magique.
10. **Pas de recyclage commercial non autorisé.** Un template gratuit peut s'utiliser personnellement ; sa redistribution dépend de sa licence.

## Modèle canonique de navigation (à adapter)

```text
┌──────────────────────┬────────────────────────────────────────────────┐
│ NAVIGATION (~20 %)   │  ACCUEIL — focus du jour / événement suivant    │
│                      ├──────────────┬──────────────┬─────────────────┤
│ ⌂ Accueil            │ Priorités    │ Échéances    │ Capture rapide  │
│ ◷ Aujourd'hui        ├──────────────┴──────────────┴─────────────────┤
│ ▣ Projets            │ [Aujourd'hui] [Cette semaine] [En attente]     │
│ ◇ Domaines           │ Liste compacte de vraies données              │
│ ▤ Notes/Ressources   │ Chaque fiche ouvre un aperçu sans quitter     │
│ ◫ Archives           │ le contexte si possible                       │
│ ⚙ Configuration      ├────────────────────────────────────────────────┤
│                      │ Secteur actif / prochains éléments            │
└──────────────────────┴────────────────────────────────────────────────┘
```

Ce schéma explique **la hiérarchie**, pas une mise en page pixel-perfect. Sous 700 px, la navigation devient une barre compacte et le centre une colonne : capture, focus, échéances, liste.

## Comment exploiter ce référentiel

- **Concevoir un espace personnel** : lire les parcours, inventorier la matière réelle, construire un espace de test sans supprimer les données, itérer.
- **Créer un template premium** : choisir une population et un problème étroit, construire une méthode de travail, vérifier son fonctionnement sur compte gratuit, livrer une page d'accueil et un guide.
- **Améliorer un ancien workspace** : auditer les bases, repérer doublons et pages isolées, établir un plan de migration réversible.
- **Former une IA** : donner le dépôt complet et un contexte d'usage ; exiger les livrables définis par [AGENTS.md](AGENTS.md).

## Bibliographie commentée

Les six templates analysés, les idées retenues et les limites de chacun sont décrits dans [02 — Recherche & références](docs/02-reference-reviews.md). Les liens y sont donnés pour étudier les mécanismes originaux ; **ils ne représentent aucune licence de redistribution**.

## Ce dépôt peut vieillir

Les fonctionnalités Notion, les réglages, forfaits et API changent. En cas de contradiction, **documenter** : (1) ce que dit ce manuel daté, (2) ce que dit la documentation officielle actuelle, (3) ce qui est constaté dans l'interface du compte, (4) le choix pris et les tests. Ne jamais présenter des détails historiques comme garantis dans dix ans.

## Confidentialité

Ce dépôt est **public et volontairement générique**. Pas de données personnelles, secrets, comptes, titres de séjour, dossiers de candidature, journaux privés, finances réelles, ni exports complets de Notion. Toute personnalisation privée doit rester dans un espace privé séparé.

---
**Objectif final :** qu'un designer, un développeur et une IA puissent discuter du même système avec le même vocabulaire, le même niveau d'exigence et une méthode reproductible.


## Mise à jour v1.1 — 12 novembre 2026

Avant toute intervention, lire en priorité les sections 9 et 10 de [AGENTS.md](AGENTS.md) et le [chapitre 08](docs/08-agent-execution-and-visual-direction.md). Elles rendent obligatoires l'audit des capacités réelles, les preuves distinctes de configuration/test, le signalement précoce des limites et les icônes natives sans emojis de substitution. Le design n'est pas limité au bleu et aucune recoloration globale par bouton Notion ne doit être promise sans preuve.
