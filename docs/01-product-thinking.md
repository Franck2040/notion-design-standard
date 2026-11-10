# 01 — Penser comme une équipe de design produit

## 1. Distinguer quatre niveaux

Un espace Notion est à la fois :
- **Système de données** : où se trouve chaque information et comment elle est reliée.
- **Système d'actions** : comment capturer, traiter, planifier, terminer et retrouver.
- **Interface** : ce que l'utilisateur voit, dans quel ordre, avec quel feedback.
- **Expérience** : effort perçu, esthétique, fluidité, sentiment de contrôle, envie d'y revenir.

Améliorer un seul niveau échoue souvent. Un bel écran peut pointer sur dix bases incohérentes ; un schéma impeccable peut rendre la capture pénible.

### Exemple causal

**Symptôme** : « Je ne retrouve jamais mes idées de chansons. »

Mauvaise réponse : ajouter un lien « MUSIQUE » en page d'accueil.

Diagnostic approfondi :
- les idées existent en notes libres, clips audio, images et phrases ;
- elles arrivent de manière imprévisible ;
- certaines idées deviennent des projets, d'autres ne sont pas utilisées avant plusieurs années ;
- une idée doit être retrouvée par émotion, date, type, thème ou morceau associé.

Architecture répondant à ce besoin :
- une Inbox de capture à faible friction ;
- une base Idées avec type de média, date, sujet, lien fichier, état, éventuel projet associé ;
- une base Œuvres/Morceaux avec états Inspiration → Écriture → Composition → Enregistrement → Mixage → Publié ;
- une vue « à revoir » et une vue « prêts à développer », sans oublier les archives.

Interface :
- un accès « capturer » visible ;
- trois idées récentes ou à reprendre, pas tout l'historique ;
- fiches média en galerie si la dimension visuelle aide ;
- édition du détail en aperçu, depuis le contexte de travail.

**Test** : une idée dictée au téléphone est-elle enregistrable et retrouvable plus tard sans connaître à l'avance le futur morceau ?

## 2. L'esthétique n'est pas un supplément honteux

Une jolie horloge ou une météo ne sont pas seulement des « gadgets inutiles » ; elles peuvent servir de **point de respiration visuelle**, signaler que l'espace est vivant, ou renforcer un rituel d'ouverture. Elles n'ont pas besoin d'être défendues par un indicateur de productivité.

La question est **leur coût de présence** : combien d'écran occupent-elles ? perturbent-elles la lecture ? ralentissent-elles la page ? requièrent-elles une intégration externe collectant des données ? fonctionnent-elles sur téléphone ? changent-elles correctement de contraste ?

Un maximum raisonnable initial peut être **une horloge et un petit widget météo**, testés sans hypothèse sur leur utilité ; une troisième zone d'ambiance peut être ajoutée si l'écran le justifie. Ce n'est pas une règle immuable.

## 3. Concevoir en couches de dévoilement

**Couche 1 — aperçu** : ce qui réclame attention à court terme (focus, échéance, capture).
**Couche 2 — vue active** : tâches et projets en cours avec propriétés essentielles.
**Couche 3 — détail** : fiche tâche, projet, note, pièce jointe, historique.
**Couche 4 — administration** : propriétés, formules, bases techniques, templates, automatisations.
**Couche 5 — archives** : éléments fermés et patrimoine de connaissances.

La plupart des actions quotidiennes doivent rester aux couches 1 et 2. La profondeur doit être disponible, pas omniprésente.

### Exemple d'arbitrage : calendrier plein mois ?

- **Avantage** : vue spatiale, dates rassurantes, bon repère de planification.
- **Inconvénient** : hauteur considérable, surtout sur petit écran.
- **Choix** : mini-agenda « 7 prochains jours » sur l'accueil ; calendrier complet dans un onglet ou une page d'analyse. Si l'utilisateur gère une activité très calendaire, inverser ce choix.
- **Validation** : compter les clics pour voir la prochaine échéance et la surface occupée par les cases vides.

## 4. Différence entre « aimer une référence » et la copier

Décomposer une référence en :
1. **Intention** : que permet-elle de faire ?
2. **Structure** : navigation, hiérarchie, zones ?
3. **Interactivité** : bouton, formule, filtre, relation, ouverture ?
4. **Style** : palette, typographie, images, rythme ?
5. **Fragilité** : risque de complexité, plan payant, scripts externes, licence ?
6. **Transférabilité** : quel principe général est réutilisable sans copier le produit ?

Exemple : **barre latérale PARA**.
- Intention : passer facilement d'un domaine à l'autre.
- Structure : colonne étroite ; labels courts ; repères cohérents.
- Interactivité : liens / blocs synchronisés vers des pages détaillées.
- Style : icônes discrètes monochromes.
- Fragilité : surcharge si 20 domaines affichés ; pénible sur mobile.
- Transfert : une barre stable pour les 6–8 destinations les plus fréquentes, mobile avec menu compact.

## 5. Gestion de la densité

Un dashboard compact n'est pas une interface où tout est minuscule. Trois heuristiques à tester :
- priorité lisible en une seconde ;
- peu de lignes dans les vues opérationnelles ;
- espaces blancs qui séparent les décisions, pas les éléments d'une même opération.

**Ne pas imposer** un nombre de pixels ou d'éléments universel. Tester sur l'écran réel, à largeur réelle, navigateur et zoom habituels.

### Exemple avant / après

Avant :
```
BANNIÈRE DE 300 PX
INTRO DE 4 PARAGRAPHES
6 BLOCS COLORÉS CHACUN AVEC 6 LIENS
TOUTES LES TÂCHES (47 LIGNES)
CALENDRIER MOIS COMPLET
HISTORIQUE DES CANDIDATURES
ARCHIVES ...
```

Après :
```
[Navigation] | Focus prioritaire    | prochaine échéance
             | Capture rapide        | petite ambiance
             | Actions du jour (4)   | Projets actifs (3)
             | [Aujourd'hui] [Semaine] [Plus]
Détails administratifs : accessibles, non affichés.
```

Le second écran n'est pas « vide », il protège **l'attention**.

## 6. Quand une IA a compris le design

Elle ne se contente pas de dire « UI moderne, épurée et verte » ; elle doit savoir :
- expliquer pourquoi telle tâche appartient à la base A et pas à une page libre ;
- décrire ce qui se passe quand une date change ;
- prédire ce que verra l'utilisateur sur ordinateur et sur téléphone ;
- montrer l'avant/après d'une action ;
- choisir une esthétique adaptée au contenu, y compris une pause visuelle ;
- identifier ce qui cassera si on renomme un statut ;
- refuser de présenter un lien ordinaire comme une automatisation.
