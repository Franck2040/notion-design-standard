# 04 — Design d'interfaces : maquettes, variantes et parcours

## 1. Cockpit desktop : priorité au premier écran

```text
┌───────────────────────────────────────────────────────────────────────────────┐
│ Life OS                                       [FR | EN] (navigation)  [?]      │
├──────────────────┬────────────────────────────────────────────────────────────┤
│ ⌂ Accueil        │   Bonjour · mardi 10 novembre                + Capture    │
│ ◷ Aujourd'hui    ├──────────────────┬────────────────┬────────────────────────┤
│ ▣ Projets        │  MON FOCUS       │  ÉCHÉANCES     │   HORLOGE / MÉTÉO      │
│ ◇ Domaines       │  1 action       │  2 proches     │   Widget discret       │
│ ▤ Connaissances  ├──────────────────┴────────────────┴────────────────────────┤
│ ♫ Studio         │  [Aujourd'hui] [À traiter] [Cette semaine] [Projets]       │
│ ▧ Finances       │  ┌─────────────────────────────────────────────────────┐   │
│ ◫ Archives       │  │ tâche A — priorité  ·  projet lié       [ouvrir]    │   │
│                  │  │ tâche B — délai     ·  projet lié       [ouvrir]    │   │
│                  │  │ tâche C — en cours                       [ouvrir]    │   │
│                  │  └─────────────────────────────────────────────────────┘   │
│                  │  Projets actifs : 3 cartes compactes                       │
└──────────────────┴────────────────────────────────────────────────────────────┘
```

**Ce qui est intentionnel** :
- la navigation reste relativement calme ;
- la capture apparaît avant les longues bases ;
- la météo et l'horloge sont un accent, pas la moitié de la page ;
- le centre expose un **état de travail**, pas seulement des destinations ;
- une seule vue principale est active à la fois.

**Notion natif** : simuler la navigation par colonne + bloc synchronisé ; vues liées ; onglets ou vues filtrées ; fiches ouvertes en Side peek / Center peek quand disponibles. Ne pas promettre un menu latéral fixe au scroll, du CSS arbitraire ou des overlays React dans un template natif.

## 2. Version mobile

```text
┌────────────────────────────┐
│ Life OS       [Menu] [+]   │
├────────────────────────────┤
│ Focus du jour              │
│ Prochaine échéance         │
├────────────────────────────┤
│ Tâches · Aujourd'hui       │
│  • Action A                │
│  • Action B                │
│  Voir plus                 │
├────────────────────────────┤
│ Navigation compacte        │
│ Projets  Notes  Agenda     │
└────────────────────────────┘
```

L'ordre ne doit pas reproduire le côté gauche du desktop puis dérouler tous les widgets avant les tâches. Le mobile sert surtout à capturer, consulter et cocher ; le classement complexe peut être réservé au desktop.

## 3. Trois variantes d'interface : adapter selon usage

### A. « Focus » pour un utilisateur débordé
- accueil minimal ;
- une priorité, tâches ouvertes, échéances ;
- journal et projets dans un second niveau ;
- excellente ergonomie, moins de visibilité panoramique.

### B. « Studio » pour créateur polyvalent
- navigation stable ;
- zone projets, idées récentes et contenus média ;
- galerie de créations et zone capture ;
- risque de multiplier les images ; prévoir un mode liste efficace.

### C. « Analyste » pour suivre plusieurs flux
- quelques KPI, tables compactes, incidents ou retards ;
- filtres rapides, calendrier/timeline secondaire ;
- éviter des métriques sans question métier.

**Ne pas mélanger aveuglément les trois variantes.** Un Life OS peut avoir un cockpit A et des espaces spécialisés B/C.

## 4. Micro-interactions — exemples précis

### « Ajouter une idée »
Avant : clic « Notes » → chercher sous-page → nouvelle page → titre → retour.
Après : une action « Capturer » ouvre une nouvelle entrée Inbox, date automatique, type proposé, champ texte. L'utilisateur peut quitter le formulaire sans choisir le domaine.

**Test d'acceptation** : idée enregistrée en quelques gestes, visible dans « À trier ».

### « Marquer une tâche comme terminée »
Après : propriété Status modifiée dans la vue liée. La tâche quitte la vue des tâches ouvertes et reste dans l'historique. Si action récurrente : vérifier l'automatisation, éviter les doublons.

**Test** : la tâche apparaît une seule fois dans la source centrale et son statut est cohérent partout.

### « Reprendre un projet »
Après : clic sur la carte compacte → fiche en aperçu latéral avec prochaines tâches et notes liées. Le contexte de la page d'accueil reste visible si l'interface et le type de vue le permettent.

**Test** : on peut modifier une tâche liée et revenir au cockpit sans recourir à « arrière » plusieurs fois.

### « Reprendre un morceau »
Après : « Studio musical » → vue « À poursuivre » ; fiche avec brouillon de paroles, démo, inspirations audio et prochaines étapes. L'accès n'exige pas une navigation à travers l'archive entière.

## 5. Icônes et rythme visuel

- Choisir une famille d'icônes. Les icônes natives Notion monochromes peuvent fournir une cohérence durable.
- Éviter une icône différente à chaque ligne ; réserver la couleur aux domaines et aux états significatifs.
- Palette indicative : blanc cassé `#F8F9F6`, vert sauge `#DCE7DB`, vert encre `#32503A`, beige `#EDE8E1`, gris texte `#323A34`. **Palette indicative seulement** : les blocs Notion ne permettent pas toutes les valeurs HEX ; respecter ses couleurs natives et utiliser des assets lorsque pertinent.
- Une couverture peut ancrer une page, mais son poids et sa hauteur ne doivent pas repousser les informations urgentes trop bas.

## 6. Réduire la hauteur utile

Hiérarchie proposée sur desktop :
1. navigation / identité : petite ;
2. résumé : trois cartes sur une ligne ;
3. vue principale : quelques entrées ;
4. projets actifs : quelques cartes ;
5. informations supplémentaires : repliables / vues alternatives.

Compter les écrans nécessaires pour :
- voir la première tâche ;
- voir la prochaine échéance ;
- capturer une idée ;
- retrouver un projet ;
- accéder aux archives.

Si la première tâche se trouve à deux longueurs de scroll, la page est trop narrative pour être un cockpit.

## 7. Utiliser la beauté pour respirer

Exemple d'intégration : une météo et une horloge côte à côte dans un bloc de 250–300 px, palette coordonnée, sans publicité ni animation agressive. En mobile, un widget peut être masqué ou déplacé sous les actions. **Mais Notion natif ne masque pas nécessairement un bloc conditionnellement selon l'écran** : vérifier le comportement ou choisir un widget suffisamment compact pour les deux.

Un élément décoratif est acceptable si le temps d'accès aux tâches n'augmente pas notablement et si sa présence est choisie, pas imposée.

## 8. Notion vs application web personnalisée

| Ambition | Notion natif | React/Framer/SaaS |
|---|---|---|
| Colonnes, callouts, vues, onglets | Oui, selon fonctionnalités disponibles | Oui |
| Fiches en panneaux | Selon les vues et paramètres | Oui, modales sur mesure |
| CSS précis, composants sticky | Non, pas librement | Oui |
| Changer langue de tous les textes d'un clic | Non natif | Oui si développé |
| Forcer l'apparence globale d'un clic personnalisé | Non natif | Oui dans son application |
| Partager un template duplicable dans Notion | Oui | Non équivalent |
| Widgets externes | Via embeds compatibles | Intégration sur mesure |

Il faut d'abord choisir le **produit** : template Notion ou application web intégrée. Ne jamais promettre l'expérience du second avec les possibilités du premier.


## Addendum v1.1 — direction visuelle à vérifier

Ne pas confondre schémas ASCII d'exemple et injonction d'utiliser des caractères Unicode ou emojis comme icônes dans les pages. Pour une interface réelle : icônes natives Notion homogènes, signification des actions, pas d'emojis de décoration. Le bleu n'est pas la seule couleur : partir d'un fond calme et d'un accent choisi selon l'espace (vert sauge possible), ajouter d'autres couleurs par nécessité sémantique et tester contraste et mobile. Ne pas automatiser l'ajout de couvertures, de gradients ou de cartes colorées sans diagnostic des usages. Un menu latéral par mentions de pages doit reprendre leurs véritables icônes ; un emoji devant un lien n'est pas une icône native. Voir [08](08-agent-execution-and-visual-direction.md).
