# 03 — Architecture de l'information et des données

## 1. Distinction centrale : page, base, vue, item

- **Page** : contexte de lecture ou de travail (ex. page « Musique »).
- **Base** : ensemble de fiches de même nature avec des propriétés stables (ex. « Chansons »).
- **Vue liée** : filtre, tri, groupe ou rendu d'une base ; ne crée pas de copie de données.
- **Item/fichier** : occurrence datée, projet, ressource, chanson, tâche.
- **Relation** : lien métier entre occurrences : une tâche appartient à un projet ; une source nourrit une réflexion ; une inspiration contribue à une chanson.

### Anti-pattern

« J'ai une page Tâches personnelles, une page Tâches études, une page Tâches projets. » Si elles sont trois listes indépendantes, une action devient invisible ailleurs.

### Pattern corrigé

Une base `Tasks` avec champs `Task`, `Status`, `Due`, `Priority`, `Area`, `Project`, `Notes` et des vues :
- « Today » : ouvertes avec échéance pertinente ;
- « This week » : ouvertes et prévues ;
- « Project A » : relation Project = A ;
- « Inbox » : non planifiées.
**Attention** : selon le projet, une tâche « à faire aujourd'hui » peut être une tâche planifiée volontairement aujourd'hui, pas uniquement une tâche à échéance aujourd'hui. Prévoir une propriété `Scheduled for` distincte de `Due` si ce besoin est établi.

## 2. PARA adapté : rôle de chaque niveau

**Projects** : effort avec résultat et fin (préparer une certification, sortir un EP, lancer un SaaS).
**Areas** : responsabilité continue (études, langues, carrière, création musicale, sport, finances).
**Resources** : savoir qui sert potentiellement plusieurs domaines (concept réseau, citation sur le leadership, technique vocale).
**Archives** : matériel conservé qui n'est plus actif.

Ce sont des **catégories fonctionnelles**, pas l'obligation de créer exactement quatre dossiers géants.

### Exemple pratique

« Apprendre OSPF » peut être :
- ressource : fiche et schéma OSPF ;
- projet : préparer la certification réseau ;
- tâche : résoudre le TP OSPF ;
- domaine : formation technique.

Il ne faut pas recopier le cours dans chaque lieu. Relier la ressource au projet et la tâche au projet.

## 3. Schéma de données minimal, extensible

```text
AREAS 1 ─────── * PROJECTS
                   │ 1
                   │
                   * TASKS
AREAS 1 ─────── * KNOWLEDGE
PROJECTS * ──── * KNOWLEDGE
INBOX captures → triage → TASK / PROJECT / KNOWLEDGE / ARCHIVE
EVENTS ↔ TASKS or PROJECTS (optional)
```

### Table de base conceptuelle

| Source | Champs utiles | Danger |
|---|---|---|
| Areas | Name, Description, Owner?, Status | Faire du domaine un projet sans fin |
| Projects | Name, Area, Outcome, Status, Start, Target, Next action | 20 statuts incompréhensibles |
| Tasks | Name, Status, Due, Scheduled, Priority, Project, Area, Duration? | Mélanger date limite et date de travail |
| Knowledge | Title, Type, Topic, Area, Project, Source, Captured, Reviewed | Transformer toute phrase en fiche sophistiquée |
| Inbox | Content, Capture date, Media type, Review status, Destination | Poubelle infinie sans rituel de traitement |
| Events | Title, Date-time, Related project, Location? | Copier un calendrier externe sans synchro |
| Finances | Date, Amount, Category, Account, Type, Note | Confondre montants personnels et données publiques |

Une propriété n'est justifiée que si elle est **saisie, filtrée, calculée ou utile à une décision**. Les propriétés décoratives sans usage doivent disparaître des formulaires d'entrée.

## 4. Sous-systèmes spécialisés sans fragmentation

### Musique : inspiration ≠ chanson

```text
Creative Captures
- ID, date, texte/audio/image/lien, idée, mood, statut de traitement
         ↘ optionnel vers
Works / Songs
- titre, état, intention, paroles, démo, fichier audio, pochette,
  version, crédits, date de sortie, sources d'inspiration
         ↘ optionnel vers
Practice Log
- date, exercice vocal, durée, sensation, ressource, observation
```

Conserver les idées brutes **sans obligation de les finaliser**. Une note ancienne peut nourrir plusieurs projets. Ne pas présenter le suivi vocal comme une compétition de métriques : la qualité des notes d'entraînement prime.

### Développement personnel / leadership : conservation et provenance

```text
Source (livre/conférence/expérience)
  └── Observation / citation paraphrasée
        └── Principe / réflexion personnelle
              └── Application vécue (optionnelle)
              └── Projet de livre ou de formation (futur, non publié)
```

Chaque réflexion peut comprendre Date, Source, Mots-clés, Contexte, Application, Évolution de pensée, Confidentialité. Il faut distinguer une conviction personnelle, une citation sourcée, une hypothèse et un enseignement rédigé ultérieurement. **Ne pas réécrire les convictions privées pour les rendre « plus professionnelles ».**

### Apprentissage et certifications

Distinguer :
- programme : objectif ou certification ;
- modules : thèmes/compétences ;
- session d'étude : date, temps, exercices ;
- ressources : notes, labs, vidéos et documents ;
- bilan : acquis, incertitudes, prochains exercices.
Les relations évitent que la même fiche de cours soit dupliquée dans « cette semaine » et « certification ».

### Produits digitaux et SaaS

Pipeline adapté : Idée → Recherche → Validation → Prototype → Test → Publiable → Publié → Maintenance. Éviter de qualifier une idée de produit validé sans preuve (retours utilisateurs, test réel, proposition de valeur).

## 5. Inventaire de migration : un travail indispensable

Un agent **ne doit pas** décider qu'une page est un doublon car son titre ressemble à une autre. Chercher contenu unique, sous-pages, pièces jointes, commentaires, liens entrants et historique.

Table de suivi recommandée :

| Source actuelle | Nature | Cible | Action | Validation |
|---|---|---|---|---|
| « Mes Notes » | notes mixtes | Knowledge + Inbox | extraire progressivement | liens et fichiers intacts |
| « Life OS 1 » | accueil ancien | Archives / legacy | conserver en accès discret | vues existantes disponibles |
| « Tâches » | base de production | source centrale | réutiliser, créer vues | statuts inchangés |
| « CRM » | base métier | carrière | réutiliser | candidatures intactes |
| « Journal libre » | réflexion | Knowledge privé | garder privé ; migration optionnelle | contexte conservé |

Une migration est complète quand **les entrées sont vérifiées**, pas simplement lorsque les anciennes pages sont masquées.

## 6. Traitement de l'Inbox

```text
CAPTURE (sans classement)
   ↓
REVIEW : Qu'est-ce que c'est ?
   ├─ action concrète → TASK
   ├─ résultat à produire → PROJECT
   ├─ connaissance durable → KNOWLEDGE
   ├─ référence temporaire → RESOURCE
   └─ rien d'utile pour le moment → ARCHIVE (pas forcément supprimer)
```

La vitesse de capture doit être indépendante de la précision du classement. La revue est un acte distinct (quotidien ou hebdomadaire selon le volume).

## 7. Requêtes de validation

Avant/après, tester :
1. retrouver une note par sujet sans connaître sa page d'origine ;
2. retrouver les documents liés à un projet ;
3. afficher une tâche sur deux vues sans avoir deux copies ;
4. enregistrer une inspiration audio en dehors d'une session prévue ;
5. identifier la source originale d'une information déplacée ;
6. retrouver un projet terminé plusieurs années après.

Si ces tests échouent, la jolie interface masque une architecture fragile.
