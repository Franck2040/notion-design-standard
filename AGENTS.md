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
