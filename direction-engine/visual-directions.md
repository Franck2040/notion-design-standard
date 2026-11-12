# Six directions visuelles — vocabulaire de composition, pas presets imposés

> Les exemples donnent des **intentions**. Notion natif ne permet pas le contrôle complet des polices, des gradients, du CSS, des espacements ou des hex exacts. Un agent doit traduire ces intentions vers les réglages disponibles, puis inspecter le résultat. **Aucun des six styles n'est le style universel.**

## 1. Atelier éditorial

- **Usage fort** : portfolio, écriture, musique, publication, collection d'œuvres.
- **Signature** : une création vedette, puis galerie de pièces choisies ; titres aérés et descriptions courtes.
- **Contraste** : base neutre chaude, accent facultatif (vert profond, aubergine, brun, noir).
- **Composants** : page principale, galerie avec couvertures possédées, fiche détaillée, capture d'inspiration, version.
- **À ne pas faire** : transformer chaque action en grande vignette, utiliser une image d'illustration sans provenance.
- **Stress test** : aucune image ou plus de 50 œuvres.

## 2. Cockpit utilitaire

- **Usage fort** : tâches, stages, projets individuels, opérations quotidiennes.
- **Signature** : actions et délais avant toute décoration ; deux vues pertinentes sur le premier écran au maximum.
- **Contraste** : neutres dominants, accent pour les priorités importantes, statut d'erreur non confondu avec une étiquette.
- **Composants** : capture native, liste filtrée, prochaine échéance, projets actifs, navigation réduite.
- **À ne pas faire** : afficher 10 métriques sans décision associée.
- **Stress test** : 0 tâche, 300 tâches, dates absentes, toutes terminées.

## 3. Bibliothèque documentaire

- **Usage fort** : recherche, connaissances, méthodes, documentation interne.
- **Signature** : recherche + filtres bien définis + provenance visible.
- **Contraste** : base calme, peu d'accents, statut de vérification clairement libellé.
- **Composants** : liste, filtres par domaine/type, fiche source et historique, note à examiner.
- **À ne pas faire** : perdre les textes originaux derrière un résumé IA.
- **Stress test** : deux documents quasi identiques et 10 versions liées.

## 4. Console analytique

- **Usage fort** : équipes, incidents, pipelines, opérations récurrentes.
- **Signature** : exception à traiter + état réel + lien vers détail vérifiable.
- **Contraste** : palette d'états sémantiques, couleurs utilisées uniquement si elles portent un sens.
- **Composants** : liste des alertes, board, table spécialisée, chart lorsqu'il est disponible et pertinent.
- **À ne pas faire** : chiffres inventés, widgets Business sur forfait incompatible, 12 graphiques sans question.
- **Stress test** : données manquantes, anomalie de calcul, accès lecture seule.

## 5. Espace serein et personnel

- **Usage fort** : journal, habitudes, activités familiales, rétrospectives.
- **Signature** : capture chaleureuse, section du jour, archives discrètes.
- **Contraste** : blanc cassé ou gris clair, accent doux (vert sauge, ocre, violet atténué) selon les préférences, sans imposer une signification psychologique universelle.
- **Composants** : journal daté, routine, calendrier limité, callout discret d'orientation.
- **À ne pas faire** : mécanismes de streak culpabilisants, abondance de badges rouges, notes personnelles exposées.
- **Stress test** : absence de saisie pendant un mois, mobile, partage involontaire.

## 6. Centre de formation

- **Usage fort** : cours, exercices, certifications, parcours pédagogique.
- **Signature** : prochaine séance / révision / livrable visible d'abord, bibliothèque de cours ensuite.
- **Contraste** : distinction visuelle entre « à apprendre », « à faire », « revu », sans ne s'appuyer que sur la couleur.
- **Composants** : prochaines échéances, notes par cours, questions, révisions, ressources liées.
- **À ne pas faire** : afficher un calendrier géant à la place des devoirs urgents.
- **Stress test** : années archivées, matières avec mêmes noms, exercices sans échéance.

## Choisir sans caricaturer le domaine

Une association peut nécessiter une console analytique ; un ingénieur peut préférer une galerie pédagogique ; un studio artistique peut exiger un cockpit de production. Le domaine donne des **hypothèses**, pas un verdict. La preuve décisive reste le job-to-be-done et la validation avec données réelles.

## Contrat de style à remettre à l'agent

```yaml
direction:
  nom: "..."
  pourquoi: "..."
  objet_primaire: "..."
  signature_visuelle: "..."
  densite: "compacte | moyenne | éditoriale"
  palette:
    fond: "neutre | chaleureux | sombre"
    accent: "vert | bleu | violet | ambre | autre | aucun"
    etats: "signification documentée, texte lisible sans couleur"
  navigation: "mentions natives | bloc synchronisé | autre"
  icones: "famille native cohérente ; pas d'emojis de substitution"
  couvertures: "utiles et sous licence | non nécessaires"
  mobile: "ordre de priorités explicite"
  contexte_du_test: "..."
  inconnues: []
```

## Test d'originalité

Comparer deux solutions conçues à partir de briefs différents : si mêmes cinq cartes, mêmes couleurs, mêmes ordres et mêmes vues sont proposés sans justification, le moteur a échoué. La diversité doit porter sur l'**architecture d'interaction et la hiérarchie**, pas sur une simple rotation de couleurs.
