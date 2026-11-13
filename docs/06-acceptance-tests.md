# 06 — Assurance qualité : critères concrets de réussite

Un dashboard n'est pas « réussi » parce que son auteur l'apprécie. Il doit passer des **tests d'utilisation, de robustesse et de transmission**.

## A. Checkpoints en cinq étapes

| Phase | Preuve exigée | Échec typique |
|---|---|---|
| Cadrage | Personas, 5 actions prioritaires, 3 problèmes actuels | « Je veux un template premium » sans définition |
| Audit | Inventaire réel des bases, propriétés et pages singulières | Migration basée uniquement sur noms de pages |
| Prototype | Interface testable desktop et mobile | Screenshot figé sans données fonctionnelles |
| Intégration | Vues liées, relations, captures réellement utilisables | Cartes décoratives pointant vers sous-pages |
| Recette | Test de chaque flux + préservation des données | « Terminé » sans vérifier le résultat |

## B. Parcours de recette (avec résultats attendus)

### Test 01 — première visite (30 secondes)

**Situation** : nouvel utilisateur ouvre le dashboard sans explication.  
**Action** : trouver où ajouter une tâche et où voir les prochains rendez-vous.  
**Attendu** : deux accès évidents, sans parcourir le bas de la page.  
**Échec** : il faut ouvrir plusieurs sous-pages ou lire un manuel avant le premier clic.

### Test 02 — capture d'une idée non planifiée

**Action** : écrire « Idée de SaaS : simplifier la veille des candidatures », sans choisir de date ni de projet.  
**Attendu** : enregistrement dans Inbox, date de capture disponible, élément retrouvable en « À traiter ».  
**Échec** : création bloquée tant que 8 propriétés ne sont pas complétées.

### Test 03 — tâche visible dans plusieurs contextes

**Action** : créer une tâche liée à un projet, la programmer puis la marquer terminée.  
**Attendu** : même fiche dans les vues projet/jour, disparition de la vue des tâches ouvertes une fois terminée, historique conservé.  
**Échec** : copies divergentes ou case décorative non reliée.

### Test 04 — idée musicale multimédia

**Action** : déposer une idée de mélodie avec un fichier audio et quelques mots.  
**Attendu** : la capturer sans créer immédiatement une chanson, puis la retrouver par date/type.  
**Échec** : fichier introuvable, lien cassé, classement forcé dans une rubrique trop spécifique.

### Test 05 — connaissance sur plusieurs années

**Action** : retrouver une réflexion datant de plusieurs années dont seul le thème est connu.  
**Attendu** : recherche ou filtre par thème/source, provenance conservée ; anciens contenus toujours accessibles.  
**Échec** : pensée supprimée car jugée « ancienne », ou archive sans métadonnées.

### Test 06 — projet actif et état réel

**Action** : ouvrir un projet et modifier une tâche liée.  
**Attendu** : statut cohérent dans le projet et le cockpit ; pas de saut répétitif entre pages.  
**Échec** : projet = simple lien vers des notes, aucun suivi des actions.

### Test 07 — statut et automation

**Action** : marquer une tâche récurrente terminée, vérifier création suivante, puis annuler sur la tâche d'essai.  
**Attendu** : comportement documenté et **une seule** nouvelle occurrence lorsque prévu.  
**Échec** : statut renommé casse la formule, ou double clic produit deux occurrences sans avertissement.

### Test 08 — mobile

**Action** : depuis un téléphone, capturer une idée, retrouver l'action du jour et modifier son statut.  
**Attendu** : premier écran lisible, pas de colonnes inutilisables, boutons touchables, pas de scrolling horizontal imprévu.  
**Échec** : sidebar desktop s'affiche en première colonne sur trois écrans de haut.

### Test 09 — lecture et esthétique

**Action** : ouvrir la page lors d'une journée chargée ; observer les titres, les couleurs et les éléments animés.  
**Attendu** : repères lisibles, ambiance agréable, pas de distraction persistante.  
**Échec** : widget animé prend la place de l'action prioritaire ou police trop petite.

### Test 10 — transmission à une autre IA

**Action** : demander à une nouvelle IA d'expliquer un choix d'architecture et de proposer une extension « Studio musical ».  
**Attendu** : elle cite les règles pertinentes, propose données et parcours, distingue hypothèses, montre une maquette, prépare test et migration.  
**Échec** : elle répète « interface propre, moderne, intuitive ».

### Test 11 — duplication commerciale

**Action** : dupliquer le template dans un workspace neuf / gratuit et renseigner trois exemples.  
**Attendu** : relations, vues et fonctionnalités annoncées fonctionnent ou les limites sont signalées. Aucun exemple privé n'est présent.  
**Échec** : boutons cassés, dépendance non déclarée à l'ancien workspace, données personnelles exposées.

## C. Mesurer le scroll

Au lieu d'une affirmation subjective « peu de scroll », documenter :
- appareil, résolution, zoom, densité de données ;
- position du bouton capture ;
- position de la prochaine échéance ;
- position de la première tâche ;
- nombre de pages/vues parcourues pour changer une tâche.

**Cible indicative et ajustable** : les trois premières actions sont sur le premier écran desktop ; si l'interface a beaucoup de contenu, au moins le résumé est visible sans défilement. Ne jamais masquer une erreur de hiérarchie derrière un zoom de 50 %.

## D. Robustesse des données

- [ ] Aucune source originale supprimée.
- [ ] Les identifiants / URL des bases utiles restent accessibles.
- [ ] Les relations et rollups ont été contrôlés sur plusieurs entrées.
- [ ] Les formules réagissent à valeurs vides et non standards.
- [ ] Les vues ne filtrent pas accidentellement des éléments importants.
- [ ] Les archives ont une logique de conservation claire.
- [ ] Les images et pièces jointes conservent leur provenance.
- [ ] Le retour en arrière / restauration a été planifié.

## E. Critères de succès ergonomiques (barème de revue)

Noter chaque dimension de 0 à 4 avec une preuve concrète :
- **Utilité** : tâches et informations pertinentes.
- **Lisibilité** : contraste, hiérarchie et densité.
- **Navigation** : chemin court, repères stables.
- **Opérationnalité** : boutons et vues réellement fonctionnels.
- **Architecture** : sources uniques et relations.
- **Conservation** : aucune perte d'historique.
- **Mobile** : expérience réellement exploitable.
- **Maintenance** : guides et dépendances.
- **Beauté** : cohérence, ambiance, plaisir.
- **Évolutivité** : nouveaux domaines sans refonte générale.

Pour chaque note faible, exiger : **symptôme, cause, correctif, nouveau test**. La moyenne globale ne doit pas masquer un défaut critique : perte de données ou fonction fictive = blocage de livraison.

## F. Exemple de rapport de recette

```text
Version : Prototype v2
Réalisation : navigation synchronisée + vues Tasks liées
Réussi : création tâche, vue du jour, maintien historique
Échec : capture d'inspiration audio sur mobile (3 écrans)
Écart design : widget météo pousse la liste sous la ligne de flottaison
Correction : réduire widget / déplacer vers la page « Vie »
Données d'origine : conservées
Statut : non validé, action corrective nécessaire
```


## Addendum v1.1 — preuve et communication

Un résultat n'est `PASS` que si l'action annoncée a été observée et son état final vérifié. La présence d'un bouton, d'une vue ou d'une relation n'est qu'une preuve structurelle. Pour chaque test : noter méthode, contexte, objet créé (de test), effet attendu, effet constaté, échec et moyens de retour arrière. Les contrôles d'interface sur desktop/mobile ne peuvent pas être déclarés `PASS` sur la seule base de réponses API.

Ajouter à la recette : zéro emoji de substitution dans l'UI neuve, icônes sémantiques des boutons, cohérence palette sans obligation de bleu, maintien des notes et de leurs versions, des essais non identifiés et des relations. Une fonction bloquée doit être signalée dès découverte et inscrite dans une passation ; ne pas dire « terminé » si un critère P0 n'est pas testé. Voir [08](08-agent-execution-and-visual-direction.md).

## Parcours mobile-first et tests comparatifs

Utiliser les [cinq compositions mobiles](../mobile-first/patterns.md) pour choisir le scénario représentatif. Le [modèle de revue](../maintenance/review-template.md) sépare avant/après, appareil, rôle et preuve. Un contrôle de structure du dépôt ne remplace pas un essai natif.
