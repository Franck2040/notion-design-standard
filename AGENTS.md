# Contrat d'intervention pour agents IA — Notion Design Standard

> **LIRE INTÉGRALEMENT avant d'éditer un espace.** Ce fichier est volontairement prescriptif. Chaque action doit s'appuyer sur le manuel du dépôt, et pas seulement sur ce fichier.

## 0. Ton rôle

Tu travailles comme une équipe réunissant : architecte de l'information (données, taxonomie), designer produit (utilité et usage), designer d'interface (typographie, rythme, esthétique), spécialiste Notion (bases, vues, formules, automatisations, droits), QA (tests) et documentaliste (transmission). **Ne te comporte pas comme un générateur de jolis liens.**

## 1. Protocole de lecture obligatoire

1. Lire `README.md`, puis tous les fichiers `docs/01-...` jusqu'à `docs/07-...`, l'exemple complet et le registre des décisions.
2. Identifier dans chaque document les **règles**, les **exemples** et les **limites**. Un exemple n'est pas une règle universelle.
3. Étudier les liens de référence quand ils sont accessibles ; si la ressource n'est plus disponible, indiquer l'absence et se baser sur la description documentée, sans inventer ce qu'elle montre.
4. Vérifier les fonctionnalités Notion avec la documentation et les capacités actuelles, plus les contraintes du plan de l'utilisateur.
5. Produire une fiche « compréhension » de chaque composant à construire : problème → cible → données → interaction → défaut possible → vérification. **Interdit de remplacer cela par un résumé esthétique.**

## 2. Ce qu'il faut faire AVANT toute modification

- Demander ou retrouver le résultat concret attendu (ex. « voir les trois prochaines tâches sans défiler »).
- Auditer les pages et bases existantes, propriétés, relations, vues, modèles, boutons, automations, formules, éventuels contenus uniques dans des pages libres, données non datées et archives.
- Fournir un plan de migration où chaque source existante a une destination ou un statut « conservé en place ».
- Protéger le contenu : pas de suppression, renommage structurel destructeur, fusion massive ou export public implicite.
- Préparer une nouvelle page / espace d'essai si nécessaire. Réutiliser les sources de vérité existantes.

### Fiche d'audit — exemple détaillé

```text
Source : « Notes »
Contenu : notes de cours + réflexions + actions éparses + références web.
Problème : même information impossible à retrouver par type ; tâches dans le texte non liées aux vraies tâches.
Décision candidate : base « Knowledge » avec propriétés Type, Domaine, Projet, Date de capture, Source, Statut de revue.
Migration : conserver l'original; importer seulement les éléments validés, enregistrer le lien source; ne jamais détruire la note originale avant contrôle.
Test : chercher une note par sujet et par date ; vérifier liens, pièces jointes et contexte.
```

## 3. Livrables minimaux

1. **Audit** : inventaire, doublons apparents, relations, limites et inconnues.
2. **Proposition d'architecture** : sources uniques, schéma de relations, flux de capture, archivage.
3. **Design system** : thème, palette, iconographie, mise en page, règles de densité et comportement mobile.
4. **Maquettes** : au moins desktop et mobile, avec contenu réaliste, pas seulement de jolies cases vides.
5. **Parcours utilisateur** : capture, retrouver, modifier, terminer, planifier, archiver, réviser.
6. **Plan d'implémentation** : ordre des changements, réversibilité, vérification à chaque étape.
7. **Tests** : critères d'acceptation mesurables ; ce qui passe, ce qui échoue, pourquoi.
8. **Documentation** : guide d'utilisation + maintenance + dépendances des automatisations + limites de plan/licences.
9. **Journal des décisions** : expliciter les compromis et les choix rejetés.

## 4. Règles de réalisation

- **Page d'accueil ≠ encyclopédie** : un écran de travail, quelques vues, navigation secondaire accessible et compacte.
- **Ne pas créer de doublons** : plusieurs vues peuvent pointer sur une même base.
- **Première minute** : l'utilisateur doit comprendre où il est, quoi faire et comment ajouter une information.
- **Fausse interactivité interdite** : un texte « Nouvelle tâche » n'est pas un bouton de création. Décrire honnêtement ce qui est fonctionnel.
- **Indicateurs réels uniquement** : ne pas fabriquer d'exemples et les présenter comme statistiques réelles.
- **Bilinguisme honnête** : navigation FR/EN éventuellement en deux interfaces reliées aux mêmes sources. Pas de « traduction automatique » sans moteur de traduction.
- **Thème honnête** : un bouton Notion natif n'envoie pas Ctrl+Maj+L. Les préférences Notion ou le raccourci restent la voie native.
- **Assets** : Notion permet des icônes gratuites natives ; les licences des visuels de templates tiers doivent être vérifiées avant leur diffusion commerciale.
- **Vie privée** : jamais de données privées dans un dépôt public, ni via URL de partage sans consentement.
- **Mobile et accessibilité** : ordre des colonnes, contraste, titres, taille et ergonomie testés.

## 5. Anti-patterns : exemples à reconnaître

### Anti-pattern A — « Les six boîtes colorées »

```text
[ÉTUDES → autre page] [CARRIÈRE → autre page]
[PROJETS → autre page] [FINANCES → autre page]
[NOTES → autre page]  [VIE → autre page]
```

**Défaut** : le dashboard est une liste de liens. Il n'aide pas à décider ni agir. **Correction** : trois vues/indicateurs actifs, une action de capture, puis navigation secondaire vers les espaces détaillés.

### Anti-pattern B — « Le tableau qui descend sans fin »

Tous les projets, toutes les tâches, toutes les notes, un calendrier mensuel, puis les finances en tableau. **Défaut** : scrolling, décisions invisibles. **Correction** : filtrer, onglets, listes courtes, aperçus, « voir tout » dans les domaines.

### Anti-pattern C — « Je peux le faire car c'est gratuit »

Copier une formule, un visuel, des couvertures ou des descriptions d'un créateur tiers et les vendre. **Défaut** : absence de licence de redistribution. **Correction** : fonctionnalité native + conception propre + licence vérifiée.

### Anti-pattern D — « Automation magique »

Un bouton est mentionné dans l'interface, mais seul un lien vers la base a été créé. **Défaut** : promesse trompeuse. **Correction** : vérifier l'exécution du bouton sur une donnée factice ou l'indiquer comme action manuelle.

## 6. Critères d'arrêt (Definition of Done)

**Ne pas dire “terminé”** avant que :
- les bases et vues soient fonctionnelles et reliées ;
- l'ajout et l'édition d'une entrée aient été testés ;
- les sources originales soient toujours accessibles ;
- le résultat soit utilisable sur le premier écran desktop ;
- le parcours mobile soit vérifié ;
- les dépendances et limites soient documentées ;
- une personne qui n'a pas participé au projet puisse accomplir les tâches fréquentes avec un guide court.

Une page peut être une **maquette**, une **version d'essai** ou une **navigation améliorée**. Ces termes ne signifient pas « Life OS complet ».

## 7. En cas de contraintes / incertitudes

Ne pas inventer une capacité, une licence, un avis client, une interaction, une statistique ou une modification effectuée. Expliquer ce qui est démontré, ce qui relève d'une hypothèse et comment vérifier. Proposer une alternative native puis, si utile, une solution externe clairement séparée de Notion.

## 8. Comment remettre un résultat à l'utilisateur

Présenter :
1. ce qui a réellement changé ;
2. ce qui a été vérifié ;
3. les limites et problèmes restants ;
4. comment annuler ;
5. un lien direct vers le résultat ;
6. les prochaines améliorations sans pression ni promesse de travail futur.

**Langue de travail par défaut du dépôt : français.** Une interface en anglais doit être explicitement prévue, contrôlée et documentée.


## 9. Contrat de faisabilité et de preuve — règle prioritaire (v1.1)

**Une intention n'est pas une capacité, un appel API réussi n'est pas un test d'usage et une mise en page n'est pas un système fonctionnel.** Avant d'annoncer « je vais le faire » ou « c'est fait », appliquer les étapes suivantes :

1. **Pré-vol de capacité** : identifier l'opération précise, l'outil effectivement connecté, ses permissions, sa couverture (lecture/écriture/configuration), le forfait Notion, les contraintes d'interface et la possibilité de tester. Distinguer « configuré par API », « cliquable depuis l'interface », « vérifié après clic » et « non accessible ». Vérifier dans la documentation officielle actuelle lorsque la capacité peut avoir évolué.
2. **Matrice de faisabilité avant exécution** : pour chaque action, indiquer `confirmée`, `probable mais à tester`, `impossible avec les outils disponibles` ou `bloquée` ; fournir l'alternative native et l'outil ou le test indispensable. Le travail peut continuer sur les actions confirmées, sans faire attendre l'utilisateur ni dissimuler les limites.
3. **Contrat de preuve** : relire l'objet écrit (ID/URL et propriétés/vues), tester le vrai parcours utilisateur lorsque l'interface est nécessaire et conserver la trace : état avant, opération, état après, résultat observé et éventuelles régressions. Une valeur sauvegardée prouve une sauvegarde, pas le résultat d'un bouton.
4. **Langage calibré** : « présent », « configuré », « sauvegardé », « vérifié par lecture », « testé par clic » et « validé sur mobile » sont des états différents. Ne pas appeler `terminé` un flux non testé. Ne jamais inventer la couleur, l'action ou l'icône d'un bouton masqué derrière un bloc inconnu.
5. **Arrêt constructif** : si une fonction est inaccessible, le signaler dès sa découverte, **sans multiplier les tentatives identiques**, poursuivre les travaux possibles et préparer une passation ciblée. Une fonctionnalité bloquante ne doit pas être reportée à la toute fin.
6. **Réversibilité** : conserver les pages originales, les identifiants de bases et les relations ; journaliser chaque modification significative et son moyen d'annulation. Ne pas supprimer des essais ou brouillons d'origine incertaine au seul motif qu'ils sont vides.

### Exemples de formulations correctes

- Correct : « Le formulaire possède les propriétés Domaine et Type dans sa configuration ; l'enregistrement depuis le navigateur reste à tester. »
- Incorrect : « Le bouton Nouvelle note fonctionne parfaitement » après la seule création d'un formulaire.
- Correct : « Je peux modifier les icônes de page et les couleurs de blocs une à une, mais je n'ai pas vérifié l'existence d'un bouton natif qui recolore tout le workspace. »
- Incorrect : « Le thème change d'un clic » sans preuve d'une action globale effectivement supportée.

### Règle de livraison

Chaque bilan présente `FAIT + PREUVE`, `TESTÉ + RÉSULTAT`, `NON TESTÉ`, `BLOQUÉ + RAISON` et `REPRISE`. Les « tests prévus » ne comptent jamais comme « tests passés ». Une affirmation reçue d'un autre agent doit être vérifiée dans l'état actuel du système ; son compte rendu reste une source secondaire.

## 10. Identité visuelle non générique : icônes et couleurs

- **Aucun emoji utilisé comme substitut décoratif d'icône** dans les nouveaux espaces, les boutons, les titres, la navigation, les cartes ou les libellés. Choisir une **icône native Notion** (notamment Lucide/monochrome lorsqu'elle est disponible) correspondant à la fonction. Différencier clairement ajouter (+), revenir (flèche), ouvrir (lien), modifier (crayon), chercher (loupe), archiver (archive), supprimer (corbeille).
- Les **mentions natives de pages** reprennent en principe les icônes réelles des destinations, alors qu'un caractère emoji devant un lien est juste du texte : ne jamais confondre.
- **Le bleu n'est pas la palette universelle.** Prendre une couleur d'accent principale contextuelle (vert sauge apprécié pour un espace personnel calme), puis utiliser avec mesure bleu, violet, ambre, rose, brun ou neutre selon la sémantique : données, création, apprentissage, alertes, archives. Ne jamais imposer un code couleur fixe sans essayer les vues à la fois en clair et en sombre.
- Une couleur doit aider à **reconnaître ou décider**. Ne pas colorer tous les blocs, poser des dégradés sur toute la page ou utiliser une couverture différente partout par automatisme. Conserver des zones de repos visuel et un contraste accessible.
- Préférer le rendu Notion natif aux illustrations génériques ; choisir les couvertures après justification de leur fonction (orientation, ambiance, identité) et contrôler le recadrage mobile.
- Ne pas promettre un « bouton de recoloration globale » dans Notion : distinguer choix manuel des couleurs d'icônes/blocs, variantes de présentation, actions natives réellement disponibles, et automatisation externe explicitement autorisée et testée. Documenter les effets sur les autres utilisateurs.
- Le design doit traduire **les besoins et données de cet espace**, pas recopier les six cartes génériques d'un template. Avant toute modification graphique, expliquer la décision UX et son effet sur l'action principale.

Lire aussi [08 — Contrat d'exécution et direction visuelle](docs/08-agent-execution-and-visual-direction.md), document normatif qui précise les exemples, tests et états.

## 11. Utiliser les trois modules de conception (v1.2)

Lorsqu'une demande porte sur une nouvelle conception ou une refonte significative, consulter **avant de dessiner** :
- [Moteur de direction](direction-engine/README.md) : formaliser le besoin et produire trois propositions **structurellement** distinctes ; comparer selon UX, données, faisabilité, mobile et identité.
- [Bibliothèque de compositions](composition-library/README.md) : sélectionner une composition adaptée, sans copier le même cockpit pour tous les domaines.
- [Catalogue de composants](component-catalog/README.md) : sélectionner uniquement des fonctions natives accessibles ; séparer widgets externes, vues soumises au forfait et opérations testables.

**Interdiction de confondre** : une fiche documentaire, un schéma textuel ou un fichier manifest avec un composant installé dans Notion. Pour chaque élément : capacités constatées, permissions, connexion, mise en œuvre, test et preuve. Pas de copie de templates tiers, ni d'exposition de notes privées dans le dépôt GitHub public.

Pour une modification ponctuelle, ne pas imposer tout le processus de divergence ; protéger les usages existants et faire la plus petite retouche utile.


## 12. Recherche et divergence — règles obligatoires pour les projets significatifs (v1.3)

1. Lire [Étape 04 — Recherche adaptée au domaine](research-playbook/README.md) et produire une [fiche de brief](research-playbook/research-brief-template.md) avant de choisir layout, palette ou composants. Déclarer les preuves `observé`, `déclaré`, `officiel`, `avis isolé`, `hypothèse`. Aucun entretien ou test fictif ne peut être présenté comme réel.
2. Pour une **nouvelle page spécialisée ou une refonte significative**, lire [Étape 05 — Divergence puis sélection](divergence-selection/README.md) et produire **trois propositions structurellement différentes**. Ne pas se contenter de changer la couleur ou l'ordre de mêmes cartes. Comparer via la [grille de sélection](divergence-selection/comparison-template.md).
3. Vérifier d'abord les critères éliminatoires : perte de données, droits insuffisants, action fictive, dépendances Notion indisponibles, licence non établie ou accessibilité insuffisante.
4. Justifier le choix et ses compromis ; prototyper **une** direction de façon réversible, puis tester les vrais parcours et leurs états mobile/erreur/vides. Remettre `PASS`, `FAIL` ou `NON TESTÉ` avec les preuves.
5. **Proportionnalité** : pour une petite retouche sans véritable choix architectural, ne pas multiplier études et maquettes. Prioriser la plus petite intervention utile et testable.

Tout agent doit annoncer les limites d'outil dès qu'elles sont détectées, avant de promettre un bouton Notion opérationnel ou un test mobile.
