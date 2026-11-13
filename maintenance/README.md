# Étape 10 — Apprendre et maintenir le référentiel

Le standard change quand une preuve change une décision, pas parce qu’un nouveau composant paraît séduisant. Ce dispositif tourne à chaque contribution et lors des revues déclenchées ci-dessous. **Aucune veille planifiée ni aucun benchmark exécuté ne sont revendiqués.**

## Du signal à la règle

| Étape | Action et preuve minimale |
| --- | --- |
| 1. Signaler | Décrire l’observation et sa source : incident, changement d’interface/API/forfait, retour utilisateur ou résultat d’essai. Noter version, environnement, rôle et date. Anonymiser avant publication. |
| 2. Trier | Reproduire si possible. Marquer `CONFIRMÉ`, `À REPRODUIRE` ou `NON REPRODUIT`. Priorité : perte/exposition de données, parcours cassé, friction répétée, puis confort. Un avis isolé n’est pas un benchmark. |
| 3. Corriger | Chercher la règle canonique. Préférer corriger ou supprimer une règle plutôt qu’en ajouter une presque identique. Examiner les liens atlas, recettes, manifest et mobile. |
| 4. Comparer | Jouer la même tâche, les mêmes données et le même rôle avant/après. Si Notion ou l’environnement a changé entre les deux, noter le biais et ne pas calculer de gain certain. |
| 5. Publier | Ajouter une entrée au registre, la modification et les preuves ou limites. Indiquer le repli et le statut. Une règle non vérifiée peut rester proposée, pas être présentée comme certifiée. |
| 6. Réviser | Consulter [Notion Releases](https://www.notion.com/releases), [changelog API](https://developers.notion.com/page/changelog), [permissions](https://www.notion.com/help/sharing-and-permissions) et les docs liées. Réexaminer après incident, changement de version/forfait, signal répété ou avant un nouveau déploiement. |

## Contrat pour toute nouvelle règle

Renseigner le **motif**, un **exemple**, un **contre-exemple** et une **vérification falsifiable**. Ajouter ID, portée, preuve, propriétaire de revue et lien canonique. Le [registre JSON](rules.json) fournit quatre entrées de départ. Utiliser `proposed`, `active`, `deprecated` ou `retired`. Lorsqu’une règle vieillit, ajouter la raison et le remplacement ou le repli. Ne pas modifier son ID pour cacher l’historique.

## Benchmark minimum à rejouer

| Scénario | Résultat attendu | À mesurer si possible |
| --- | --- | --- |
| B01 — Capture mobile | La donnée persiste une seule fois et revient dans la file | Étapes, temps, doublons |
| B02 — Bouton de base | Seule la fiche cliquée change | Nombre de fiches modifiées, erreurs de droits |
| B03 — File volumineuse | Objet pertinent trouvé sans ouvrir la table exhaustive | Volume, étapes, temps, échecs |
| B04 — Lecture et permissions | L’utilisateur autorisé revient à sa liste; le lecteur non autorisé n’accède pas à la source | Résultats par rôle, points de friction |

Utiliser le [modèle de revue](review-template.md), marquer `NON TESTÉ` pour toute case non jouée et ne jamais confondre succès documentaire, test natif et résultat utilisateur. Ne publier que des données synthétiques ou anonymisées.

## Vérification automatique du dépôt

Exécuter `python3 scripts/check_standard.py` à la racine avant de livrer. Le contrôle valide les règles et leurs liens, l’inventaire des composants et la présence/structure des planches. Il ne déclenche pas de test Notion ni de veille externe. Une [issue de revue](../.github/ISSUE_TEMPLATE/standard-feedback.md) sert à recueillir les signaux en public sans exporter des informations privées.
