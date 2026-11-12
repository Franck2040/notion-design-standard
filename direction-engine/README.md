# Moteur de direction artistique Notion — version 1.0

> **Statut : guide de conception, non application exécutable.** Il transforme un brief en directions artistiques comparables. Les recommandations restent à implémenter et tester dans la version et le forfait Notion de l'utilisateur. Il ne promet ni CSS libre, ni thème global à bouton, ni édition native des actions par toutes les intégrations.

## Contrat d'entrée

Ne pas choisir « minimaliste bleu » par défaut. Constituer un brief avec :

| Champ | Questions à résoudre | Exemple fictif |
| --- | --- | --- |
| Utilisateur | Qui utilise réellement le système ? Individu/équipe, expérience Notion, contraintes visuelles, appareils | Une petite association, 6 bénévoles, mobile fréquent |
| Décision principale | Quelle question la page doit-elle résoudre dans les 30 premières secondes ? | « Quel événement doit être préparé ? » |
| Action principale | Que doit pouvoir faire l'utilisateur en un geste ? | Créer une nouvelle activité |
| Données | Sources existantes, volumes, propriétés, relations, fichiers, qualité de données | Événements, participants, tâches |
| Contexte | Usage quotidien / hebdomadaire, travail concentré / lecture / terrain, confidentialité | Usage rapide et partagé |
| Sensibilité | Enjeux d'erreur, accessibilité, statut d'une information, coût d'une erreur | Éviter d'oublier un bénévole |
| Identité | Émotions à évoquer, références appréciées/rejetées, logo/palette disponible | Chaleureux, accueillant, non enfantin |
| Contraintes | Notion gratuit/Plus/Business, outils disponibles, mobile, permission, autonomie | Pas de Dashboard view si forfait incompatible |
| Succès | Tests mesurables, seuils et preuve | Ajouter un événement, retrouver les tâches liées |

**Si des éléments manquent** : poser au maximum les questions qui empêchent vraiment de travailler ; sinon retenir des hypothèses explicitement révisables. Ne pas transformer un goût de l'agent en préférence de l'utilisateur.

## 1. Diagnostiquer avant de dessiner

Écrire une phrase pour chacun :
1. **Job-to-be-done** — « Lorsque [situation], je veux [action], afin de [résultat]. »
2. **Unité d'attention** — ce qui doit dominer la page : échéance, œuvre, document, projet, personne, événement, métrique ?
3. **Volume** — 5, 50 ou 5 000 éléments : la même galerie n'est pas adaptée à toutes les tailles.
4. **Rythme** — consultation rapide, travail continu, revue mensuelle, exploration libre.
5. **Coût d'erreur** — un statut trompeur est-il plus grave qu'un manque de personnalisation ?
6. **Sources de vérité** — la donnée a-t-elle une base d'origine ? Quelle vue peut la montrer sans duplication ?

## 2. Générer trois hypothèses **structurellement** différentes

Produire exactement trois concepts en variant **la hiérarchie et le mode d'interaction**, pas simplement la couleur :

- **A — Utilitaire / Focus** : capture et état de travail en premier, liste compacte, faible décoration.
- **B — Éditorial / Studio** : œuvre, collection, récit ou média en premier, aperçu plus généreux, détails progressifs.
- **C — Analytique / Pilotage** : exceptions, échéances, décisions ou tendances en premier, vues croisées et sources vérifiables.

Ces noms ne sont **pas** des templates obligatoires : si les trois sont mal adaptés au besoin, proposer trois autres axes. Chaque concept fournit : croquis textuel (desktop et mobile), action principale, données nécessaires, 2 vues maximum au premier écran, famille d'icônes, choix de couleur, comportement d'état vide, contraintes Notion, coût d'entretien et risque majeur.

### Éviter les « fausses variantes »

Deux variantes qui ne diffèrent que par bleu/vert ou par la position de trois boîtes sont équivalentes. Pour être distinctes, au moins **deux** éléments doivent changer : premier objet visible ; ordre des actions ; mode d'exploration (liste vs galerie vs calendrier) ; profondeur de navigation ; quantité d'information ; interaction de capture.

## 3. Sélectionner une direction (score + exclusions)

Pondération initiale, **à ajuster au brief** :

| Critère | Poids | Comment noter |
| --- | ---: | --- |
| Première action évidente | 25 | L'utilisateur la trouve sans guide |
| Adaptation aux données et au domaine | 20 | La bonne unité d'attention est visible |
| Faisabilité native + plan + permissions | 20 | Aucun faux composant, dépendance connue |
| Lisibilité / accessibilité / mobile | 15 | Ordre et contraste vérifiables |
| Signature émotionnelle cohérente | 10 | Une identité et non un décor arbitraire |
| Maintenance / croissance | 10 | Modifications sans recréer les bases |

**Critères éliminatoires** : perte de données, action fictive, besoin de privilèges impossibles, accessibilité gravement insuffisante, usage de visuels tiers sans droits. Un score élevé ne compense jamais un critère éliminatoire. Le score est une aide à la décision, pas un benchmark validé.

## 4. Définir une identité sans copie de template

- **Signature** : choisir un seul élément dominant justifié (typographie de titre, photographie autorisée, bandeau sobre, grande liste éditoriale, galerie, repère couleur). Pas six signatures simultanées.
- **Palette** : neutre dominant + accent primaire contextuel + états sémantiques. Vert, bleu, violet, brun ou ambre peuvent convenir. Ne pas associer automatiquement un métier à une couleur.
- **Hiérarchie** : primaire = décision/action ; secondaire = informations facilitatrices ; tertiaire = navigation/archives. Mesurer la hauteur du premier écran.
- **Iconographie** : famille native cohérente. Flèche = retour, plus = ajout, loupe = recherche, dossier = projet, archive = conserver sans effacer, corbeille = suppression. Pas d'emoji de substitution.
- **Couvertures** : facultatives ; leur présence doit servir la reconnaissance ou l'ambiance. Vérifier les recadrages et l'attribution/licence.
- **Rythme** : alterner groupes denses et respirations, éviter callouts colorés systématiques, longues chaînes de tableaux ou gradients omniprésents.

**Limite structurelle** : Notion n'expose pas le contrôle CSS d'une application web personnelle. Les hex, typographies et espacements précis sont des intentions de maquette, pas des valeurs garanties dans une page Notion native. Reprendre les couleurs proposées dans l'éditeur au plus près, sans prétendre à une correspondance exacte.

## 5. De la direction à l'implémentation

1. Choisir les patterns dans [la bibliothèque](../composition-library/README.md), **pas** par hasard.
2. Pour chaque zone, choisir un composant dans [le catalogue](../component-catalog/README.md).
3. Cartographier composant → source de vérité → vue/filtre → action → permission → test.
4. Marquer chaque capacité `confirmée`, `configurée`, `testée` ou `bloquée`. Une requête API réussie ne démontre pas que le bouton fonctionne dans l'interface.
5. Construire sur une page de test ou de manière réversible. Tester avec une donnée factice non sensible.
6. Vérifier en desktop et mobile ; améliorer à partir des défauts observés, pas de l'appréciation subjective de l'agent.

## 6. Livrable obligatoire de l'agent

```yaml
brief:
  utilisateur: "..."
  job_to_be_done: "..."
  decision_30_secondes: "..."
  capture_prioritaire: "..."
  appareils: ["desktop", "mobile"]
  sources_existantes: ["..."]
  limites_connues: ["..."]
concepts:
  - nom: "A"
    composition: "..."
    signature: "..."
    priorite_ux: "..."
    composants_nat: ["..."]
    risque: "..."
    score_estime: null
  - nom: "B"
    composition: "..."
  - nom: "C"
    composition: "..."
choix:
  concept: "..."
  justification: "..."
  compromis: ["..."]
verification:
  tests_effectues: []
  tests_non_effectues: []
  blocages: []
```

Un `score_estime` doit rester une appréciation de conception jusqu'aux tests utilisateurs. **Ne jamais substituer une maquette à une modification Notion réellement effectuée.**

## Références

- [Notion — vues et filtres](https://www.notion.com/help/views-filters-and-sorts)
- [Notion — mises en page de bases](https://www.notion.com/fr/help/layouts)
- [AgentsORG/DESIGN](https://github.com/AgentsORG/DESIGN) : séparation intention, contraintes, composants et règles, **architecture étudiée, code non copié**.
- [Référentiel actuel](../docs/08-agent-execution-and-visual-direction.md) : contrats de preuve et iconographie.
