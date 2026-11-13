# Étape 07 — Manuel d’implémentation reproductible

Ne pas commencer par « je vais faire le bouton ». Commencer par identifier **qui agit, depuis quel écran, sur quelle fiche, avec quels droits et quel résultat attendu**. Appliquer le [contrat de faisabilité v1.1](../docs/08-agent-execution-and-visual-direction.md) à chaque action.

## Choisir la recette

| ID | Intention UX | Recette |
| --- | --- | --- |
| R01 | Créer une note sans quitter son espace | [Bouton bloc et Inbox](actions.md#r01--capturer-une-note-dans-la-source-existante) |
| R02 | Changer l’état d’une seule fiche | [Bouton de base](actions.md#r02--modifier-seulement-la-fiche-cliquée) |
| R03 | Demander des champs structurés | [Formulaire](actions.md#r03--recueillir-une-entrée-structurée-avec-un-formulaire) |
| R04 | Retrouver son travail aujourd’hui ou en retard | [Vues liées et onglets](views-and-layout.md#r04--retrouver-le-travail-dans-des-vues-liées) |
| R05 | Reconnaître et reprendre une œuvre | [Galerie, couvertures et états](views-and-layout.md#r05--montrer-des-œuvres-en-galerie) |
| R06 | Ouvrir une fiche cohérente et prête à remplir | [Modèle, panneau et aperçu](views-and-layout.md#r06--préparer-une-fiche-et-choisir-son-ouverture) |
| R07 | Atteindre l’action sur téléphone | [Ordre des blocs et navigation](views-and-layout.md#r07--construire-une-page-lisible-sur-téléphone) |
| R08 | Relier sans recréer ou écraser l’historique | [Relations et reprise](data-and-qa.md#r08--relier-les-fiches-sans-dupliquer-les-données) |
| R09 | Rendre l’espace reconnaissable sans promettre un thème global | [Icônes et palette](data-and-qa.md#r09--donner-une-identité-visuelle-sans-faux-interrupteur) |

## Pré-vol à compléter avant modification

| Contrôle | Consigner |
| --- | --- |
| Parcours | Rôle réel, déclencheur, résultat, preuve observable et fallback |
| Cibles | ID page hôte, ID base, ID source, propriétés exactes, ID vue/modèle si pertinent |
| Périmètre | Ce qui change dans une vue, dans une fiche ou dans toute la base |
| Accès | Droits dans Notion pour auteur **et** utilisateur final, droits de la connexion, accès aux sources reliées |
| Capacités | Interface disponible ? Endpoint et version documentés ? Outil du connecteur présent ? Forfait compatible avec **l’action précise** ? |
| Essai et retrait | Zone d’essai ou données QA identifiables, valeurs initiales, procédure de retour arrière |

**Les trois canaux sont indépendants.** Une capacité documentée en REST ne garantit ni sa présence dans le connecteur, ni l’autorisation sur le compte. Une opération d’écriture réussie ne valide pas le parcours de l’utilisateur. Dans ce manuel, « documenté » signifie que la méthode est décrite, **pas qu’elle a été exécutée dans votre espace**. La version REST `2026-03-11` est celle indiquée dans la [référence Create a view](https://developers.notion.com/reference/create-view) lors de la rédaction. Vérifier la version et les schémas avant usage.

## Ordre d’exécution

1. Lire l’existant, résoudre les IDs, confirmer une seule source de vérité et noter les valeurs initiales.
2. Choisir la recette et le canal réalisable. Si la config native manque, annoncer précisément ce que l’agent ne peut pas faire ou vérifier avant de promettre le résultat.
3. Configurer un seul parcours. Rechercher un objet déjà créé avant de répéter une écriture dont le résultat est incertain. En cas de refus d’accès, diagnostiquer le partage et les capacités, sans tenter un accès plus large de sa propre initiative.
4. Relire la config puis jouer les [tests et consigner les preuves](data-and-qa.md#journal-de-recette). Tester les rôles et l’affichage séparément. Ne pas convertir un état `NON TESTÉ` en réussite.
5. N’élargir le déploiement qu’après l’essai. Retirer seulement les objets QA ou changements recensés. Réutiliser les [critères de recette existants](../docs/06-acceptance-tests.md).

## Sources de référence

- [Capacités des connexions](https://developers.notion.com/reference/capabilities) et [partage et permissions](https://www.notion.com/help/sharing-and-permissions).
- [API des vues](https://developers.notion.com/reference/view), [création de vue](https://developers.notion.com/reference/create-view), [création de page](https://developers.notion.com/reference/post-page).
- [Bouton bloc](https://www.notion.com/help/buttons), [bouton de base](https://www.notion.com/help/database-buttons), [formulaires](https://www.notion.com/help/forms).
- [Vues, filtres et tris](https://www.notion.com/help/views-filters-and-sorts), [modèles](https://www.notion.com/help/database-templates), [mises en page des fiches](https://www.notion.com/help/layouts) et [colonnes](https://www.notion.com/help/columns-headings-and-dividers).
