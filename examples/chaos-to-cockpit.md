# Cas complet — transformer un espace Notion fragmenté en cockpit

> Démonstration fictive, construite pour enseigner **le diagnostic, la conception, la migration et la vérification**. Tous les noms de lignes et chiffres sont des exemples, pas des données utilisateur.

## Phase 0 — Point de départ

Une personne polyvalente travaille sur ses études, ses candidatures, des chansons et des applications futures. Son espace contient :
- page « Mon organisation » avec 18 sous-pages ;
- page « Notes » longue de plusieurs centaines de blocs ;
- « Études » avec des cases à cocher à la main ;
- base « Tâches » déjà existante ;
- « Projets » avec une partie des projets ;
- CRM de candidatures complet, mais isolé ;
- plusieurs pages d'accueil plus ou moins redondantes.

**Plainte** : « C'est moche, je cherche longtemps et je dois scroller pour voir une information. »

Une IA superficielle crée six jolies cartes qui pointent vers les pages d'origine. Le problème n'est donc pas résolu.

## Phase 1 — Enquêter et préserver

| Élément | Question à résoudre | Résultat |
|---|---|---|
| Tâches | Existe-t-il une base centrale ? | Oui ; la réutiliser |
| Notes | Toutes les notes sont-elles du même type ? | Non ; ne pas déplacer en bloc |
| CRM | Y a-t-il des statuts et dates ? | Oui ; créer des vues liées |
| Projets | Quels ont des prochaines actions ? | Identifier les actifs |
| Inspirations | Où sont les fichiers audio ? | Répertorier et préserver |
| Accueils | Ont-ils du contenu unique ? | Vérifier avant archiver |
| Assets | Sont-ils redistribuables ? | Pas nécessairement |

**Avant migration** : relever les URL et structures, sauvegarder selon les capacités disponibles. Tout élément non examiné reste en place.

## Phase 2 — Définir cinq parcours

1. « Il me faut cinq secondes pour capturer une idée. »
2. « Au réveil, je vois ce qui réclame mon attention. »
3. « Je reprends une préparation de certification au point exact où je l'avais laissée. »
4. « Je retrouve une phrase personnelle écrite il y a trois ans, par thème. »
5. « Je peux enregistrer une mélodie sans avoir encore de chanson. »

Ces cinq cas servent de tests, pas d'arguments marketing.

## Phase 3 — Décider les bases

```text
Areas
 ├── Projects ─── Tasks
 └── Knowledge (sources, notes)
Inbox ──────────► task / project / knowledge / archive
Music ideas ────► Works (relation optionnelle)
Practice logs ─► Area: Music
CRM = base métier conservée ; vues « relances » et « entretiens » liées au cockpit
```

On ne crée pas une deuxième base Tasks simplement parce qu'un nouveau template est plus beau. On peut créer un **système expérimental séparé**, puis migrer si des incompatibilités techniques l'exigent, avec validation des données.

## Phase 4 — Designer la première minute

```text
 ┌───────────────┬────────────────────────────────────────────┐
 │ Accueil       │ Prochaine action : finaliser lab réseau   │
 │ Aujourd'hui   │ Échéance : devoir mercredi              │
 │ Projets       │ [Capturer]     [Reprendre un projet]       │
 │ Connaissances ├────────────────────────────────────────────┤
 │ Studio        │ [À faire] [Cette semaine] [En attente]     │
 │ Archives      │ 3 tâches essentielles (vues liées)        │
 └───────────────┴────────────────────────────────────────────┘
```

Les chiffres « 3 tâches » sont fictifs pour montrer la densité. Ne pas fabriquer ce chiffre à partir de données manquantes.

**Pourquoi cette organisation ?** Le regard passe d'abord à l'action et au délai, puis aux outils ; la navigation reste latérale. L'utilisateur n'a pas besoin de trois scrolls avant de voir la prochaine action.

## Phase 5 — Rendre la capture réelle

**Prototype A — échec**
- bloc « + Nouvelle idée » contenant un lien vers une page Notes ;
- l'utilisateur doit encore trouver l'endroit exact et décider sa catégorie.

**Prototype B — amélioration**
- bouton natif créant un item dans Inbox, si supporté par le workspace ;
- champs : titre/texte, capture date, média éventuel ; aucune obligation de choisir un projet.
- vue « À revoir » intégrée dans le centre de travail.

**Recette** : créer une idée « refrain entendu dans le train », joindre un petit mémo audio, la retrouver trois jours après et la relier à une nouvelle chanson sans déplacer ni copier le fichier.

## Phase 6 — Mettre en place des pages spécialisées

- **Études** : cours en cours, devoirs/échéances, préparation certification, ressources liées.
- **Carrière** : relances, entretiens, projets professionnels, documents utiles.
- **Studio** : inspirations, chansons en cours, versions audio et couvertures, journal d'entraînement.
- **Connaissances** : Inbox, lectures, thèmes, pensées, notes reliées.
- **Finances** : dépenses et objectifs sans afficher tous les mouvements à l'accueil.

Les détails restent dans les espaces spécialisés. Sur l'accueil, seuls les flux importants ou les tâches reliées ressortent.

## Phase 7 — Design visuel

Direction retenue pour le cas :
- fond clair ;
- palette vert sauge / beige / gris ;
- familles d'icônes natives homogènes ;
- navigation courte ;
- cartes compactes ;
- une horloge agréable et une météo discrète, sous réserve des contraintes de widget.
- faible usage de dégradés, couvertures seulement quand elles servent l'identité ou la mémoire visuelle.

La beauté ne remplace pas la fonction : si les widgets repoussent les tâches hors du premier écran, réduire les widgets.

## Phase 8 — Migration graduelle

```text
Ancien CRM   → intact ; nouvelle vue liée sur page Carrière
Ancienne base Tasks → intacte ; vues Today / Week / Project
Notes libres → inventaire ; sélection de notes révisées → Knowledge
Chansons     → nouvelles fiches liées, originales conservées
Ancien Life OS → conservé en Archive d'interface, pas supprimé
```

Après chaque sous-ensemble : comparer nombre d'items, URL, propriétés clés, pièces jointes et relations ; noter les anomalies. Éviter les déplacements massifs tant qu'un seul type de contenu n'a pas été testé.

## Phase 9 — Test contradictoire

1. Sur bureau, la prochaine action est-elle visible sans scroll ?
2. Une tâche modifiée apparaît-elle partout correctement ?
3. L'Inbox est-elle utilisable sur téléphone ?
4. Une inspiration musicale non classée est-elle récupérable ?
5. Le dernier projet archivé reste-t-il recherchable ?
6. Le document d'aide explique-t-il les dépendances et la langue ?
7. Un autre agent peut-il identifier les sources des bases sans ouvrir 30 pages ?

**Exemple de résultat** : tests 1–4 réussis, test 5 échoué parce que les archives manquent d'index. **Statut : non terminé.** Ajouter une recherche par sujet et date, puis retester.

## Phase 10 — Transmission

Livrer trois objets distincts :
1. **le workspace** (fiches et données réellement utilisées) ;
2. **le standard public** (ce dépôt, sans informations privées) ;
3. **les décisions de migration privées** (liens, inventaire, état des changements et procédures de retour arrière).

L'autre IA n'a ainsi ni besoin de deviner ce qui a été décidé, ni de transformer cette méthode en une liste rigide de bonnes pratiques.
