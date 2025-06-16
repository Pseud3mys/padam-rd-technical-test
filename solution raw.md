Qlq chose à faire avec Jikstra ? Mais c'est juste entre 2 sommets...

l'algorithme de Floyd-Warshall par contre ca relit tous les sommets.

C'est pas exactement le problème du voyageur de commerce, car on peut passer plus d'une fois par sommet. "problème du postier chinois" ?
Ca permet de résoudre des graph qui n'ont pas de chemin eulerien (ie. qui ont un sommet avec un degré impaire, auquels cas il faut passer obligatoirement 2 fois sur ce sommet).

C'est un problème connu avec une solution optimal en O(n^3). c'est juste ca ? Ah oui mais l'optimium à l'air galère en 2h.

Sinon on pourrait implémenter un algorithme genetique.. On n'aurait pas la solution optimal mais ca pourrait être un bon entre-deux avec une complexité inférieur à O(n^3).

DUCOUP... le principe de l'algo c'est de rendre le graph Eulerien enfaite.. et pour ca on applique l'algorithme de Floyd-Warshall.

En gros: 
"hard to choose" est un graph eulerien
"islands" est un graph avec que des sommets de degré impaires
et la map de paris est le cas difficile (bcp de sommets)


Floyd-Warshall c'est l'evolution de Dijkstra. Il calcul le plus court chemin entre tous les sommets d'un graph orienté. Alors que Dijkstra ne le fait que pour un sommet de départ.

----
J'ai fait une première implémentation pour le postier chinois. D'après Wikipedia:

"Dans le cas général, il y a toujours un nombre pair de sommets de degré impair. La solution optimale peut être obtenue par l'algorithme suivant[2] :

- Former un nouveau graphe G’, constitué uniquement des sommets de degré impair dans le graphe initial G.
- Entre deux sommets de G’, ajouter une arête dont la longueur est celle du plus court chemin entre les deux sommets dans G.
- Trouver un couplage parfait de poids minimum dans G’, ce qu'on peut calculer avec un algorithme de complexité O(n3).
- Pour chaque paire de sommets u et v couplés dans G’, ajouter au graphe initial G les arêtes du plus court chemin de u à v.
"

L'idée c'est que le cas des sommets paires est simple à régler... On veut savoir comment combiner les sommets impaires. (graphe non Eulerien).
Le jeu est simple, on applique Floyd-Warshall pour tous les sommets impaires.
Ensuite vient le problème de couplage entre les sommets impaires. Comment rajouter les meilleurs arc pour optimiser le cout de la solution ?

C'est cette partie là qui est difficile. Ma première implementation etait de faire de la force brute avec chaque paire de sommets... Mais c'est m^me pas la peine d'y penser pour la carte de Paris par exemple.

J'ai implémenter Floyd-Warshall mais sur Paris ca ne tourne pas bien (ca mouline trop longtemps). il faudrait couper le problème en petit sous problème (=sous graph) avec des heuristiques, genre sur les quartiers et tt ca).

A ce moment ca fait environ 1h15 que je suis dessus... Va falloir choisir une implémentation.

Faut trouver un moyen d'associer les sommets impaires entre eux pour minimiser le coût total.
Mais il en moins de n3.. parce que ca ne fonctionne pas pour Paris sinon..