# Registre des décisions et questions à vérifier

**2026-11-10 — v1.0**

## Décisions fortes

| Décision | Motivation | Contrepartie |
|---|---|---|
| Dashboard compact | Premier écran utile, moins de scroll | Toutes les bases ne seront pas visibles |
| Architecture « source unique » | Limite contradictions et doublons | Relations et vues à concevoir |
| Navigation latérale légère | Repères stables, inspiration Second Brain | Notion n'offre pas la même sidebar sticky que CSS |
| Thème clair par défaut | Lisibilité, ambiance calme | Les contrastes et le mobile doivent être vérifiés |
| Icônes natives cohérentes | Longévité, faible maintenance | Moins de personnalisation extrême |
| Ambiance assumée | Météo/horloge peuvent rendre l'espace accueillant | Widgets externes à auditer |
| Contenus détaillés dans pages spécialisées | L'accueil reste léger | Nécessite navigation de qualité |
| Séparation référentiel public / données privées | Confidentialité et réutilisabilité | Deux documents/surfaces à maintenir |
| Support FR/EN possible avec vues communes | Immersion sans double saisie | Traduction des libellés à entretenir |
| Préservation avant migration | Ne pas perdre les notes historiques | Travail de classification plus long |

## Décisions non validées / paramètres à tester

- Position exacte de l'horloge et de la météo, taille et source autorisée.
- Existence et comportement d'une action Inbox native à travers les différents appareils.
- Schéma définitif de « Knowledge » après audit de l'existant.
- Représentation des inspirations musicales et du journal vocal.
- Définition de « tâche d'aujourd'hui » : date prévue vs date limite vs priorité.
- Palette exacte dans les couleurs natives Notion et covers éventuelles.
- Équilibre mobile entre navigation, widgets et tâches.
- Bilinguisme par deux pages vs libellés bilingues sur une seule page.
- Limitations de forfait pour charts, automatisations et autres composants.
- Conditions de licence des assets de templates gratuits avant redistribution.

## Journal de changement

- v1.0 : dépôt créé pour préserver les principes, les cas d'usage, les références et les critères de test, indépendamment des données privées du workspace.
- Les prochaines modifications doivent indiquer : date, problème résolu, justification, incompatibilité éventuelle et lien vers le test.

## Consigne

Un futur agent peut proposer un autre design que celui du manuel **s'il explique les compromis et valide les parcours**. Le but n'est pas de figer un style pour dix ans ; c'est d'empêcher l'oubli de la logique, des exemples et de la rigueur.


## 2026-11-12 — v1.1 : qualité et langage de preuve

- **Décision** : tout agent vérifie sa capacité d'action et sa capacité de test avant toute promesse. Les états `présent`, `configuré`, `testé` et `validé` sont distincts. **Motif** : éviter les annonces trompeuses et les boucles de modifications partielles. **Contrepartie** : rendre les limites visibles tôt.
- **Décision** : les nouveaux éléments d'interface utilisent des icônes natives Notion, pas des emojis tapés devant les liens. **Motif** : cohérence, entretien, scannabilité. **Contrepartie** : respecter les possibilités de l'éditeur et vérifier les icônes héritées.
- **Décision** : palette contextuelle multicolore mais contrôlée, bleu non obligatoire ; vert sauge possible. **Motif** : éviter un thème générique. **Contrepartie** : tests de contraste, mobile et sens des couleurs.
- **Décision** : ne pas promettre de bouton de recoloration globale sans démonstration native ou intégration explicitement autorisée et testée.
- **Décision** : séparer la documentation publique des audits et données personnelles hébergés dans l'espace privé.

Les détails normatifs figurent dans [08 — Contrat d'exécution et direction visuelle](docs/08-agent-execution-and-visual-direction.md).

## 2026-11-13 — v1.5 : variantes, téléphone et évolution

- Étendre les dix compositions sans les transformer en gabarits universels. Garder la référence Notion publique distincte de l’illustration originale.
- Documenter les interactions par ID stable et l’ouverture des fiches séparément du panneau de détails.
- Concevoir le premier geste mobile selon le contexte. Réutiliser les mêmes données même si le chemin d’entrée change.
- Maintenir les règles à partir d’un signal et d’un test reproductible. Les benchmarks du guide restent à exécuter dans l’espace cible.

## 2026-11-16 — v1.6 : ergonomie quotidienne, navigation sans flèches et limites calendrier

- **Décision — Navigation sans flèches `↗` (`@Page`)** : dans la barre de navigation ou le menu latéral d'un dashboard, placer directement les vraies sous-pages ou bases (`inline="false"`) plutôt que des mentions `@Page`, afin d'éviter les flèches de renvoi `↗` sur les icônes et de garder un menu propre.
- **Décision — Accès rapide aux tâches et densité réelle** : un utilisateur qui gère simultanément études, travail, projets et quotidien doit tout retrouver vite. Prévoir un accès direct aux tâches dès l'accueil (onglet dédié + page dédiée dans la navigation) sans sur-simplifier son quotidien.
- **Décision — Limite native du calendrier Notion (pas de grille horaire)** : une vue `Calendar` native dans une page Notion (mois ou semaine) n'affiche pas de colonne d'heures sur la gauche ni de ligne rouge en temps réel. Lorsque l'utilisateur a besoin d'un planning horaire heure par heure (time-blocking à 8 colonnes : heures + 7 jours), le documenter explicitement et orienter vers **Notion Calendar** (`calendar.notion.so`, connecté à la base via « Gérer avec Notion Calendar ») ou un widget dédié — ne jamais laisser croire que la vue calendrier native de Notion sait le faire.
