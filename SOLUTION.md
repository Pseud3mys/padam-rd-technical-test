Ma connaissance en graphes s'arrêtait à Dijkstra, aux parcours en largeur et à A*. Ce fut donc mon point de départ dans les recherches.

Je savais aussi qu’il faut que les sommets aient un degré pair pour permettre de relier toutes les arêtes d’un graphe de façon optimale (au maximum un passage par arête).

En effet, intuitivement, on voit qu’un sommet de degré impair ne peut pas être relié à un autre sommet de degré impair sans repasser par une arête déjà parcourue.

Après avoir implémenté une fonction de test simple, on voit que le graphe "hard to choose" est déjà eulérien (tous les sommets ont un degré pair), que "islands" n’a que des sommets impairs, et enfin que le graphe de Paris contient un mélange des deux, avec un grand nombre de sommets et d’arêtes (ce qui posera un problème de complexité).

Après quelques recherches, j’ai trouvé que l’algorithme pour trouver une solution optimale dans un graphe eulérien est l’algorithme de Hierholzer. De plus, il a une complexité linéaire en nombre de sommets + nombre d’arêtes. Ce qui est parfait et fonctionne même pour la carte de Paris.

J’ai implémenté cet algorithme pour le graphe "hard to choose", et ça fonctionne. Je trouve:

- Length of path found: 596 (/596 arêtes)
- Value of path found: 1200.0

La solution optimale pour le graphe "hard to choose" est la suivante :
![Solution optimal islands.png](img%2FSolution%20optimal%20islands.png)


Vient ensuite le problème des graph non eulérien, où il faut relier les sommets impairs entre eux pour rendre le graphe eulérien. (On ajoute des arêtes "imaginaires" qui sont en fait des chemins existants sur les sommets du graphe général.)

Le but est de trouver le couplage parfait de ces sommets pour minimiser le poids additionnel rajouté par ces doublons (car sans cela, chaque arête était parcourue une seule fois).

J’ai ensuite implémenté l’algorithme de Floyd-Warshall pour trouver les plus courts chemins entre tous les sommets du graphe. Le problème est qu’il fonctionne en O(n³), ce qui prend trop de temps à s'exécuter sur mon PC pour le graphe de Paris.

J’ai donc cherché des heuristiques. En me concentrant sur le cas de Paris.

J’ai donc implémenté deux optimisations dans l’algo de base :

 - Premièrement, au lieu d’essayer chaque paire de sommets du graphe, je ne boucle que sur les sommets impairs. (complexité temporelle par 4 sur le graphe de Paris.)

- Ensuite, au lieu de chercher n’importe quel sommet à intercaler entre deux sommets impairs, je limite la recherche dans un rayon à vol d’oiseau de 0.05 (en degrés).
Il y a deux défauts à ça :

  - S’il y a un sommet impair isolé dans ce rayon, il ne sera pas relié.
  - Ce n’est pas forcément la solution optimale puisque distance sur le graphe ≠ distance à vol d’oiseau.

Après avoir implémenté cela, le code tourne beaucoup plus vite, mais reste un peu long pour Paris (si on considère qu’une durée "raisonnable" est de quelques minutes).

Du coup, j’ai utilisé l’algorithme de Dijkstra que j’avais implémenté au début. Je me suis dit qu’une complexité en O(n log n) exécutée pour les sommets impaires serait meilleure.
Je voulais calculer Dijkstra pour chaque sommet, prendre la distance la plus petite au global, associer les sommets, puis recommencer…

Mais c’était toujours trop long… Manquant de temps pour tenir dans les 2/3 heures imparties, je suis allé au plus simple avec une heuristique encore plus légère :
au lieu de calculer Dijkstra, je calcule juste la distance à vol d’oiseau entre les sommets (c'est là où je me concentre sur la topologie du réseau de Paris, et non sur celui d’"islands", car sur "islands", la distance 2D n’a pas vraiment de sens. D'autant que pour Island ). 

La complexité est en O(1), donc cette fois je trouve une solution en 2/3 minutes.

Voici les graphes obtenus :


Les points rouges sont les sommets impairs ; les lignes sont les arêtes rajoutées pour les relier entre eux. On voit que la solution est pas mal, mais qu’il y a quelques aberrations (problème classique des heuristiques gloutonnes non globales : à la fin, il faut bien relier les sommets restants, même s’ils sont très éloignés).

![sommet impaire heurisitque Paris.png](img%2Fsommet%20impaire%20heurisitque%20Paris.png)

Pour "island.txt". Cette solution a moins de logique : la distance sur le graphe ne dépend pas du tout de la distance réelle. Deux sommets très proches à vol d’oiseau peuvent avoir un poids de 4, ce qui est le poids maximum sur ce graphe.

![paire pour Islande.png](img%2Fpaire%20pour%20Islande.png)

L’implémentation de base de Floyd-Warshall permettait de calculer ces paires de façon optimale, mais je suis arrivé à court de temps avant de pouvoir tracer un graphe des paires avec cette fonction. Je me suis concentré sur avoir un code qui donne une solution OK pour tous les graphes.

À ce stade, j’ai dû passer environ 2h30 sur le projet, en deux temps. Je n’ai donc pas eu le temps de combiner les couples de sommets impairs pour créer un nouveau graphe et appliquer Hierholzer dessus. Mais toutes les briques sont en place pour le faire.

J’ai passé environ 1h de plus à rédiger ce rapport. Mes notes de réflexion brutes sont dans "solution raw.md" (attention aux yeux niveau orthographe…).
J’utilise PyCharm avec des fonctions d’autocomplétion efficaces, donc pas mal de commentaires et de définitions de fonctions sont écrits par l’IA. C’est aussi le cas des fonctions de plot plot_vertexes et plot_edges. J'ai cru comprendre que ce n'était pas la qualité de rédaction du code qui était evalué, il est un peu chaotique, mais il suffit de modifier un peu le main pour retrouver mes résultats.