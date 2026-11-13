# Catalogue de composants Notion — index v1.0

> 24 fiches identifiées, dont 16 composants de base et 8 patterns composites. **Catalogue de sélection et de recette, non code directement exécutable**. Il distingue fonctionnalités natives, limitations du forfait et widgets externes. Pour l'implémentation, consulter [fiches détaillées](native-components.md) et [manifest JSON](manifest.json).

## Règles d'utilisation pour les agents

1. Sélectionner les composants en fonction de la question utilisateur ; **ne pas empiler les composants pour montrer qu'ils existent**.
2. Pour chaque composant choisi : source de vérité, affichage, permissions, interactions, fallback, test et source officielle.
3. Toujours consulter la documentation Notion à jour ; l'état ci-dessous correspond à une revue documentaire de **novembre 2026**, pas à la garantie d'un plan ou d'un workspace.
4. Ne pas confondre **bloc visible**, **action configurée** et **action exécutée puis vérifiée**.
5. Pas d'emoji de substitution dans l'interface finale ; utiliser l'iconographie native, avec couleur/contextes de sens.
6. Ne pas importer visuels ou bases d'un template tiers sans licence explicite. Les modèles inspectés dans l'espace utilisateur ont servi uniquement d'inspiration structurelle.
7. Lire le [contrat de faisabilité](../docs/08-agent-execution-and-visual-direction.md) avant d'agir.

## Tableau de choix

| ID | Composant | Intention | Statut / condition majeure |
| --- | --- | --- | --- |
| N01 | Page et sous-page | Contenu durable | Natif |
| N02 | En-tête et typographie | Hiérarchie | Natif, typographies limitées |
| N03 | Callout | Guidance / alerte | Natif, sans saturation |
| N04 | Colonnes | Zones desktop | Natif, reflow mobile à tester |
| N05 | Toggle | Détail progressif | Natif |
| N06 | Mention de page | Navigation contextuelle | Natif, icône réelle |
| N07 | Blocs synchronisés | Navigation répétée | Natif, droits du bloc source |
| N08 | Bouton de page | Action de capture/navigation | Natif, actions à configurer et tester |
| N09 | Base de données | Source de vérité | Natif, schéma relationnel |
| N10 | Vue liste | Lecture rapide | Natif |
| N11 | Vue table | Édition riche | Natif |
| N12 | Vue board | Statuts / pipeline | Natif |
| N13 | Vue galerie | Objets visuels | Natif |
| N14 | Vue calendrier | Échéances datées | Natif |
| N15 | Vue timeline | Durées et dépendances | Natif ; droits/plan à revérifier |
| N16 | Vue formulaire | Capture structurée | Natif ; tester soumission et propriétés |
| N17 | Bouton de base | Modifier/créer depuis une fiche | Natif ; certaines actions payantes |
| N18 | Relations / rollups | Cohérence multi-objets | Natif |
| N19 | Formules | Indicateurs dérivés | Natif, formules à vérifier |
| N20 | Mise en page des fiches | Propriétés utiles | Native, **s'applique à toutes les fiches de la base** |
| N21 | Graphique | Tendances / décompte | Natif, restrictions et quota selon plan |
| N22 | Dashboard view | Plusieurs widgets de données | **Business/Enterprise** selon doc 2026 |
| N23 | Embed externe | Horloge/météo/outil | Externe, connexion/performance/privacy |
| N24 | Bloc de fichiers et média | Lecture / illustration | Natif, licences et permissions |

## Patterns composites (combinaisons, pas composants Notion séparés)

| Pattern | Composition | Test critique |
| --- | --- | --- |
| C01 | Capture rapide + Inbox + tri | Une nouvelle note apparaît dans la bonne base |
| C02 | Actions du jour + retards | États et échéances correctement filtrés |
| C03 | Galerie d'œuvres + page détaillée | L'original et ses versions restent liés |
| C04 | Navigation latérale par mentions/synced block | Retour et permissions correctes |
| C05 | Index documentaire + source | Recherche et provenance préservées |
| C06 | Projet + tâches liées | Même tâche visible dans deux vues sans duplication |
| C07 | Calendrier + backlog | Date vide conservée dans le backlog |
| C08 | KPI calculé + vue source | Valeur reproductible, aucun chiffre fabriqué |

## Usage interdit / limites fréquemment confondues

- **NotionKit / NotionKit-Elements** : bibliothèques HTML/CSS qui imitent Notion ; **ce ne sont pas des composants natifs à coller dans une page Notion**. Utile pour apprendre les règles de hiérarchie, pas pour annoncer un bouton Notion fonctionnel.
- **notion-arena** : contient notamment widgets et composants externes ; ils peuvent exiger un hébergement, autorisations, licences et maintenance, et ne deviennent pas « natifs » par simple embed.
- **Scripts du cookbook Notion** : exemples d'intégration/API, non garantie que chaque configuration de bouton natif soit possible via l'API du connecteur.
- **Vues dashboard** : disponibles uniquement sur Business/Enterprise selon [la documentation](https://www.notion.com/help/dashboards), ne pas les présumer disponibles.
- **Mise en page de base** : s'applique à l'ensemble des fiches, pas à une seule vue. Voir [Layouts](https://www.notion.com/fr/help/layouts).
- **Formules et automations** : ne jamais utiliser des KPI ou un processus automatique sans vérifier données, triggers, règles et permissions.

## Références publiques vérifiées

- [Notion Help — Database views](https://www.notion.com/help/views-filters-and-sorts)
- [Notion Help — Forms](https://www.notion.com/help/forms)
- [Notion Help — Database buttons](https://www.notion.com/help/database-buttons)
- [Notion Help — Layouts](https://www.notion.com/fr/help/layouts)
- [Notion Help — Dashboards](https://www.notion.com/help/dashboards)
- [Notion Help — Synced blocks](https://www.notion.com/en-gb/help/synced-blocks)
- [Notion — official cookbook](https://github.com/makenotion/notion-cookbook) (MIT, exemples de code sous contrôle de licence)
- [AgentsORG/DESIGN](https://github.com/AgentsORG/DESIGN) (MIT, approche d'intention et contraintes)
- [JUNGHERZ/NotionKit](https://github.com/JUNGHERZ/NotionKit) (MIT, CSS **extérieur à Notion**)
- [SynergyFlowLabs/notion-arena](https://github.com/SynergyFlowLabs/notion-arena) (widgets externes, vérifier licence/conditions fichier par fichier)

**Aucun code, visuel, composant ou texte de template tiers n'a été copié** dans ce catalogue. Les recettes ont été rédigées pour ce projet.

## Passer de la fiche à la configuration

Pour les boutons, formulaires, vues, galeries, panneaux et relations, ouvrir le [manuel d’implémentation](../implementation-recipes/README.md). Il distingue configuration native, écriture directe des données et preuve d’interaction. L’[atlas](../visual-atlas/README.md) montre où placer les composants selon le parcours.
