# Étape 04 — Recherche contextualisée avant tout design Notion

**Statut : méthode réutilisable, pas étude terrain déjà effectuée.** Un agent qui consulte uniquement des pages et des templates n'a pas « interviewé les utilisateurs ». Ce guide sépare recherche documentaire, observation réelle, hypothèses et faits vérifiés.

## But

Découvrir les tâches, utilisateurs, données, contraintes, erreurs coûteuses et habitudes réelles **avant** de choisir navigation, couleurs, composants, bases et vues. Le contexte métier guide le design sans imposer de stéréotypes : une association peut avoir besoin d'une console dense et un ingénieur peut avoir besoin d'un studio éditorial.

### Fondements consultés

- [NN/g — Contextual inquiry](https://www.nngroup.com/articles/contextual-inquiry/) : observer le travail dans son environnement et interpréter avec les utilisateurs ; contexte, partenariat, interprétation, focus.
- [NN/g — Field studies](https://www.nngroup.com/articles/field-studies/) : questions d'étude, participants, lieux, moments et méthodes d'observation.
- [Google Design Sprint](https://designsprintkit.withgoogle.com/methodology) : Understand → Define → Sketch → Decide → Prototype → Validate.
- [Notion — vues, tris et filtres](https://www.notion.com/help/views-filters-and-sorts) : les vues sont des configurations d'une même source, non de nouvelles bases.
- [Notion — database settings](https://www.notion.com/help/customize-your-database) : les changements de schéma concernent la base entière, certains réglages de vue sont locaux.
- [Notion — layouts](https://www.notion.com/en-gb/help/layouts) : la mise en page de fiche s'applique à toutes les pages de la base, pas à une seule vue.

La recherche ne consiste pas à recopier des modèles populaires. Elle permet de comprendre **pourquoi un composant est justifié et quand il ne l'est pas**.

## 0. Pré-vol de recherche (obligatoire)

Avant toute affirmation sur les utilisateurs :

1. Inventorier ce qui existe : page d'accueil, bases sources, propriétés, relations, formules, permissions, vues, automatisations, notes libres, historique et fichiers.
2. Définir quelles sources sont réellement accessibles : workspace, documents, entretiens, captures, test sur mobile. Lire sans modifier.
3. Étiqueter la preuve : **OBSERVÉ DIRECTEMENT**, **DÉCLARÉ PAR L'UTILISATEUR**, **DOCUMENT OFFICIEL**, **AVIS ISOLÉ**, **HYPOTHÈSE**. Ne jamais remplacer ces catégories par une certitude générale.
4. Ne pas exporter d'informations privées ou de modèles propriétaires vers un dépôt public.
5. Identifier les inconnues bloquantes ; ne demander que les questions dont la réponse change une décision majeure. Si l'utilisateur a déjà fourni les réponses, les réutiliser.
6. Déclarer immédiatement toute incapacité à inspecter les boutons ou à tester sur téléphone. Un export avec des blocs inconnus n'autorise pas à affirmer leurs actions.

## 1. Définir les objets de recherche

| Objet | Questions | Résultat attendu |
| --- | --- | --- |
| Population | Qui travaille, qui consulte, qui administre, quel niveau Notion ? | Rôles, permissions, scénarios |
| Activités | Quelles 5 actions reviennent réellement et à quel moment ? | Fréquence, séquence, déclencheur |
| Décisions | Que doit-on savoir sur le premier écran ? | Question prioritaire, critères de décision |
| Données | Quels objets, sources, documents, volumes et relations ? | Inventaire sans doublon |
| Contexte | Desktop, mobile, terrain, faible réseau, interruption ? | Contraintes de capture et lecture |
| Erreurs | Quel oubli ou statut faux aurait un coût ? | Risques, garde-fous |
| Esthétique | Quels exemples plaisent, déplaisent, et pourquoi ? | Attributs observables plutôt que « joli » |
| Maintenance | Qui classera, archivera, mettra à jour ? | Coût réaliste et responsables |

**JTBD** : « Lorsque [situation réelle], je veux [action], afin de [résultat] ». Le JTBD est une synthèse de l'observation, pas un cliché inventé.

## 2. Choisir la méthode selon le niveau de preuve

| Méthode | Autorisée quand | Apprend quoi | N'apprend PAS |
| --- | --- | --- | --- |
| Audit du workspace | Connexion en lecture | Structure réelle, sources et volumes | Ce que les gens préfèrent visuellement |
| Analyse d'une session enregistrée | Consentement et preuve fournie | Parcours, frictions observables | Taux d'échec de tous les utilisateurs |
| Entretien contextuel | Utilisateur disponible | Motivations et arbitrages décrits | Comportement réellement observé |
| Observation de tâche | Consentement et session réelle | Séquence, détours, interruptions | Popularité d'un style dans le marché |
| Test de prototype | Prototype présent et exécuté | Faisabilité et frictions de ce prototype | Attractivité générale à long terme |
| Recherche documentaire | Documentation publique vérifiable | Capacités de Notion et normes UX | Préférences propres au propriétaire |
| Avis communautaires | Sources datées et contexte | Signaux et hypothèses de problèmes | Statistiques représentatives |

Les entretiens et observations ne doivent jamais être inventés par l'agent. Sur une petite mission, **audit + hypothèses explicitement marquées + test rapide** peut suffire ; sur un système critique, rechercher une validation plus solide.

## 3. Protocole d'entretien / observation (si possible)

Ne pas demander seulement « Quel design préférez-vous ? » ; demander des **situations vécues** :

1. Montre-moi la dernière fois où tu as eu besoin d'ajouter ou retrouver cette information.
2. Qu'est-ce qui a déclenché l'action ? Quel appareil utilisais-tu ?
3. Quelles trois informations devais-tu comparer ?
4. À quel moment as-tu quitté Notion ou contourné le système ?
5. Quelle erreur ou perte de temps veux-tu absolument éviter ?
6. Montre-moi un écran que tu apprécies : **quels éléments précis** rendent la tâche plus simple ou agréable ?
7. Que serait-il raisonnable de saisir au moment de la capture, et qu'est-ce qui peut attendre ?
8. Qui aura accès à ces données et qui les maintiendra ?

Observer la tâche si l'utilisateur le souhaite ; lui laisser expliquer ses propres détours. Distinguer citation exacte, paraphrase et interprétation de l'enquêteur. Respecter confidentialité et consentement.

## 4. Analyse du flux d'information

Pour les 5 actions principales, documenter **déclencheur → entrée → décision → action → feedback → stockage → récupération**. Exemple fictif :

| Étape | Candidature (exemple fictif) |
| --- | --- |
| Déclencheur | Une offre intéressante est trouvée |
| Entrée | Entreprise, poste, source, date |
| Décision | Candidater ou enregistrer pour plus tard |
| Action | Créer une candidature dans une seule base |
| Feedback | Statut « À préparer » et fiche créée |
| Stockage | Base Candidatures, lien vers l'offre |
| Récupération | Vue « À relancer » calculée depuis la même base |

Ne pas inventer une automatisation de relance : si elle n'existe pas, écrire « vue filtrée, vérification manuelle ».

## 5. Matrice des contraintes

- **Notion** : forfait, intégrations, permissions, fonctions natives, différences entre bouton bloc et bouton de base.
- **Mobile** : ordre des colonnes après reflow, largeur des tableaux, accès à l'ajout, taille des médias.
- **Données** : provenance, migrations, versions, archivage, échantillon de qualité, confidentialité.
- **Charge** : temps de maintenance, volume d'éléments, nombre de clics, dépendance aux widgets.
- **Esthétique** : iconographie native, palette sémantique, contraste, densité, langue, droits sur les images.
- **Organisation** : propriétaire, éditeurs, lecteurs, changements simultanés, historique.

### Faille bloquante

Si un agent ne peut pas vérifier la configuration d'un bouton, il doit **l'annoncer avant de promettre le flux**, et noter : `CONFIGURATION INCONNUE`, `TEST D'INTERACTION REQUIS`.

## 6. Livrables de recherche

1. Une fiche synthétique de contexte (qui, pourquoi, quand, où, appareil, confidentialité).
2. Inventaire des sources existantes et statut de conservation, avec liens **dans l'espace privé**, pas dans le dépôt public.
3. Les 5 jobs-to-be-done hiérarchisés et leurs preuves.
4. Une carte des flux et frictions.
5. Une liste de contraintes, inconnues et hypothèses falsifiables.
6. Un brief de conception prêt pour l'[étape 05](../divergence-selection/README.md), **sans layout ni palette décidés d'avance**.

Voir [fiche structurée](research-brief-template.md) et [cas de démonstration](examples.md).
