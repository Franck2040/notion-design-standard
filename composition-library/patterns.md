# 10 compositions fonctionnelles — fiches de conception

> Croquis **originaux** et réutilisables comme inspiration. Ils ne constituent pas une mise en œuvre validée. Chaque fiche explicite objets, interaction, sources, mobile et risques. Adaptez l'ordre et l'esthétique au brief ; ne pas garder le même squelette par habitude.

Voir les [dix planches illustrées et exemples Notion](visual-cards.md) pour les proportions, les blocs natifs et les références externes.

## 01 — Cockpit focalisé

**Problème** : connaître immédiatement la prochaine action sans parcourir des bases entières. **Utilisateurs** : travail individuel, vie quotidienne, petite équipe.

```text
[ Capture rapide  ]     [ Prochaine échéance  ] [ État du jour ]
[ Priorités ouvertes (liste courte, filtrée et triée)         ]
[ Projet actif : 1 à 3 fiches ]     [ À traiter / En attente   ]
[ Domaines / archives : navigation secondaire                 ]
```

- **Sources** : Tâches, Projets, Inbox ; une seule entrée par objet.
- **Interaction** : formulaire de tâche ou capture, puis changement de statut dans la vue centrale.
- **Mobile** : capture → tâches ouvertes → échéance → projet actif → navigation.
- **État vide** : texte « Aucune action planifiée » et accès de création, pas une métrique 0 présentée comme réussite.
- **Risques** : dates vides, retards exclus des filtres, liste infinie ; ne pas confondre « aujourd'hui » avec tout le backlog.
- **Test** : trois tâches aux dates différentes et états différents visibles dans les vues attendues.

## 02 — Studio d'œuvres

**Problème** : retrouver une création et ses variantes, sans transformer le studio en table administrative.

```text
[ Œuvre active (titre, étape, extrait/couverture possédée) ]
[ Reprendre l'écriture ] [ Capturer inspiration ]
[ Galerie de créations liées à la base d'œuvres           ]
[ Inspirations (liste courte) ] [ Séances / prochaines actions ]
```

- **Sources** : Œuvres, Inspirations, Actions ; relations croisées ; versions dans la fiche originale.
- **Interaction** : capture d'idée dans Inbox spécialisée ou liée ; ouverture fiche en peek si disponible.
- **Mobile** : œuvre active + capture ; galerie réduite ; informations de production ensuite.
- **État vide** : exemple fictif explicitement marqué, ou explication du premier ajout.
- **Risques** : images sous licence, mots de chansons protégés, bases séparées non reliées, onglets de production cachés.
- **Test** : créer une inspiration, l'associer à l'œuvre, la retrouver sur les deux vues.

## 03 — Centre documentaire

**Problème** : répondre à une question avec une source traçable et un statut de validité.

```text
[ Recherche et filtres de type, domaine, statut ]
[ Procédures vérifiées / récemment utilisées ] [ À examiner ]
[ Base de connaissances filtrée (liste)                     ]
[ Source originale + date de revue dans chaque fiche        ]
```

- **Sources** : Connaissances, Captures, Sources ; l'original reste accessible.
- **Interaction** : ajout d'une note, classement, revue, archivage réversible.
- **Mobile** : recherche/filtres → procédures → sources ; éviter tables de 15 propriétés.
- **Risques** : confondre « indexé » avec « vérifié », dupliquer un document, masquer les versions.
- **Test** : rechercher par catégorie, statut et source ; rouvrir le document original.

## 04 — Console de projets

**Problème** : progresser sur plusieurs livrables en identifiant blocages et échéances.

```text
[ Projets en cours (3-5) ] [ Bloquants à débloquer ]
[ Mes actions prochaines / échéances ]
[ Board par phase ou statut ] [ Chronologie si dates utiles ]
[ Documentation du projet et archives ]
```

- **Sources** : Projets, Actions ; relations bidirectionnelles (pas de copie).
- **Interaction** : ajout projet → fiche résultat attendu → actions liées.
- **Mobile** : liste des blocages et tâches avant board.
- **Risques** : board vide, projet de test compté actif, indicateurs sans formule correcte.
- **Test** : changer statut d'une action depuis la vue liée et vérifier dans la base unique.

## 05 — Calendrier éditorial

**Problème** : passer d'une idée à une publication sans oublier les contenus en retard.

```text
[ Créer idée / nouveau contenu ] [ À publier ensuite ]
[ Calendrier de programmation ] [ En retard / à valider ]
[ Campagnes ] [ Bibliothèque média et ressources de marque ]
[ Statistiques réelles si les données existent ]
```

- **Sources** : Contenus, Campagnes, Canaux, Ressources.
- **Interaction** : formulaire titre + canal + état + date, sans forcer une idée à posséder une date.
- **Mobile** : prochaines publications en liste avant calendrier mensuel.
- **Risques** : chiffres inventés, mauvais fuseaux, cartes de performance sans données.
- **Test** : publication à venir, publiée, sans date, en retard ; vérifier leur tri.

## 06 — Journal et routines

**Problème** : capturer une expérience quotidienne et garder un historique consultable.

```text
[ Nouvelle entrée ] [ Habitudes du jour (courtes) ]
[ Journal récent / note à reprendre ]
[ Calendrier ou vue mensuelle ] [ Archives datées ]
```

- **Sources** : Journal, Habitudes, Entrées d'habitudes.
- **Interaction** : nouvelle entrée horodatée, validation facultative d'une routine.
- **Mobile** : capture très haute, saisie sans cinq écrans de propriétés.
- **Risques** : mettre des notes privées dans une page publique, scores ou streaks culpabilisants, confusion entre données et sensation.
- **Test** : saisir et retrouver par date ; vérifier permissions et absence de publication implicite.

## 07 — Hub d'apprentissage

**Problème** : retrouver le prochain cours, la révision et le travail à rendre.

```text
[ Prochain travail à rendre ] [ Révision suivante ]
[ Cours actifs : liste / galerie modeste ]
[ Notes classées par matière ] [ Exercices et ressources ]
[ Archives des semestres ]
```

- **Sources** : Cours, Notes, Tâches, Séances et ressources.
- **Interaction** : capture note contextualisée, création exercice/tâche.
- **Mobile** : échéance → cours actif → nouvelle note.
- **Risques** : surcharge de calendrier, confusion date de cours/date limite, chapitres archivés inaccessibles.
- **Test** : retrouver une ancienne note et un devoir à échéance proche.

## 08 — CRM de suivi

**Problème** : ne rater aucune relance et préserver l'historique des interactions.

```text
[ Prochaines relances ] [ Ajouter interaction ]
[ Opportunités actives par phase ] [ Contacts à rappeler ]
[ Historique horodaté / documents associés ]
```

- **Sources** : Contacts, Opportunités, Interactions, Tâches.
- **Interaction** : enregistrer échange ; planifier relance ; mettre à jour même fiche.
- **Mobile** : relances et formulaire rapide, pas table multi-colonnes.
- **Risques** : exposition de données privées, statuts obsolètes, doublons de personnes.
- **Test** : une interaction reliée au bon contact et à la bonne opportunité.

## 09 — Espace communautaire

**Problème** : coordonner réunions, événements et bénévoles avec peu de formation.

```text
[ Prochain événement ] [ Nouvelle activité ]
[ Affectations ouvertes et dates ] [ Calendrier compact ]
[ Ressources / procédure d'accueil ]
```

- **Sources** : Événements, Personnes autorisées, Actions, Documents.
- **Interaction** : formulaire d'événement, attribution à une personne.
- **Mobile** : événement imminent → tâches → documentation.
- **Risques** : permissions incorrectes, confusion public/privé, synchronisation externe supposée.
- **Test** : une personne autorisée peut voir ses tâches et pas les notes réservées.

## 10 — Portail de lecture

**Problème** : consulter, sélectionner et annoter un corpus sans le noyer dans des tâches.

```text
[ Reprendre la lecture / rechercher ] [ Nouvelle source ]
[ Collections par thème ] [ Sources récentes ]
[ Notes et citations avec provenance ]
```

- **Sources** : Documents, Notes, Thèmes et Sources ; les documents d'origine sont conservés.
- **Interaction** : sauvegarder une source, annoter, classer.
- **Mobile** : recherche puis lecture, liste compacte plutôt que longues tables.
- **Risques** : licences, confusion entre texte original et résumé, doublons de fichiers.
- **Test** : ouvrir source, retrouver annotation, lire les versions.

## Stress tests transversaux

Pour **chaque** composition : 0 données / 3 données / 300 données ; 360 px mobile / desktop ; thème clair/sombre ; permissions lecture seule ; titre long ; donnée sans date ; lien cassé ; état « non vérifié ». Observer les effets réels. **Aucun de ces tests n'est déclaré exécuté par ce fichier.**
