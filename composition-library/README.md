# Bibliothèque de compositions Notion — index v1.1

> **10 patterns originaux documentés**, construits à partir de problèmes d'usage et d'observations de structures existantes. Il ne s'agit **ni de templates importables**, ni d'une extraction de code ou d'assets tiers. Les proportions sont des hypothèses à tester, non des mesures universelles.

## Sélecteur

| Pattern | Quand l'utiliser | Première action | Première information | À éviter si… |
| --- | --- | --- | --- | --- |
| [01 — Cockpit focalisé](patterns.md#01--cockpit-focalisé) | Besoin d'agir chaque jour | Capturer / terminer | Actions urgentes | Usage surtout lecture longue |
| [02 — Studio d'œuvres](patterns.md#02--studio-dœuvres) | Images, morceaux, créations | Nouvelle inspiration | Œuvre active | Aucune donnée visuelle |
| [03 — Centre documentaire](patterns.md#03--centre-documentaire) | Procédures, recherche | Chercher / classer | Sources vérifiées | Mesures temps réel prioritaires |
| [04 — Console de projets](patterns.md#04--console-de-projets) | Plusieurs livrables et échéances | Nouvelle tâche/projet | Bloquants | Très peu de projets |
| [05 — Calendrier éditorial](patterns.md#05--calendrier-éditorial) | Publication multicanal | Nouvelle idée | À publier ensuite | Publications sporadiques |
| [06 — Journal et routines](patterns.md#06--journal-et-routines) | Ritualisation personnelle | Nouvelle entrée | Aujourd'hui | Données sensibles en espace partagé |
| [07 — Hub d'apprentissage](patterns.md#07--hub-dapprentissage) | Cours, révisions, projets | Nouvelle note / séance | Prochaine révision | L'usage principal est administratif |
| [08 — CRM de suivi](patterns.md#08--crm-de-suivi) | Relations avec contacts | Ajouter interaction | Relances dues | Pas de suivi relationnel régulier |
| [09 — Espace communautaire](patterns.md#09--espace-communautaire) | Événements et bénévoles | Nouvel événement | Prochaine activité | Accès publics mal configurés |
| [10 — Portail de lecture](patterns.md#10--portail-de-lecture) | Bibliothèque de contenus | Sauver une source | Lire/reprendre | Priorité aux décisions urgentes |

## Composition : règles communes

1. Identifier **la question du premier écran**, pas simplement les sections à montrer.
2. Ajouter d'abord le **minimum fonctionnel** : une capture, une vue courante filtrée, une navigation courte.
3. Introduire un seul élément de signature émotionnelle (couverture contextuelle, galerie, titre éditorial, accent coloré, etc.).
4. Reprendre une base existante via **vue liée** plutôt que dupliquer les données.
5. Distinguer navigation décorative, bouton natif et formulaire qui enregistre.
6. Réserver les tableaux complets et archives à une page spécialisée.
7. Sur mobile, ordonner les blocs selon le geste prioritaire : capture, décision ou lecture. Ne pas imposer l’ordre du cockpit à toutes les pages. Voir [mobile-first](../mobile-first/README.md).
8. Les couleurs et la largeur sont indicatives ; les options sont limitées aux réglages natifs Notion.
9. Tester les états **vide**, **quelques entrées**, **surcharge**, **erreur/perte de permission**, **mobile** et **mode sombre**.
10. La bibliothèque sert à **composer et adapter**, pas à copier une page complète.

## Structures étudiées en espace privé (consultation non destructive)

> La table conserve des conclusions générales. Les liens, identifiants et visuels privés ne sont pas reproduits.

| Type examiné | Observations structurelles vérifiées | Risques / compromis |
| --- | --- | --- |
| Second Brain — variante PARA | Sidebar environ 19 %, 6 boutons de capture, multiples vues de données et liens de domaines | Facile de multiplier les tables et le scroll |
| Second Brain — variante synchronisée | Sidebar 25 %, bloc synchronisé et bases liées | Bonne cohérence de navigation ; droits d'accès et ordre mobile |
| Task Tracker | Capture, statut, urgence, échéances, matrice de priorités et instructions détaillées | Interface riche et formules dépendantes de libellés de statut |
| Habit Tracker | Suivi quotidien, historique, streak et mode d'emploi long | Éviter les indicateurs culpabilisants ou non fiables |
| Content Calendar | Actions rapides, navigation de sources, priorité aux éléments à traiter, calendrier, campagne et synthèse | Risque de surcharge de widgets |
| Project Management | Dashboard de tâches, projets actifs, chronologie et répartitions | Trop d'indicateurs pour petite équipe |
| Knowledge Vault | Sidebar 25 %, catégories de médias et base de contenu | Navigation profonde, dépendances d'assets et attribution |
| Life OS actuel | Boutons, notes, projets, navigation d'espaces et vues multiples | Des tests visuels/interactifs restent distincts de la structure |

**Méthode** : lecture du contenu et des tags de structure des pages Notion ; ni récupération d'une licence de redistribution, ni preuve du comportement visuel desktop/mobile. Les templates propriétaires restent dans le workspace du propriétaire. Les patterns de ce dépôt sont rédigés indépendamment.

## Sources publiques de capacités

- [Notion — vues, filtres, tris](https://www.notion.com/help/views-filters-and-sorts)
- [Notion — boutons de base](https://www.notion.com/help/database-buttons)
- [Notion — mises en page](https://www.notion.com/fr/help/layouts)
- [Notion — dashboard view](https://www.notion.com/help/dashboards) : vue réservée aux plans Business et Enterprise selon l'aide consultée en novembre 2026 ; **ne pas la présumer disponible**.
- [Notion — blocs synchronisés](https://www.notion.com/en-gb/help/synced-blocks)

## Démonstrations visuelles

L’[atlas annoté](../visual-atlas/README.md) met en image trois compositions (cockpit, galerie créative et bibliothèque de recherche), chacune avec un contre-exemple et un ordre de lecture mobile. Réutiliser la hiérarchie si le besoin la justifie, pas la disposition entière par défaut.

## Dix compositions illustrées

Les [dix planches](visual-cards.md) réunissent proportions, gestes, états vides, blocs natifs, limites et références publiques de modèles Notion. Elles distinguent explicitement maquette originale et exemple natif tiers.
