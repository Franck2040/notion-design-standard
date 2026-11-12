# 08 — Contrat d'exécution et direction visuelle (v1.1)

> Document normatif pour agents intervenant dans un système Notion existant. **Ce fichier est public et générique : n'y copier aucune donnée personnelle ni URL privée de workspace.**

## A. Pourquoi une belle page a pu échouer

Une colonne de liens ornés de caractères emoji, des bannières génériques et quelques boutons dont on n'a pas accès à la configuration produisent une apparence de Life OS, pas un espace fiable. L'échec ne vient pas d'une palette insuffisante : il vient de la confusion entre *navigation*, *capture*, *interaction*, *information*, *preuve* et *livraison*. Le design doit répondre à des tâches réelles, avec des contrôles reproductibles.

### Démonstration problème → choix → preuve

| Besoin | Mauvaise réponse | Meilleur design | Preuve à obtenir |
| --- | --- | --- | --- |
| Capturer et catégoriser une note | Écrire « Nouvelle note » comme lien | Bouton natif ou formulaire vers Inbox unique, avec Domaine et Type | Créer une fiche, lire les champs enregistrés et la retrouver par filtre |
| Retrouver une réflexion ancienne | Copier un résumé sans provenance | Index avec lien vers source, thème, état, projet lié | Ouvrir source et vérifier contenu, pièces jointes et versions |
| Revenir à l'accueil | Texte « Back » sans action | Bouton natif ou mention de page, icône de flèche selon action | Cliquer puis contrôler la page d'arrivée |
| Montrer les urgences | Table entière de tâches | Vue filtrée sur retard / aujourd'hui, états ouverts seulement | Préparer trois cas tests et confirmer l'affichage |
| Donner de l'identité | Six cartes bleues, emoji à chaque ligne | Hiérarchie, icônes natives, espaces, petite palette sémantique | Captures desktop/mobile et test de lecture à 30 secondes |

## B. Portique « puis-je réellement faire cela ? »

**Avant d'écrire ou d'annoncer un résultat**, remplir ces colonnes :

| Opération | Capacité constatée | Permission et forfait | Test disponible | Statut |
| --- | --- | --- | --- | --- |
| Changer une icône de page | Outil de mise à jour et lecture de l'icône | Édition autorisée | Fetch après mutation | Configurable ; lecture vérifiable |
| Configurer un bouton natif | Dépend de l'intégration utilisée | Édition et interface souvent nécessaires | Cliquer dans Notion puis inspecter la cible | Ne pas déclarer valide par simple présence d'un bloc |
| Ajouter des champs à un formulaire | Dépend des vues et outils accessibles | Édition du formulaire | Soumission test + lecture de la fiche | Configuré puis testé séparément |
| Changer toutes les couleurs par un bouton | Fonctionnalité globale non établie | Inconnues à examiner | Démonstration sur plusieurs pages | Non promis sans preuve |
| Adapter mobile | Lecture des blocs insuffisante | Navigateur mobile requis | Captures et navigation tactile | Non testé par API seule |

Catégories de statut : `À ÉTUDIER`, `FAISABLE`, `CONFIGURÉ`, `TESTÉ`, `VALIDÉ`, `NON TESTABLE ICI`, `BLOQUÉ`. Mettre immédiatement à jour le statut si une capacité s'avère indisponible.

**Différence centrale** : un ID de bloc n'en donne pas automatiquement les actions internes ; une création de vue ne garantit pas son affichage ni son ergonomie ; l'existence d'un widget ne prouve pas son chargement ; la lecture d'un extrait d'une note ne garantit pas la migration de tout le corpus.

## C. Direction artistique : calme, expressif, pas générique

Le système est vivant : il peut évoluer d'une période à l'autre sans imposer une esthétique unique ni réinitialiser les bases.

- **Couleurs** : fond principalement clair, neutralité chaleureuse ; vert sauge ou vert profond possible comme accent d'identité, sans exclure bleu, violet, orange, rose ou brun lorsqu'ils portent une fonction. La palette exacte dépend des couleurs natives Notion, du contraste et des préférences effectives de l'utilisateur.
- **Iconographie** : famille cohérente d'icônes natives Notion (trait simple si possible). Pas d'emoji en remplacement. Les icônes de page font aussi office de repères dans les mentions et la navigation. Exemple : maison pour accueil, dossier pour projets, livre pour connaissances, calendrier pour dates, cible pour objectifs, note de musique pour studio, carte pour finances, archive pour historique.
- **Hiérarchie** : accueil = cockpit d'action ; pages de domaine = vues utiles + saisie ; archive = conservation + provenance. Texte d'orientation court, listes ciblées, filtres utiles. Réserver les tableaux riches aux pages spécialisées.
- **Bannières** : optionnelles. Une couverture n'est pas un progrès UX automatique ; privilégier un visuel intentionnel, peu chargé, et vérifier son recadrage. Ne pas « combler le vide » par des gradients, des images aléatoires ou des cartes de couleur partout.
- **Émotion et utilité** : une ambiance calme et agréable favorise la fréquentation ; elle ne doit pas cacher les tâches, les dates, ni ajouter du scroll.
- **Accessibilité** : sens compréhensible sans couleur seule ; texte lisible en clair/sombre ; zones tactiles suffisantes ; ordre mobile contrôlé ; titres français cohérents.

### Tests design anti-template

1. Remplacer les vraies données par six titres génériques : si le dashboard ne change presque pas d'utilité, le design est trop superficiel.
2. Masquer couleurs et couvertures : les actions restent-elles découvrables ?
3. Supprimer les étiquettes des icônes : un nouvel utilisateur peut-il comprendre leur fonction par le contexte ? L'icône seule ne doit pas devenir ambiguë.
4. Ouvrir sur téléphone : où se trouvent capture, tâches du jour, prochain événement et navigation ?
5. Lire les statuts : une donnée « À examiner » est-elle clairement différente d'une donnée « Vérifiée » ?

## D. Couleurs : ce que Notion permet, ce qu'il ne faut pas inventer

Les pages et callouts peuvent recevoir des icônes et couleurs via les réglages Notion ; les blocs de texte disposent d'options de texte/fond. Le thème clair/sombre se règle dans les préférences. **Un bouton Notion natif qui recolore d'un clic toutes les icônes et tous les blocs d'un espace n'est pas une capacité établie dans ce standard** : ne pas l'annoncer sans test documenté de la version et du compte.

Approches raisonnables :
1. Palette par domaine établie dans un guide, changements ponctuels d'icônes natives.
2. Quelques vues ou pages de présentation alternatives reliant les mêmes bases sans duplication.
3. Automatisation externe uniquement si demandée, autorisée, sécurisée, réversible et réellement testée.
4. Éviter les fausses variables globales CSS : Notion natif ne se pilote pas comme une application web personnelle.

## E. Boutons et formulaires : contrat vérifiable

Pour chaque bouton, renseigner : nom, icône native, page source, action cible, paramètres, effet attendu, permissions, test, résultat, retour possible.

- **Retour** : flèche gauche, page destination correcte ; tester depuis les sous-pages.
- **Ajouter** : plus, création dans la base unique ; vérifier les champs initialisés, la sauvegarde, l'absence de doublon.
- **Modifier** : crayon, ouverture/édition de la fiche attendue ; vérifier que la même donnée change dans toutes les vues.
- **Archiver** : symbole archive, état d'archive explicite ; ne pas assimiler à la suppression.
- **Supprimer** : corbeille, contrôle préalable de l'identité et de l'intention ; ne jamais nettoyer des données inconnues automatiquement.

Le bouton doit effectuer **l'action qu'il prétend effectuer** ; à défaut, afficher un libellé honnête « Ouvrir la base » ou un lien explicite. Un formulaire avec champ de titre seul ne peut pas être présenté comme un formulaire de classement complet. Tester la soumission avec contenu, type, domaine, date et classement après création.

## F. Audit des reprises d'anciens systèmes

Séparer trois preuves :

1. **Existence** : source et fichier accessibles.
2. **Indexation** : fiche résumée reliée à sa source, propriétés renseignées.
3. **Migration exhaustive** : chaque élément significatif, liste, version, image, pièce jointe et relation rapproché à l'original ; démontré par un inventaire et une comparaison.

Les deux premières preuves ne valent **pas** la troisième. Conserver l'original tant que l'exhaustivité n'est pas établie. Les fiches de test et les pages vides ne doivent ni polluer l'interface quotidienne, ni être supprimées sans identification et autorisation.

## G. Reprise, journal de décision et recette

En début de session : lire l'audit actuel, rechercher les changements récents, établir ce qui reste. Ne pas refaire la refonte parce qu'une session a changé. Conserver les IDs de base. Produire une matrice par module : `observé` / `corrigé` / `testé` / `bloqué`, avec liens et captures réelles quand disponibles.

Critères minimum : création, édition, classement, recherche, planification, archivage, préservation des données ; vues desktop et mobile ; bouton par bouton ; contraste ; navigation ; conformité iconographique. Si un point est impossible avec le connecteur, le dire **immédiatement**, pas après dix changements.

## H. Confidentialité et transmission

Ce dépôt public ne doit jamais contenir de contenu de notes privées, de CV, d'informations financières, d'URLs de partage privées ou de captures personnelles. Le journal de l'espace Notion privé doit décrire les anomalies réelles et contenir les références internes. Le dépôt stocke exclusivement la méthode réutilisable.

**Voir** : [AGENTS.md](../AGENTS.md), [04 — Layout](04-layout-patterns.md), [05 — Implementation](05-notion-implementation.md), [06 — Acceptance tests](06-acceptance-tests.md).
