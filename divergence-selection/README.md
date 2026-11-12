# Étape 05 — Diverger, sélectionner, prototyper et réviser

**Statut : protocole de design, non résultat d'un test effectué.** La première composition proposée par une IA n'est pas la réponse finale par défaut. Ce processus est inspiré du cadre [Understand → Define → Sketch → Decide → Prototype → Validate de Google](https://designsprintkit.withgoogle.com/methodology), en conservant les contraintes et la réversibilité propres à Notion.

## Entrée

Lire la [fiche de recherche](../research-playbook/research-brief-template.md) : cinq actions, objets, données, contexte, preuves et inconnues. Si elle manque, ne pas inventer des entretiens. Préparer un brief provisoire avec hypothèses clairement identifiées.

## 0. Niveau d'effort adapté

| Changement | Nombre de directions | Prototype | Validation |
| --- | --- | --- | --- |
| Correction de libellé ou d'icône | Pas de divergence formelle | Modification ciblée | Lecture puis interaction si nécessaire |
| Amélioration d'un parcours existant | Deux parcours si choix réel | Zone modifiée réversible | Test du flux et des voisins |
| Nouvelle page spécialisée | Trois structures distinctes | Prototype ou page d'essai native | Tests desktop/mobile + données |
| Refonte d'un système multi-pages | Trois directions d'architecture/UX | Prototype par étapes, sans détruire les bases | Tests critiques, conservation et permissions |
| Système très sensible (données personnelles) | Exploration encadrée | Données factices, permission minimale | Revue avant toute publication |

**Ne pas ritualiser la divergence** pour déplacer un bouton de deux lignes : l'effort doit rester proportionnel.

## 1. Divergence en deux passes

### Passe A — Priorité et architecture

Formuler **trois hypothèses substantiellement différentes** en changeant au moins deux variables :

- Unité d'attention : tâche, source, œuvre, projet, événement, exception, métrique…
- Interaction principale : capture, recherche, consultation, revue, planification, décision…
- Hiérarchie du premier écran : action d'abord, objet vedette d'abord, tableau de bord d'abord…
- Densité : compact, mixte, éditorial.
- Mode dominant : liste, galerie, calendrier, board, documentation.
- Navigation : page unique, domaines, navigation synchronisée, profondeur progressive.
- Risque et maintenance : nombre de sources et effort de mise à jour.

Une permutation de couleurs **n'est pas** une troisième hypothèse. Une solution « dashboard avec six cartes » répétée trois fois échoue au critère de diversité.

### Passe B — Direction artistique

Pour chaque structure : une proposition de caractère visuel **compatible avec Notion natif**, famille d'icônes, usage de couleur, couvertures éventuelles, rythme, densité, état vide et comportement mobile. Distinguer ce qui sera approximatif (typographies, hex exacts, CSS non natif) de ce qui est configurable.

**Condition** : ne pas installer un style au hasard avant d'avoir choisi une structure fonctionnelle.

## 2. Fiche candidate (x3)

Chaque hypothèse produit **le même niveau de détail** :

```yaml
concept:
  id: A
  nom: "..."
  job_prioritaire: "..."
  premier_ecran: ["...", "...", "..."]
  action_primaire: "..."
  architecture: ["source existante -> vue liée", "..."]
  pattern: "composition-library/..."
  composants: ["N08", "N10", "N16"]
  caractere_visuel: "..."
  icones_natives: "..."
  mobile: ["ordre 1", "ordre 2", "ordre 3"]
  etat_vide: "..."
  cout_maintenance: "faible | moyen | élevé"
  limites_notion: ["..."]
  hypotheses_risquees: ["..."]
  tests_necessaires: ["..."]
  preuves: ["..."]
```

## 3. Revue critique contradictoire

L'agent adopte successivement quatre angles — **ce sont des rôles d'analyse, pas de vrais professionnels interviewés** :

1. **Utilisateur pressé** : puis-je agir ou retrouver en moins d'un parcours compliqué ?
2. **Architecte de données** : une seule source, relations préservées, états vides et migration sûre ?
3. **Designer visuel** : hiérarchie claire, composition non générique, contraste, pas d'icônes emoji ?
4. **QA / intégrateur Notion** : le forfait et les outils permettent-ils tout ce qui est dessiné ? Quel test le prouve ?

Documenter pour chaque concept un avantage sérieux, un défaut majeur et le coût pour le corriger. Ne pas feindre un vote d'équipe réelle.

## 4. Filtre éliminatoire AVANT score

**Rejeter ou modifier** une solution qui :
- exigerait la suppression de données réelles, sans plan de conservation ;
- reposerait sur des boutons fictifs, des interactions inaccessibles ou des droits non obtenus ;
- exposerait des informations personnelles à des lecteurs non autorisés ;
- introduirait des visuels/codes tiers sans droit d'utilisation ;
- empêcherait l'action prioritaire dans un contexte essentiel ;
- ferait croire qu'un flux manuel est automatisé ;
- rendrait inaccessible un état critique sans alternative textuelle.

Le choix entre concepts doit porter sur des **solutions faisables**, pas uniquement sur des maquettes séduisantes.

## 5. Sélection pondérée et sensibilité

Barème de départ (à adapter au brief) :

| Critère | Poids |
| --- | ---: |
| Réussite du job principal et visibilité de l'action | 25 |
| Architecture de données / conservation | 20 |
| Faisabilité Notion native / droits / plan | 20 |
| Mobile et accessibilité | 15 |
| Identité visuelle cohérente et mémorable | 10 |
| Coût d'entretien / évolutivité | 10 |

**Noter chaque critère de 0 à 5** avec une justification. Calcul : somme de `poids × note / 5` ; maximum 100. **Il s'agit d'une appréciation de conception, pas d'une mesure utilisateur.** Tester la sensibilité : si l'utilisateur privilégie fortement mobile ou créativité, modifier les poids et noter si le classement des concepts change. Une différence de 2 points ne prouve pas la supériorité d'une proposition.

Après notation, rédiger :
- le concept retenu et l'explication des décisions ;
- les qualités sacrifiées et les conséquences réelles ;
- les hypothèses non confirmées et le test qui pourrait invalider ce choix ;
- le **fallback** si une fonctionnalité Notion n'est pas disponible.

## 6. Prototype progressif

1. Prototyper le premier écran et un seul parcours principal avec **données fictives non sensibles**, dans une page d'essai réversible, ou sur les sources existantes sans duplication lorsque approprié.
2. Vérifier que le composant utilisé est vraiment natif ; garder les outils externes séparés.
3. Tester l'action et lire la fiche sauvegardée. Une simple capture de bloc ne prouve pas une interaction.
4. Vérifier l'ordre des colonnes et la lecture sur téléphone (ou marquer `NON TESTÉ` si navigateur indisponible).
5. Contrôler les vues filtrées, relations et titres longs, éléments manquants et droits lecture seule.
6. Comparer prototype aux objectifs **avant** de dupliquer dans d'autres espaces.
7. Limiter le périmètre des modifications, consigner les actions et le retour arrière.

## 7. Validation et révision

Utiliser des tâches concrètes, pas seulement « est-ce beau ? ». Exemple :
- Ajouter une note, choisir son domaine, la retrouver dans le bon contexte.
- Retrouver une tâche passée / actuelle / future, comprendre pourquoi elle apparaît.
- Ouvrir une source historique, retrouver les versions.
- Naviguer du cockpit à un détail et revenir.
- Retrouver l'action principale sur mobile.

Distinguer :
- `STRUCTURE VÉRIFIÉE` : IDs/propriétés/vues configurées.
- `INTERACTION TESTÉE` : bouton/formulaire réellement actionné et résultat contrôlé.
- `MOBILE TESTÉ` : inspection effective sur petit écran.
- `PERCEPTION ÉVALUÉE` : retour d'un utilisateur réel, identifié comme tel.

Après échec, corriger **la cause de la friction**, pas ajouter seulement une autre carte colorée. Refaire le test et archiver l'observation.

## 8. Livraison

L'agent fournit une [fiche de comparaison](comparison-template.md) et un [rapport de recette](../docs/06-acceptance-tests.md) : hypothèses explorées, choix, limites, modifications réelles, preuves, résultats, régressions, prochaines corrections. « Prototype », « configuré » et « terminé » sont trois états distincts.

Voir aussi les [deux exercices d'application](examples.md).
