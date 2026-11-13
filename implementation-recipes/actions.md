# Actions — capture, changement d’état et formulaire

## R01 — Capturer une note dans la source existante

- **Entrée/sortie.** Depuis un cockpit, créer une fiche dans Inbox, avec un titre éditable, `Type` et `Domaine` selon le schéma existant, et le contenu dans l’emplacement déjà utilisé (propriété ou corps de fiche). Décider quels champs doivent être préremplis et lesquels sont à saisir.
- **Interface.** Sur la page hôte, saisir `/button` → nom « Nouvelle note » → choisir l’icône d’ajout dans le sélecteur si elle est disponible. Ajouter l’action **Ajouter une page à** et pointer vers la vraie Inbox, avec les valeurs par défaut compatibles. Ajouter **Ouvrir une page ou une URL** avec la page créée si elle est sélectionnable comme résultat de l’action précédente. Enregistrer. Ne pas créer une seconde Inbox.
- **REST / connecteur.** [Créer une page](https://developers.notion.com/reference/post-page) dans la source ou utiliser l’outil de création de pages pour créer une fiche directement. Cela ne crée pas le bouton et ne prouve pas la chaîne d’actions. Configurer le bouton dans Notion si aucun outil chargé ne sait l’écrire.
- **Droits / forfait.** Vérifier édition de la page hôte et accès d’écriture à la source pour le rôle final. Les boutons sont disponibles sur tous les forfaits, mais certaines actions dépendent du forfait. Inspecter chaque action dans le compte. [Documentation](https://www.notion.com/help/buttons).
- **Test / retrait.** Cliquer une fois, noter l’ID de la fiche créée et vérifier qu’elle s’ouvre, puis renseigner des valeurs QA, fermer et rouvrir. Retrouver le même ID dans la vue filtrée. Tester l’accès utilisateur et le téléphone. Retirer le bouton ou la fiche QA, pas la source.
- **Repli.** Lien « Ajouter une note » vers une vue existante avec `Nouveau`, ou [R03](#r03--recueillir-une-entrée-structurée-avec-un-formulaire) si le parcours doit imposer des champs. Ne pas appeler « bouton configuré » un simple lien.

## R02 — Modifier seulement la fiche cliquée

- **Entrée/sortie.** Dans une file, passer la ligne cliquée de « À relire » à « Validé », sans changer les voisines.
- **Interface.** Dans les propriétés de la base → nouvelle propriété **Bouton** → « Valider ». Modifier l’automatisation → **Modifier une propriété** de cette page → choisir le statut cible. Vérifier les variables et retirer tout filtre ou action qui modifierait d’autres fiches. Pour une action sensible, utiliser la confirmation native si disponible.
- **REST / connecteur.** [Mettre à jour une page](https://developers.notion.com/reference/patch-page) ou outil d’édition de page peut changer un statut si l’ID est connu. Ce n’est pas une propriété bouton installée. Ne pas inventer un payload `button` qui configure l’action.
- **Droits / forfait.** Notion documente `Accès complet` ou `Peut modifier` pour configurer. `Peut modifier le contenu` permet aussi de cliquer. Vérifier l’accès à toutes les cibles de la chaîne, et les actions payantes dans le menu du compte. [Documentation](https://www.notion.com/help/database-buttons).
- **Test / retrait.** Créer deux fiches QA de même état. Cliquer la première, vérifier son statut, l’ID et l’état inchangé de la seconde. Recliquer pour vérifier qu’aucune notification ou création répétée n’est déclenchée. Restaurer les valeurs QA. Ne retirer la propriété que si elle a été créée pour ce test et n’est utilisée par personne.
- **Repli.** Laisser la propriété Statut directement modifiable. Ne pas simuler une validation avec un callout.

## R03 — Recueillir une entrée structurée avec un formulaire

- **Entrée/sortie.** Collecter une seule ligne dans une base existante. Exemple : titre, URL ou provenance, et type pour une bibliothèque de sources.
- **Interface.** Sur la base → ajouter une vue **Formulaire**. Relier les questions aux propriétés existantes, vérifier les types, libellés et champs obligatoires. Aperçu → vérifier l’expérience, puis définir qui peut répondre dans le partage. Si le champ principal reste « Title » et n’est pas renommable dans l’éditeur employé, noter la limite et ne pas déclarer l’interface entièrement traduite.
- **REST / connecteur.** Le type `form` figure dans l’[objet View](https://developers.notion.com/reference/view). Ne déclarer automatisés que les réglages explicitement documentés et exposés par le canal choisi. Dans le connecteur Notion, inspecter les capacités de l’outil de création/mise à jour de vue et sa spec `notion://docs/view-dsl-spec`. Compléter les libellés, questions, partage et options manquants dans l’interface. Un POST de page ne teste pas une soumission humaine.
- **Droits / forfait.** Contrôler droits d’édition de la base, rôle répondant et lecture des réponses séparément. La logique conditionnelle est réservée à Business et Enterprise selon l’[aide officielle](https://www.notion.com/help/forms). Ne pas activer un lien public sans besoin et autorisation.
- **Test / retrait.** Soumettre depuis le lien avec le bon rôle, y compris un champ obligatoire vide et un cas valide. Relire l’ID, le titre et chaque valeur dans la source. Contrôler qu’un répondant ne peut pas consulter les réponses privées. Fermer le formulaire de test et retirer uniquement les entrées QA identifiées.
- **Repli.** Formulaire linéaire avec questions facultatives, ou fiche guidée si le répondant a déjà accès à la base. Ne pas remplacer l’accès de l’utilisateur par le seul accès de l’intégration.
