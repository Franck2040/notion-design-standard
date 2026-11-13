# Vues et mise en page — source, cartes, fiche et mobile

## R04 — Retrouver le travail dans des vues liées

- **Entrée/sortie.** Une base Tâches, une propriété Date et une propriété Statut. Résoudre les noms et valeurs exacts avant de configurer les filtres.
- **Interface.** Dans la page hôte, taper `/linked` ou chercher « Vue liée de la source de données », sélectionner la source existante, puis ajouter les vues Liste. Configurer les filtres ci-dessous, enregistrer pour tous si le menu le propose, trier par date croissante et n’afficher que titre, état et date utiles.
- **REST / connecteur.** [POST /v1/views](https://developers.notion.com/reference/create-view) avec `data_source_id`, `name`, `type` et un seul placement : `database_id` pour un onglet, `create_database` pour une vue liée dans une page. Ajouter filtres et tris selon le schéma. La création REST exige les capacités insert et update. Connecteur : récupérer IDs avec fetch, puis passer `data_source_id` et exactement un de `database_id` ou `parent_page_id` à l’outil de création de vue. Lire le DSL réel avant d’écrire les filtres. Interroger les fiches avec un filtre ne configure pas une vue.
- **Droits / forfait.** Édition de l’hôte et accès à la source. Valider en lecteur les droits effectifs sur la base. Un filtre n’est pas une autorisation. Pour une variante payante ou un type de vue différent, vérifier le forfait de l’espace.
- **Test / retrait.** Essayer les cas ci-dessous. Vérifier la date locale autour du changement de jour si c’est important, et que la même fiche garde son ID dans plusieurs vues. Effacer uniquement la vue ou rétablir sa configuration, pas les fiches ni la source.
- **Repli.** Lien vers une vue enregistrée de la base, avec un nom descriptif. Si les dates relatives ne sont pas disponibles dans le canal, les configurer dans l’interface et tester leur mise à jour sans édition quotidienne.

| Vue | Filtre métier | Cas d’essai |
| --- | --- | --- |
| Aujourd’hui | Date = aujourd’hui ET statut non terminal | Aujourd’hui + ouvert apparaît, aujourd’hui + terminé n’apparaît pas |
| En retard | Date renseignée, avant aujourd’hui ET statut non terminal | Hier + ouvert apparaît, sans date ne remonte pas |
| Prochaines échéances | Date après aujourd’hui ET statut non terminal | Demain apparaît, aujourd’hui ne remonte pas |
| En attente | Statut = valeur d’attente du système | Une fiche sans date mais en attente apparaît ici |

Exemple de corps JSON pour créer un onglet « En attente » via REST, avec une vraie propriété de type `status`. Remplacer les IDs, le nom et la valeur par ceux du schéma lu. Cet exemple n’envoie aucune requête et n’a pas été exécuté sur un compte.

```json
{
  "database_id": "ID_BASE",
  "data_source_id": "ID_SOURCE",
  "name": "En attente",
  "type": "list",
  "filter": { "property": "Statut", "status": { "equals": "En attente" } },
  "sorts": [{ "property": "Échéance", "direction": "ascending" }]
}
```

Avec le connecteur, sur ce même schéma et après lecture de la spec, la configuration équivalente se décrit par `FILTER "Statut" = "En attente"; SORT BY "Échéance" ASC`. Si la propriété est de type Sélection, utiliser l’opérateur du type réel en REST. Relire l’onglet créé, pas seulement les lignes retournées.

Une fiche en attente peut aussi être en retard : c’est voulu si les vues répondent à deux questions distinctes. Si l’utilisateur veut des listes exclusives, modifier la règle et les cas d’essai.

## R05 — Montrer des œuvres en galerie

- **Entrée/sortie.** La fiche doit rester reconnaissable sans ouvrir la carte. Prévoir un titre, un statut textuel, une couverture facultative et un moyen d’ouvrir la fiche.
- **Interface.** Ajouter une vue Galerie sur Œuvres → Options de vue → Mise en page → Aperçu de la carte : couverture de page ou propriété fichier adaptée → Taille moyenne pour commencer. Afficher titre et statut. Filtrer Production sur les états de travail convenus, et garder une vue Catalogue distincte.
- **REST / connecteur.** Créer ou mettre à jour une vue `gallery` avec la configuration de galerie documentée par le canal. Le connecteur peut exposer `CARD SIZE`, `SHOW` et `COVER` pour une propriété. Ne pas présumer qu’un réglage de recadrage ou le choix « couverture de page » est exposé.
- **Droits / forfait.** Édition de la vue, lecture de la source et des fichiers, droits sur les visuels et respect des limites de téléversement du forfait si des médias sont ajoutés.
- **Test / retrait.** Trois cartes : couverture paysage, portrait et aucune couverture. Tester clair/sombre, téléphone, un titre long et la sélection de la bonne œuvre. Restaurer les réglages précédents ou retirer seulement la vue QA.
- **Repli.** Liste avec titre et état si les couvertures ne distinguent pas les œuvres. Voir la [planche Studio](../visual-atlas/README.md#02--le-studio-des-œuvres).

## R06 — Préparer une fiche et choisir son ouverture

- **Entrée/sortie.** Séparer le **modèle de contenu** (blocs préremplis), la **mise en page de fiche** (réglage transversal) et le **mode d’ouverture** (option d’une vue). Modifier seulement la couche nécessaire.
- **Interface.** Flèche à côté de `Nouveau` → nouveau modèle → sections utiles. Pour organiser les propriétés, ouvrir la base en pleine page et choisir Apparence et disposition → Personnaliser la disposition. Prévisualiser plusieurs fiches : la disposition touche toute la base. Dans les options de la vue, choisir l’ouverture latérale si elle aide à conserver le contexte, puis vérifier.
- **REST / connecteur.** [Lister les modèles](https://developers.notion.com/reference/list-data-source-templates), puis [créer une page](https://developers.notion.com/reference/post-page) avec un modèle existant. L’application est asynchrone : relire le contenu avant de poursuivre et ne pas répéter la création si l’ID existe. Le connecteur peut exposer `template_id`. Ne pas déduire de ces capacités que l’éditeur de disposition ou son panneau sont automatisables.
- **Droits / forfait.** Édition de la base pour modèles et disposition. Vérifier l’accès du créateur et l’ouverture pour les lecteurs. Tester sur bureau/web où l’éditeur de disposition complet est documenté. Vérifier les options disponibles dans l’espace.
- **Test / retrait.** Créer une fiche via le modèle, vérifier les sections et l’ouverture. Ouvrir aussi une fiche historique et vérifier que son contenu est intact. Restaurer le mode d’ouverture, le modèle par défaut ou la disposition d’origine selon la couche touchée.
- **Repli.** Fiche pleine page avec lien de retour et sections préremplies, sans promettre de panneau.

## R07 — Construire une page lisible sur téléphone

- **Entrée/sortie.** Action et état essentiels lisibles sans dépendre d’une grille horizontale. Distinguer l’ordre visuel sur bureau et l’ordre de lecture sur téléphone.
- **Interface.** Placer l’action principale et le résumé hors colonnes, puis les blocs de travail dans l’ordre utile. Sur bureau, déplacer les blocs par leur poignée pour créer des colonnes. Utiliser une liste compacte et des mentions/liens de retour pour le mobile. Vérifier le résultat réellement affiché : les [colonnes ne sont pas disponibles sur téléphone](https://www.notion.com/help/columns-headings-and-dividers).
- **REST / connecteur.** Les [blocs](https://developers.notion.com/reference/block) documentés peuvent être utilisés si l’outil les prend en charge. Pour les colonnes, vérifier le schéma `column_list` et ses enfants. Pour le connecteur, lire sa spec Markdown et ne pas supposer qu’un collage Markdown reproduit la disposition. Aucun retour JSON ne prouve le rendu mobile.
- **Droits / forfait.** Édition de la page hôte, lecture des vues et des pages liées. Pas de widget ou forfait supplémentaire requis pour la variante en blocs simples. Ne pas garantir une largeur CSS personnalisée.
- **Test / retrait.** Sur téléphone ou dans un émulateur explicitement nommé, vérifier titre long, absence de défilement horizontal dans le parcours, action et retour accessibles. Distinguer `TESTÉ SUR APPAREIL` et `ÉMULÉ`. En cas de régression, remettre les blocs dans l’ordre initial sans les dupliquer.
- **Repli.** Une seule colonne native, avec priorité aux actions et un lien vers la vue dense sur bureau.
