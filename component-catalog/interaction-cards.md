# Fiches de décision — interactions et présentation

Ces cartes complètent les [fiches de base](native-components.md) et ne prouvent aucune action exécutée dans un workspace. Choisir d’abord une intention, vérifier le [pré-vol](../implementation-recipes/README.md), puis tester le cas nominal, le repli et les rôles réels.

| Si le besoin est… | Choisir d’abord | Éviter |
| --- | --- | --- |
| Créer vite, peu de saisie | N08 | Une fausse carte qui ne déclenche rien |
| Imposer plusieurs réponses | N16 | Exposer la base ou simuler un formulaire avec des blocs |
| Changer un état sur une ligne | N17 | Une action qui touche toute une sélection |
| Réutiliser les objets existants | N25 et N26 | Copier la base ou utiliser un filtre comme permission |
| Passer du résumé au détail | N05, N20 ou N28 selon le périmètre | Cacher l’action primaire ou confondre ouverture et mise en page |

## N03

**Callout**

- **Quand l’utiliser** — Guidance locale ou état vide avec une action; pas pour chaque section.
- **Variantes et paramètres** — Consigne neutre, alerte, état vide; choisir icône native, couleur et lien. Placer le message près de l’action concernée.
- **Limite et mauvais usage** — Ne pas utiliser la couleur seule ni simuler un bouton. Si l’icône manque, écrire un libellé.
- **Test d’acceptation et repli** — Lire en clair/sombre, ouvrir le lien et vérifier qu’une alerte reste claire sans couleur.
- **Source** — [Documentation Notion](https://developers.notion.com/reference/block).

## N05

**Toggle**

- **Quand l’utiliser** — Détail facultatif qu’on n’ouvre pas à chaque visite; éviter pour un prérequis.
- **Variantes et paramètres** — Toggle simple ou titre repliable; mettre la conséquence dans le titre, limiter l’imbrication.
- **Limite et mauvais usage** — Les détails cachés peuvent être ignorés. L’action critique et l’information urgente restent hors du toggle.
- **Test d’acceptation et repli** — Ouvrir et fermer au toucher, vérifier le titre long, puis refaire la tâche principale sans ouvrir le toggle.
- **Source** — [Documentation Notion](https://www.notion.com/help/columns-headings-and-dividers).

## N06

**Mention**

- **Quand l’utiliser** — Renvoi vers une page déjà existante; choisir un lien externe pour une source web.
- **Variantes et paramètres** — Mention dans le texte ou liste de navigation; utiliser le sélecteur et vérifier destination et titre.
- **Limite et mauvais usage** — Une mention ne donne aucun droit. Prévoir une navigation secondaire si la cible est réservée.
- **Test d’acceptation et repli** — Ouvrir et revenir avec le rôle final; renommer une cible QA et contrôler la mention.
- **Source** — [Documentation Notion](https://www.notion.com/help/mentions).

## N08

**Bouton de page**

- **Quand l’utiliser** — Créer une note ou aller à un endroit précis depuis le contexte; pas pour imposer un questionnaire.
- **Variantes et paramètres** — Configurer nom/verbe, icône, base cible, valeurs par défaut, enchaînement et confirmation si pertinente.
- **Limite et mauvais usage** — Un lien ou un POST de page ne configure pas le bouton. Vérifier droits et actions payantes.
- **Test d’acceptation et repli** — Cliquer une fois avec le rôle final, contrôler ID, valeurs et présence dans la vue attendue. Repli : Nouveau dans la vue.
- **Source** — [Documentation Notion](https://www.notion.com/help/buttons).

## N13

**Galerie**

- **Quand l’utiliser** — Reconnaître une œuvre, un objet ou une collection par l’image; sinon choisir Liste.
- **Variantes et paramètres** — Petite/moyenne/grande selon l’espace; source de couverture, propriétés visibles, filtre et ordre de carte.
- **Limite et mauvais usage** — L’état ne doit pas dépendre du visuel. Recadrage et largeur mobile ne sont pas garantis.
- **Test d’acceptation et repli** — Tester image paysage, portrait et absente, titre long et accès à la fiche. Repli : liste titre + statut.
- **Source** — [Documentation Notion](https://www.notion.com/help/views-filters-and-sorts).

## N16

**Formulaire**

- **Quand l’utiliser** — Poser des questions structurées à un répondant; pas pour éditer une fiche existante.
- **Variantes et paramètres** — Choisir champs, libellés, ordre, obligatoires, mode de partage, confirmation et anonymat si prévu.
- **Limite et mauvais usage** — Créer la vue ne configure pas tout. Logique conditionnelle Business/Enterprise selon l’aide. Ne pas ouvrir au public par défaut.
- **Test d’acceptation et repli** — Soumettre une entrée valide puis un champ manquant; relire les propriétés et vérifier qui voit les réponses.
- **Source** — [Documentation Notion](https://www.notion.com/help/forms).

## N17

**Bouton de base**

- **Quand l’utiliser** — Modifier la ligne cliquée ou créer un objet lié sans quitter la file.
- **Variantes et paramètres** — Propriété bouton; sélectionner ligne courante ou cible explicite, action, valeurs et confirmation.
- **Limite et mauvais usage** — Une action mal ciblée peut toucher d’autres fiches; certains gestes sont soumis au forfait et aux permissions.
- **Test d’acceptation et repli** — Deux lignes QA, n’en cliquer qu’une, vérifier que l’autre ne change pas. Repli : modifier le statut.
- **Source** — [Documentation Notion](https://www.notion.com/help/database-buttons).

## N20

**Fiche de base**

- **Quand l’utiliser** — Regrouper les propriétés visibles sur les fiches d’une même base.
- **Variantes et paramètres** — Choisir les propriétés épinglées, groupes, panneau de détails; utiliser un modèle distinct pour le contenu par défaut.
- **Limite et mauvais usage** — La disposition affecte toute la base; ne pas modifier une fiche pour prouver la configuration globale.
- **Test d’acceptation et repli** — Comparer une fiche neuve et une fiche historique, sur bureau puis téléphone, et vérifier que le contenu reste intact.
- **Source** — [Documentation Notion](https://www.notion.com/help/layouts).

## N25

**Vue liée**

- **Quand l’utiliser** — Montrer les mêmes objets dans un autre contexte sans copier la base.
- **Variantes et paramètres** — Sur une page : vue liée de source; choisir source, type, filtre, tri et propriétés visibles.
- **Limite et mauvais usage** — La vue n’accorde pas de droits sur la source; un filtre n’est pas une ACL.
- **Test d’acceptation et repli** — Modifier un champ QA depuis la vue et retrouver le même ID dans la source. Repli : lien vers une vue existante.
- **Source** — [Documentation Notion](https://www.notion.com/help/sharing-and-permissions).

## N26

**Filtre et tri**

- **Quand l’utiliser** — Répondre à une question de périmètre, par exemple les échéances ouvertes.
- **Variantes et paramètres** — Choisir types et valeurs exacts, AND/OR, relatif ou absolu, tri de départ et enregistrement pour tous si voulu.
- **Limite et mauvais usage** — Un filtre vide n’est pas une base vide. Attention aux dates absentes, fuseaux et statuts terminaux.
- **Test d’acceptation et repli** — Tester hier/aujourd’hui/demain/sans date et états ouvert/clos. Repli : vue générale et filtre manuel.
- **Source** — [Documentation Notion](https://www.notion.com/help/views-filters-and-sorts).

## N27

**Onglet de vue**

- **Quand l’utiliser** — Alterner entre différentes questions sur une même base; pas entre pages sans rapport.
- **Variantes et paramètres** — Choisir nom explicite, ordre et mode texte/icône selon options; garder le chemin principal facile à atteindre.
- **Limite et mauvais usage** — Le mode icône seule cache le sens; ne pas supposer que tous les onglets restent visibles sur téléphone.
- **Test d’acceptation et repli** — Ouvrir chaque onglet sur bureau et retrouver l’onglet utile sur téléphone. Repli : liens nommés vers les vues.
- **Source** — [Documentation Notion](https://www.notion.com/help/views-filters-and-sorts).

## N28

**Ouverture de fiche et panneaux**

- **Quand l’utiliser** — Consulter le détail sans perdre le contexte; préférer pleine page pour lecture longue.
- **Variantes et paramètres** — Modes côté/centre/pleine page selon type de vue et options. Le panneau de détails N20 est une autre configuration.
- **Limite et mauvais usage** — Ne pas promettre une ouverture latérale sur téléphone. Le réglage dépend de la vue et ne change pas le schéma.
- **Test d’acceptation et repli** — Ouvrir, modifier une fiche QA, revenir et retrouver la file. Repli : pleine page + lien retour.
- **Source** — [Documentation Notion](https://www.notion.com/help/views-filters-and-sorts).
