# 02 — Études des références : six templates examinés

> Audit des versions accessibles le 10 novembre 2026. Les produits peuvent changer, et les liens peuvent devenir inaccessibles. Les comptes rendus ci-dessous décrivent **les structures observées** et non une licence de reproduction.

## Méthode de lecture d'un template

Pour chaque produit : (1) quel problème est résolu ; (2) quelle est sa première action ; (3) quelles bases soutiennent la page ; (4) comment les vues évitent le scroll ; (5) comment les relations et automatisations fonctionnent ; (6) où l'interface échoue ; (7) ce qu'on peut transférer légalement et techniquement.

## A. Second Brain (PARA Method)

[Référence Notion](https://app.notion.com/p/73d97ee22290838d8cfa818e109b57e5)

**Structure observée**
- Colonnes environ 19 % / 81 %.
- À gauche : Quick Action (plusieurs boutons), Navigation vers Projects & Tasks, Resources & Notes, Finance Tracker, Areas, Habit Tracker et Daily Journal ; accès Backend.
- À droite : Life Areas, Projects Manager, Tasks To-Do, Resources.
- Plus bas : habitudes, journal quotidien et notes.
- Le Backend conserve les sources Project, Tasks Manager, Notes, Resources, Finance Tracker, Areas, Habit Tracker, Journal.

**Pourquoi le design fonctionne** : l'utilisateur reconnaît l'emplacement de chaque famille, la navigation possède une présence spatiale, les icônes aident à scanner, les données opérationnelles restent à droite.

**Problème potentiel** : trop de vues détaillées empilées → une grande page. Le modèle PARA n'oblige pas à afficher toute la collection sur l'accueil.

**Transfert** : rail court + domaine actif + bases communes, pas duplication de l'ensemble.

## B. Second Brain — navigation synchronisée

[Référence Notion](https://app.notion.com/p/6e297ee222908283a7f781af755daca3)

**Structure observée**
- 25 % / 75 % : navigation à gauche, zone active à droite.
- Le menu de gauche est un **bloc synchronisé** : Home, Inbox, Tasks, Projects, Areas, Resources, Notes, Archive, Database.
- Sous les liens : Topics, Notebooks, Habit tracker.
- La zone droite contient Inbox, Areas, Tasks, Resources et Notes avec vues liées.
- Les sous-pages reproduisent la même navigation via références au bloc synchronisé.

**Pourquoi c'est fort** : l'utilisateur peut revenir au même « panneau de contrôle » depuis plusieurs pages. La structure paraît plus proche d'une application que d'une pile de sous-pages.

**Limites** : la sidebar simulée est une colonne Notion, pas un véritable composant sticky CSS ; elle peut descendre ou se réorganiser sur mobile. Le contenu reste soumis au layout de Notion.

**Transfert** : navigation répétée via bloc synchronisé vers les destinations essentielles, vue active à droite, possibilité de réduire les listes secondaires.

## C. My Task Tracker

[Référence Notion](https://app.notion.com/p/0e097ee2229083b19df10149d2089efc)

**Structure observée**
- Documentation de démarrage détaillée dans un callout repliable.
- Bandeau de quatre zones : Quick Nav, Due today, Overdue, Done this week.
- Vue My Tasks avec onglets Today / Inbox.
- Matrice de priorités : Do now / Schedule / Clear it fast / Someday.
- Section Momentum.
- Source unique Tasks avec propriétés : Task, Due Date, Completed On, Status, Parent/Sub-item, Area, Repeat, Urgent, Important, Energy, Days Left (formula), Priority (formula), boutons Do today et Tomorrow.
- Des automatismes de complétion, répétition et revue sont **décrits par le template**.

**Ce qu'il faut comprendre** : la priorité ne résulte pas d'une couleur saisie arbitrairement ; elle découle de Urgent/Important. Les tâches sans date résident dans Inbox. Certaines valeurs exactes (ex. `Done`, `Daily`) sont utilisées par les formules ou automatismes.

**Défauts à surveiller** : une tâche récurrente marquée Done deux fois peut dupliquer une occurrence (signalé dans le guide). Les automatisations peuvent dépendre de l'abonnement ou du compte. Une matrice complète sur l'accueil peut allonger la page.

**Transfert** : un bandeau d'indicateurs + 1 vue de tâches + changement de priorité explicite + historique fidèle ; documenter les valeurs de statut essentielles.

## D. My Habit Tracker

[Référence Notion](https://app.notion.com/p/e0697ee2229083dcb86b0161a736fbdb)

**Structure observée**
- Documentation extensive : usage quotidien, propriétés, conseils, manipulation des habitudes.
- Zone « Keep the Streak Going ».
- Trois cartes statistiques : Habits Completed Today, Highest Current Streak, Best Streak Ever.
- Graphique Consistency, puis table Habit Overview.
- Sources distinctes Habits et Daily Entries.
- La documentation indique qu'un clic « Done today » crée une entrée et actualise le streak, mais **un double clic peut produire un doublon**.

**Pourquoi la séparation des bases aide** : « une habitude » est une définition durable ; « une entrée quotidienne » est un événement daté. Cette distinction rend l'historique exploitable.

**Limites** : compter « jours consécutifs » peut devenir une source de pression ; mieux vaut une présentation respectueuse qui ne dramatise pas les pauses. Une grosse zone statistique n'est pas forcément indispensable au cockpit général.

**Transfert** : un simple module facultatif, suivi avec historique, correction des doublons, choix de la métrique pertinente.

## E. Content Calendar for Social Media

[Référence Notion](https://app.notion.com/p/ee997ee222908391ac38816f706e97be)

**Structure observée**
- Actions : nouvelle idée, nouveau post, prompt, campagne.
- Quick Nav vers Brands & Strategy, Platforms, Campaigns, Content, Prompt Library.
- Indicateur This Week's Goals, zone Needs Attention.
- Content Plan en **onglets** : Active, Calendar, Pipeline, Grid, Ideas.
- Campaign Timeline ; Performance en trois graphiques, Top Posts.
- Guide expliquant la structure, les propriétés, les automatismes, la suppression des exemples et les limites des plans.

**Point clé** : une idée devient un contenu planifié sans créer une deuxième base « publications ». Le même élément change de statut et de vue. La zone Needs Attention montre les anomalies plutôt que le volume total.

**Risque** : afficher tous les graphiques, le pipeline et le calendrier sur une page d'accueil globale serait trop long. Dans un espace « Studio contenu », ces éléments peuvent être utiles.

**Transfert** : bouton de capture + file « à traiter » + onglets adaptés au domaine ; guide « ce que le système fait automatiquement ».

## F. Project Management

[Référence Notion](https://app.notion.com/p/fb497ee222908313a62a81f982ca65b3)

**Structure observée**
- Page racine minimaliste : Dashboard, Projects, Tasks.
- Dashboard : My Tasks, Active Projects, Timeline ; colonne latérale Status Breakdown et Load Per Person.
- Deux bases reliées (Projects, Tasks), plusieurs vues spécialisées.

**Leçon** : l'analyse des projets doit montrer l'avancement et les tâches qui bloquent, pas seulement les noms de projets. Un outil destiné à une personne seule n'a pas besoin d'un indicateur « charge par personne ».

**Transfert** : relier projets, tâches, dates, responsables uniquement si nécessaire ; des KPI d'équipe n'ont pas de valeur dans un système individuel.

## G. Références visuelles et vidéos

- Collection : [75 Aesthetic Notion Templates](https://silviauralia.notion.site/75-Aesthetic-Notion-Templates-02e3b82e419a47ada685c283fbdb268a).
- Créateur : [George Vlasyev — Resources](https://vlasyev.com/resources).
- Vidéos étudiées via les transcriptions transmises : comment faire un dashboard Notion esthétique ; techniques de bases de données et boutons ; hiérarchie, couvertures et widgets ; enseignements de vente de templates.
- Images de référence : white/sage life hub, second brain sombre, planificateur d'études, dashboard à métriques.

### Ce qu'il faut extraire visuellement

- White/sage : chaleur, rythme, espaces aérés, palette restreinte ; risque de décor trop vertical.
- Dark Second Brain : iconographie et sidebar utiles, **pas obligation d'adopter le sombre**.
- Études : vrai planning et actions visibles ; attention aux énormes calendriers.
- Dashboard SaaS : hiérarchie des KPI, contrastes, actions à proximité ; Notion ne permet pas tout le CSS, le sticky sidebar et les modales personnalisées.

## H. Avis utilisateurs et preuve

Des avis publics peuvent confirmer une perception de simplicité et d'utilité ; ils ne prouvent pas la rentabilité, le revenu, la rétention ni la qualité technique. Éviter de conclure sur des commentaires que l'on n'a pas consultés, et dater toute note ou métrique susceptible de changer.

**Question à poser à chaque référence** : que permet-elle de faire en 30 secondes ? que perd-on en supprimant la moitié des widgets ? comment elle aide un nouvel utilisateur sans tutoriel d'une heure ?
