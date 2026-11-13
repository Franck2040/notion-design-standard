# Données, identité et preuve

## R08 — Relier les fiches sans dupliquer les données

- **Entrée/sortie.** Une source peut étayer plusieurs questions. Garder la fiche, le contenu, les fichiers et les versions d’origine. Noter l’ID canonique, les références à conserver et les ambiguïtés.
- **Interface.** Dans Sources, utiliser la relation Questions existante ou ajouter une propriété Relation pointant sur la bonne base. Vérifier si une relation réciproque est souhaitée. Sur une fiche QA, relier deux questions et ouvrir les vues correspondantes. Pour une reprise historique, établir la correspondance avant d’écrire et compléter uniquement les champs nécessaires. En cas de collision, isoler le cas sans fusion automatique.
- **REST / connecteur.** Lire les deux schémas, récupérer les vrais IDs de fiche et mettre à jour les relations de page existantes avec [PATCH /v1/pages](https://developers.notion.com/reference/patch-page) ou l’outil de mise à jour. Pour un champ relation, conserver et fusionner l’ensemble des IDs déjà présents quand la mutation remplace la valeur. Vérifier que la connexion accède aussi à la base liée. Pour une relation longue, lire la [propriété de page paginée](https://developers.notion.com/reference/retrieve-a-page-property) avant toute réécriture. Ne pas recréer un contenu pour imiter son historique.
- **Droits / forfait.** Vérifier modification du schéma si nécessaire, édition des fiches à reprendre et accès à la cible. La disponibilité et la profondeur de l’historique dépendent de l’espace et du forfait. Ne pas promettre de transférer un historique de versions par copie.
- **Test / retrait.** Avant/après : vérifier le même ID, les deux relations, contenu, pièces jointes et liens d’un échantillon identifié. Si l’historique complet est dans le périmètre, l’échantillon ne valide pas tout le corpus : compter les sources, établir le rapprochement complet et lister les exceptions. Restaurer les relations depuis le journal si nécessaire, sans supprimer les originaux.
- **Repli.** Mention vers la fiche originale et liste de cas à qualifier si la relation n’est pas possible. Pas de nouvelle source de vérité.

## R09 — Donner une identité visuelle sans faux interrupteur

- **Entrée/sortie.** Un accent pour l’orientation ou l’ambiance, un texte pour chaque état et des icônes au sens stable. Une commande de navigation ne doit pas ressembler à une suppression.
- **Interface.** Choisir les icônes natives disponibles et leurs couleurs dans le sélecteur des pages et composants. Appliquer un accent local à un titre, un callout ou une couverture. Ne pas substituer un emoji à une icône indisponible dans le cadre du standard : utiliser alors un libellé clair.
- **REST / connecteur.** Utiliser seulement les formats d’icône et couleurs prévus pour l’objet concerné. Lire [Emoji and icon](https://developers.notion.com/reference/emoji-and-icon) et le schéma de l’outil. Une modification d’icône de page ne modifie pas une icône de bouton et ne crée pas un thème global. Ne promettre aucune commande globale sans mécanisme documenté et testé.
- **Droits / forfait.** Édition des pages ou vues concernées et droit d’utiliser les médias. Aucun forfait ne doit être supposé débloquer une recoloration globale. Les changements de page sont partagés avec ses lecteurs, contrairement au thème clair/sombre de l’interface.
- **Test / retrait.** Vérifier lisibilité en clair et sombre, titre et icône sur téléphone, signification sans couleur, et recadrage de la couverture. Consigner ce qui a réellement été retouché et ses valeurs d’origine.
- **Repli.** Utiliser des variantes locales documentées, un libellé textuel et les réglages d’apparence personnels de Notion sans prétendre qu’ils recolorent l’espace.

## Journal de recette

Remplir une ligne par essai, y compris les échecs. Dans un dépôt public, remplacer les IDs privés, URLs, personnes, captures et contenus par des références synthétiques. Garder les preuves originales dans un espace privé autorisé.

| Champ | Valeur à renseigner |
| --- | --- |
| Contexte | Recette, date, forfait, canal/version, appareil et rôle |
| Cible | Page hôte, vue, source, fiche QA et état avant action |
| Déclenchement | Geste réellement joué, résultat attendu, résultat observé et état après |
| Preuve | Référence à une capture, enregistrement ou lecture de la fiche persistée ; utiliser les deux pour un bouton |
| Résultat | `PASS`, `FAIL`, `NON TESTÉ` ou `BLOQUÉ` avec motif, pour chaque test |
| Reprise | Correctif, risque résiduel, valeur initiale ou objet QA à retirer |

**Cas complet à rejouer — Capture du cockpit** : placer le bouton R01, ouvrir la vue R04, cliquer comme utilisateur final, créer une fiche avec un titre unique « TEST QA — capture », compléter Type et Domaine, relire la fiche, retrouver le même ID via la vue, recommencer sur téléphone et supprimer uniquement les entrées QA après vérification. Un rendu statique, une création directe par API et un clic sur un simple lien ne sont pas le même test. Si le clic natif ou le téléphone n’a pas été utilisé, l’écrire explicitement.
