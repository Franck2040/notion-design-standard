# 05 — Implémentation Notion : fiches pratiques et limites

> Ces techniques sont documentées à la date de rédaction. Vérifier l'aide officielle, les permissions, le forfait et l'interface actuelle lors de chaque nouveau projet.

## 1. Construire un dashboard qui travaille

**Étapes de conception — pas encore de clics :**
1. lister les 5 actions quotidiennes les plus fréquentes ;
2. identifier la base qui détient chaque donnée ;
3. choisir la vue par type de question ;
4. décider quelles vues seront visibles sur l'accueil ;
5. dessiner la mise en page desktop et mobile ;
6. créer les vues liées et vérifier sur des vraies données ;
7. réduire les propriétés visibles aux informations décisionnelles.

**Exemple** : « Que dois-je faire aujourd'hui ? »
- champs nécessaires : Name, Status, Scheduled, Due, Priority ;
- filtre : Status non terminé et (Scheduled aujourd'hui ou Due en retard selon la définition retenue) ;
- tri : priorité, puis échéance ;
- rendu : liste compacte plutôt que table de 14 colonnes ;
- limite : afficher un long backlog non filtré ne répond pas à cette question.

## 2. Sources vs vues liées

On conserve la base complète dans le backend ou dans son domaine. L'accueil utilise une **vue liée**. Modifier le statut depuis la vue liée modifie la fiche originale.

### Piège classique

Une page « Focus » créée avec des cases à cocher indépendantes de la base centrale. Une tâche cochée dans Focus reste ouverte dans la base source. **Ne pas faire cela** sauf si la checklist est volontairement un rituel distinct.

## 3. Relations, rollups et formules

Les relations permettent d'afficher les tâches d'un projet. Les agrégations peuvent montrer le nombre de tâches ouvertes ou une progression. Attention :
- un projet sans tâches ne doit pas afficher un pourcentage de complétion trompeur ;
- ne pas calculer une progression uniquement sur la quantité de tâches si leurs tailles diffèrent considérablement ;
- toutes les formules et propriétés utilisées doivent être documentées.

**Exemple conceptuel**
```
Projects: [Name, Status, Tasks (relation), Open tasks (rollup/formula)]
Tasks:    [Name, Status, Project (relation), Due]
```
Une fiche projet peut montrer la vue Tasks filtrée sur **ce projet courant** via un modèle de base. Tester le modèle sur au moins deux projets.

## 4. Boutons : distinguer trois réalités

1. **Lien** : conduit vers une page ou une base ; n'ajoute pas une entrée.
2. **Bouton natif Notion** : peut déclencher certaines actions configurées dans Notion, par exemple ajouter une page selon les fonctionnalités disponibles.
3. **Widget externe** : peut afficher des boutons interactifs dans un embed, mais sa capacité d'agir sur Notion dépend d'une intégration autorisée, de l'API et des permissions.

**Exigence** : si le libellé annonce « Nouvelle tâche », tester qu'une entrée est effectivement créée. Sinon, appeler cela « Ouvrir les tâches ».

## 5. Aperçus et panneaux

Les ouvertures Side peek / Center peek peuvent éviter de quitter la page. Ce comportement dépend de la vue et des paramètres d'affichage. La mise en place se fait via les réglages de la vue « Ouvrir les pages dans… » si disponible ; vérifier en usage.

**Ne pas écrire** que Notion autorise n'importe quelle modale en CSS/JavaScript à l'intérieur d'une page native.

## 6. Onglets, toggles, tableaux, galeries

- **Tabs** : remplacer l'empilement de plusieurs vues d'une même base (Today / Upcoming / Inbox / Done).
- **Toggles** : FAQ, maintenance, archives, documentation ; pas pour cacher la seule action essentielle.
- **List** : excellent pour actions courtes.
- **Board** : idéal pour pipeline et statuts, mais horizontalement encombrant sur mobile.
- **Gallery** : excellent pour créations visuelles, fiches média et projets illustrés ; éviter les couvertures inutiles.
- **Calendar** : utile pour une logique temporelle, mais souvent trop grand pour le cockpit.
- **Charts / number** : utiles quand une valeur change une décision ; vérifier les limites de forfait.

## 7. Thème clair / sombre

Notion possède des réglages d'apparence et des raccourcis. Historiquement sur Windows, `Ctrl + Maj + L` bascule l'apparence. **Un bouton Notion natif ne simule pas des touches clavier arbitraires.** Ne pas promettre un bouton « lune » qui modifie le thème global en restant un pur template Notion. On peut afficher l'astuce, créer deux variantes visuelles ou bâtir une application externe distincte.

## 8. Interface FR / EN

- Le **langage des menus Notion** se choisit dans ses préférences.
- Les **textes des pages** ne suivent pas automatiquement ce réglage.
- Proposition réaliste : deux pages de dashboard FR/EN, navigation courte permettant de passer de l'une à l'autre, vues liées aux **mêmes bases**.
- Conserver la langue d'origine des notes, des titres et des noms de propriété pour éviter de casser les formules.
- Établir des traductions contrôlées des libellés et de la documentation ; ne pas prétendre à un traducteur universel.

Alternative : étiquettes bilingues courtes (`Notes / Knowledge`) si deux pages sont trop lourdes à maintenir.

## 9. Horloge et météo

Widgets possibles via embeddings d'outils tiers ; vérifier :
- compatibilité et disponibilité de l'URL d'embed ;
- collecte de données et confidentialité ;
- thème clair, contraste, dimensions ;
- adaptation mobile ;
- absence de publicité ou d'élément intrusif ;
- fonctionnement en cas de blocage du site externe.
Une horloge peut être d'ambiance, c'est un choix UX légitime. Elle ne doit pas devenir la seule information au premier écran.

## 10. Automatisations et événements

Exemples à implémenter seulement si le plan et les permissions le permettent :
- tâche récurrente générée depuis un modèle ;
- date de complétion enregistrée lorsque Status devient Done ;
- nouvel item Inbox à partir d'un bouton ;
- revue hebdomadaire récurrente.

**Tests obligatoires** :
- statut fait puis annulé : pas de duplication inattendue ;
- création depuis mobile ;
- nom de propriété renommé : dépendances identifiées ;
- automatisation inaccessible : comportement alternatif documenté.

## 11. Personnalisation de fiches

La page interne d'une tâche doit afficher en premier : statut, priorité, date, projet, action de planification (si réelle). Les propriétés administratives peuvent être dans une section secondaire. Un modèle de page bien conçu apporte un espace de notes et une checklist, **sans reproduire toutes les colonnes du tableau dans son texte**.

## 12. Dépendances critiques

Documenter dans un fichier de maintenance :
```text
Fonction : Tâches récurrentes
Déclencheur : Status = "Done"
Propriétés : Repeat (Daily/Weekly/Monthly), Due Date
Résultat : nouvelle occurrence ; ancienne conservée
Risque : double déclenchement, statut renommé, plan insuffisant
Test : terminer une tâche d'essai puis vérifier une seule nouvelle ligne
```

Ne pas copier mécaniquement les réglages d'un modèle tiers ; reconstruire des mécanismes adaptés au besoin et à la licence.

## 13. Documentation officielle à reconsulter

- https://www.notion.com/help
- https://www.notion.com/help/keyboard-shortcuts
- https://www.notion.com/help/change-your-language
- https://www.notion.com/templates
- https://developers.notion.com/

Ne jamais considérer un article ou une vidéo de 2024–2026 comme preuve d'une capacité immuable en 2036.
