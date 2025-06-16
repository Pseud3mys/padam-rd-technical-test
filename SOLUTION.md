Qlq chose à faire avec Jikstra ? Mais c'est juste entre 2 sommets...

l'algorithme de Floyd-Warshall par contre ca relit tous les sommets, mais c'est pour un grpah orienté...

Il suffirait de doubler chaque arête pour passer de non orienté à orienté. Mais est ce que c'est encore optimal ?

C'est pas exactement le problème du voyageur de commerce, car on peut passer plus d'une fois par sommet. "problème du postier chinois" ?
Ca permet de résoudre des graph qui n'ont pas de chemin eulerien (ie. qui ont un sommet avec un degré impaire, auquels cas il faut passer obligatoirement 2 fois sur ce sommet).

C'est un problème connu avec une solution optimal en O(n^3). c'est juste ca ??

Sinon on pourrait implémenter un algorithme genetique.. On n'aurait pas la solution optimal mais ca pourrait être un bon entre-deux avec une complexité inférieur à O(n^3).