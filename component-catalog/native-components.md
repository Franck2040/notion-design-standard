# Fiches de composants et recettes d'intégration

Ces fiches séparent **besoin, choix, configuration, comportement, preuve et alternative**. Elles ne prétendent pas que les boutons sont configurables par l'ensemble des connecteurs. Pour les options exactes, utiliser les liens de documentation [dans l'index](README.md).

## N06 — Mention native de page (navigation)

- **Question** : comment ouvrir le bon espace sans multiplier les liens bricolés ?
- **Usage** : navigation courte, fiche projet → source associée, retour accueil.
- **Construire** : utiliser la mention native vers la page existante ; choisir une icône native sur la page cible. La mention devrait reprendre le titre/icône d'origine ; vérifier le rendu dans l'éditeur.
- **À éviter** : taper un emoji devant un lien texte en prétendant avoir installé une icône native ; utiliser un lien de partage public inutile.
- **État vide** : si destination absente, supprimer le lien de la navigation secondaire, pas inventer sa page.
- **Test** : ouvrir la destination et revenir ; confirmer droits, titre actuel, icône, mobile.

## N07 — Blocs synchronisés

- **Question** : comment garder une navigation cohérente entre de nombreuses pages ?
- **Usage** : bande de navigation réutilisable, consigne de maintenance.
- **Construire** : créer un bloc synchronisé d'origine, copier ses références. Modifier ensuite l'original, pas chaque copie.
- **À éviter** : coller un lien vers une page entière en prétendant créer un bloc synchronisé ; exposer un contenu source auquel les lecteurs n'ont pas droit.
- **Test** : modifier une entrée dans le bloc d'origine ; vérifier sa mise à jour dans deux pages et ses permissions. Puis rétablir la valeur.
- **Alternative** : mentions de pages simples si le connecteur ne peut pas gérer les références.

## N08 — Bouton natif de page

- **Question** : comment réduire le nombre d'étapes entre intention et création ?
- **Usage** : Nouvelle tâche/note/projet, ouverture d'une page, confirmation.
- **Pré-vol** : lire les actions supportées dans l'interface **et** la capacité réelle de l'outil connecté. Un fetch qui affiche `<unknown alt="button"/>` n'expose pas automatiquement sa configuration.
- **Construire** : action explicite et base cible unique ; nom et icône correspondant à l'action.
- **Risque** : un bouton texte sans action, création dans une base dupliquée, mauvaise permission.
- **Test** : cliquer, inspecter la fiche produite, vérifier son ID unique et sa présence dans la vue de base ; distinguer `création` et `modification`.

## N09 — Base source unique

- **Question** : où résident les données durables ?
- **Usage** : tâches, notes, relations, projets, idées, ressources.
- **Construire** : propriétés minimales (titre, statut, catégorie, date si pertinente, liens/relations). Ajouter des vues liées au besoin.
- **À éviter** : dupliquer toute la base pour chaque page ou chaque statut.
- **Test** : modifier un item depuis une vue liée ; vérifier que la source initiale montre le même changement.
- **État vide** : mode d'emploi compact et saisie directe.

## N10 / N11 — Liste et table

- **Liste** : idéale pour prochaine action, sources récentes, lectures ; n'afficher que 3-5 propriétés pertinentes et filtrer.
- **Table** : pour édition, comparaison et audit de nombreuses propriétés ; réserver aux pages de domaine.
- **Configuration** : vue spécifique à une base centrale, tri et filtre définis, propriétés visibles ciblées.
- **État vide** : « aucune action correspondant au filtre » et lien vers vue générale ; ne pas transformer un filtre vide en affirmation que la base est vide.
- **Test** : 3 exemples datés, non datés, longs titres, toutes catégories et mobile.
- **Référence** : https://www.notion.com/help/views-filters-and-sorts

## N12 — Board

- **Question** : comment visualiser un pipeline par état ?
- **Usage** : candidatures, projets, production musicale.
- **Configuration** : groupe par statut réellement existant, éventuellement cacher groupes vides, propriétés de carte utiles.
- **Risque** : statuts incomplets ou cartes tellement denses qu'elles masquent les échéances.
- **Test** : déplacer ou changer une fiche de colonne ; vérifier son statut dans la source.

## N13 — Galerie

- **Question** : la reconnaissance visuelle fait-elle gagner du temps ?
- **Usage** : œuvres, produits, ressources illustrées.
- **Configuration** : choisir une propriété de couverture autorisée, format compact, nom/état visible.
- **À éviter** : galeries de 30 cartes textuelles sans images ; covers volées ou ambiguës.
- **Test** : 0 image, image portrait, image paysage, titre long, mobile.

## N14 / N15 — Calendrier et timeline

- **Calendrier** : date ponctuelle, publication, échéance.
- **Timeline** : durée et séquencement, projets multi-phases, selon plan et droits.
- **Risque** : items sans date invisibles ; garder une vue backlog/list pour eux.
- **Test** : item sans date, item passé, actuel, futur ; vérifier fuseau et date de début/fin.

## N16 — Formulaire Notion

- **Question** : quelle information est indispensable à l'entrée ?
- **Construire** : exposer les questions liées aux propriétés de la base (titre, type, domaine, contexte quand utiles). Faire la distinction entre obligatoire et facultatif.
- **Risque** : formulaire avec titre seul présenté comme classement complet ; bloquer une idée si elle n'a pas encore de date ou projet ; partage public non voulu.
- **Test** : remplir et soumettre, lire propriétés et contenu enregistrés dans la base centrale, vérifier confidentialité, doublon et affichage dans la bonne vue.
- **Référence** : https://www.notion.com/help/forms

## N17 — Bouton de base

- **Question** : comment automatiser une transition explicite ?
- **Usage** : marquer terminé, approuver, ouvrir une fiche, créer dans une base, mettre à jour des propriétés.
- **Construire** : choisir action disponible, cible et confirmation si changement sensible, vérifier droits et forfait.
- **Risque** : bouton qui modifie plusieurs fiches non ciblées, action payante sur forfait non compatible.
- **Test** : fiche factice identifiée ; action, avant/après, régression et retour arrière.
- **Référence** : https://www.notion.com/help/database-buttons

## N18 / N19 — Relations, agrégations et formules

- **Question** : comment calculer une donnée dérivée sans duplication ?
- **Usage** : tâche ↔ projet, œuvre ↔ inspiration, calendrier ↔ contenu.
- **Construire** : une relation bien nommée, formule/rollup seulement si sa signification est documentée.
- **Risques** : dénominateur nul, relation vide, formule cassée après renommage, valeur mise à jour de façon inattendue.
- **Test** : 0/1/plusieurs éléments liés, objet supprimé ou archivé, calcul manuel de comparaison.

## N20 — Mise en page de fiche de base

- **Question** : quelles propriétés doit-on voir en premier pour comprendre une fiche ?
- **Construire** : épingler les propriétés décisionnelles, réserver détails à l'info panneau ; vérifier la portée.
- **Limite essentielle** : la mise en page s'applique **à toutes les pages de la base**, pas à une seule vue.
- **Test** : ouvrir au moins deux fiches différentes sur desktop et mobile.
- **Référence** : https://www.notion.com/fr/help/layouts

## N21 — Graphiques

- **Question** : un indicateur aide-t-il réellement à choisir ?
- **Construire** : titre précis, agrégation expliquée, source de données visible, pas d'exemple fictif présenté comme réel.
- **Risques** : petit échantillon, zéro/valeurs manquantes, quotas ou plan, agrégation trompeuse.
- **Test** : reproduire calcul manuellement, changer une valeur test, confirmer l'actualisation.
- **Alternative** : tableau filtré + calcul natif lorsque le graphique n'est pas nécessaire.

## N22 — Dashboard view

- **Question** : faut-il une surface stable de plusieurs vues ?
- **Condition majeure** : d'après l'aide Notion consultée en novembre 2026, **Business/Enterprise**. Ce n'est pas un substitut universel au dashboard de page libre.
- **Configuration** : jusqu'à 12 widgets et 4 par rangée selon la documentation consultée ; vérifier la version avant utilisation.
- **Alternative** : blocs, colonnes et vues liées dans une page normale, plus souples mais moins structurés.
- **Test** : plan, permission, limite de widgets, mise à jour des filtres et mobile.
- **Référence** : https://www.notion.com/help/dashboards

## N23 — Embed externe

- **Question** : une information ou interaction ne peut-elle pas être rendue nativement ?
- **Exemples** : horloge, météo, site intégré.
- **Pré-vol** : disponibilité du site, confidentialité, consentement, permissions, performance, cohérence clair/sombre.
- **Risque** : contenu chargé depuis un tiers, bloc vide, publicité, site non compatible iframe.
- **Fallback** : lien texte explicite ou suppression du widget non essentiel.
- **Test** : chargement, espace occupé et comportement mobile.

## N24 — Média et fichiers

- **Question** : image/audio/PDF apporte-t-il une preuve ou un contexte utile ?
- **Configuration** : source réelle, texte alternatif/caption si possible, licence/permission, version, relations à la fiche.
- **Risque** : perte de provenance, URL temporaire expirée, fichier inaccessible sur mobile, divulgation.
- **Test** : ouvrir le fichier depuis compte autorisé et vérifier que la source d'origine reste consultable.

## Ordre de recette minimal pour chaque fiche

1. Inventorier propriété et source existantes.
2. Choisir le composant natif le plus simple.
3. Vérifier capacité API vs édition manuelle.
4. Configurer en test sans détruire.
5. Lire les propriétés sauvegardées.
6. Tester par clic/soumission lorsque nécessaire.
7. Vérifier mobile et droit d'accès.
8. Produire état `PASS`, `FAIL`, `NON TESTÉ` avec liens/observations.

**Aucune des recettes de ce document n'a été exécutée dans les templates d'origine.** Ce sont des protocoles prêts à utiliser.
