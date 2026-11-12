# 8 composants composites — contrats d'assemblage

> Ce sont des compositions de **plusieurs fonctions natives**. Elles ne sont pas un bloc Notion spécial et doivent être implémentées et testées.

| ID | Assemblage minimal | Contrat de données | Test d'acceptation |
| --- | --- | --- | --- |
| C01 Capture + tri | Bouton/formulaire + base Inbox + liste « à traiter » | Titre, date, domaine/type facultatifs selon flux | Soumettre puis retrouver dans l'Inbox |
| C02 Priorités et retard | Tâches + vues distinctes : du jour, en retard, attente, prochaines | Dates, statut, éventuellement priorité | Quatre cas de dates et statuts |
| C03 Portfolio d'œuvres | Galerie œuvres + relation inspirations + page de création | ID œuvre, étape, média, version, provenance | Une inspiration visible sur sa fiche |
| C04 Navigation partagée | Mentions de pages + bloc synchronisé | Pages existantes et droits d'accès | Changer une entrée puis voir les deux pages |
| C05 Knowledge avec provenance | Index + source d'origine + statut de revue | Source, catégorie, date, révision | Retrouver l'original depuis la fiche |
| C06 Projet et actions | Base projet + relation tâches + vues filtrées | Projet ID, tâche ID, statut | Modifier une tâche depuis 2 vues sans copie |
| C07 Calendrier et backlog | Calendrier daté + liste sans date | Date nullable, statut, nom | Un item sans date reste accessible |
| C08 KPI vérifiable | Calcul/formule + vue source | Formule, périmètre, données | Valeur recalculée à la main |

## Fiche obligatoire avant de construire

```text
Composant composite :
Question utilisateur :
Source(s) de vérité et propriétés :
Action déclencheuse :
État visible initial :
États alternatifs : vide / erreur / sans permission / volume élevé
Règles de filtrage :
Limite de plan ou de connecteur :
Vérification structurelle :
Vérification réelle par interaction :
Preuve de non-duplication :
Résultat : CONFIGURÉ / TESTÉ / BLOQUÉ / NON TESTÉ
```

### Exemple C01 — Capture d'une note

- Base unique `Inbox` avec `Titre`, `Domaine`, `Type`, `Contenu`, `Création`, `État`.
- Le formulaire peut demander titre et contexte, et proposer domaine/type si le besoin le requiert. En capture ultra-rapide, il peut être préférable de rendre les métadonnées **facultatives**, puis classer en revue.
- Après soumission, l'élément doit être retrouvé dans Inbox puis dans la vue non classée. Si une automatisation vers une base de connaissances existe, elle doit être testée ; sinon, ne pas prétendre qu'une migration automatique est en place.
- Tests : titre long, sans domaine, avec lien, deux soumissions, mobile.

### Exemple C02 — Tâches

- Définir le sens de « aujourd'hui » : date prévue, date limite, ou les deux. Ne pas inclure systématiquement les retards sans mention explicite.
- Les états `Terminé` ou `Annulé` doivent être exclus des vues de travail quand cela a été décidé ; le nom réel des statuts appartient à la base.
- `En retard` = échéance strictement passée et statut ouvert, en excluant les dates absentes.
- `En attente` = statut explicitement « En attente », indépendamment de la date.
- Trois tâches fictives suffisent à tester certaines frontières ; varier également date absente et fuseau.

### Exemple C04 — Navigation

- Les pages cibles doivent avoir des icônes natives cohérentes. La mention ne doit pas afficher un caractère emoji décoratif avant la destination.
- Le bloc synchronisé évite le désalignement, mais peut être inaccessible si le lecteur n'a pas les droits sur la source.
- Le menu ne doit pas couvrir toute la hauteur mobile ; les actions principales doivent rester atteignables rapidement.
