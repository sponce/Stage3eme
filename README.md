Visualization des traces des particules jusqu'au calorimetre dans phoenix
=========================================================================

Etape 0 : Basics
----------------

### LHCb

*   comprendre le fonctionnement du detecteur -> visite du Pt8
*   comprendre les bases de la reconstruction

### Linux

*   boot sur clef USB
*   bases : menus, shell, systeme de fichiers

Etape 1 : Phoenix & json data
-----------------------------

*   visualisation des donnees LHCb [https://hepsoftwarefoundation.org/phoenix/](https://hepsoftwarefoundation.org/phoenix/)
*   fichier de donnees evenement ouvrir LHCbEventDataV2Small.json, essayer de comprendre la structure
*   syntaxe json [https://stph.scenari-community.org/bdd/nos1/co/json02.html](https://stph.scenari-community.org/bdd/nos1/co/json02.html)
*   syntaxe phoenix [https://github.com/HSF/phoenix/blob/master/guides/users.md#using-phoenix-with-your-own-data](https://github.com/HSF/phoenix/blob/master/guides/users.md#using-phoenix-with-your-own-data)
*   modification manuelle de donnees pour voir l'effet Ajouter un point a une des traces, verifier que la visualisation fonctionne

Etape 2 : utilisation de python pour explorer les fichiers json
---------------------------------------------------------------

*   installation du logiciel thonny, un environnement de developpement python pour debutants
    *   sudo apt-get install thonny
*   bases du langage python : syntaxe, boucles, fonctions
    *   [https://www.youtube.com/watch?v=VmOPhT4HFNE](https://www.youtube.com/watch?v=VmOPhT4HFNE)
    *   utiliser thonny
*   lire un fichier json en python, en extraire des donnees et les afficher exercice extrapolateExercise.py

Etape 3 : un peu de math
------------------------

*   extrapolation lineaire a partir de 2 points en z = 20000
    *   on calcule les pentes en x et y par rapport a z
    *   on extrapole dx et dy pour le nouveau point, en se basant sur la pente et le nouveau dz
    *   on calcule le nouveau point
*   a faire manuellement dans un premier temps (sur papier)
    *   et essayer d'ajouter un point extrapole a l'une des trace pour verifier les calcul

Etape 4 : extrapolation en python
---------------------------------

*   refaire l'exercice consistant a extrapoler une trace en python
    *   exercise extrapolateExercise.py
    *   verifier qu'on retrouve ce qu'on avait trouve a la main

Etape 5 : mise en commun
------------------------

*   exercice extendToCalo.py
    *   boucler sur les evenement du fichier json
    *   boucler sur les traces de chaque evenement
    *   extraire les 2 derniers points
    *   extrapoler grace a la fonction ecrite a l'etape 4
    *   ajouter le nouveau point a la fin de la trace
    *   sauvegarder
*   verifier le resultat dans Phoenix

\- Bonus - Mandelbrot set, comparison python/C++
================================================

Etape 0 : Definition of Mandelbrot set
--------------------------------------

### Nombres complexes

*   Un nombre sous la forme "z = a + i b" ou a et b sont des nombres reels
*   L'addition est definie par z1+z2 = a1+a2 + i (b1+b2)
*   La multiplication est definie par z1 \* z2 = a1\*a2 - b1\*b2 + i (a1\*b2+a2\*b1)
*   Cela revient a dire que i\*i = -1, d'ou le nom de partie "imaginaire"

### Suite Zn et divergence

*   On considere on nombre complexe quelconque c
*   On pose Z0 = 0 puis pour tout n : Zn+1 = Zn^2 + c
*   On dit que lq "suite" Zn diverge si quand n augmente, Zn finit par devenir extremement grand. Pour l'ensemble de mandelbrot on va considerer qu'on diverge si An^2+Bn^2 > 4 quand on ecrit Zn sous la forme Zn = An + iBn

### Ensemble de Mandelbrot et representation

*   On designe les points du plan par le nombre complexe correspondant a leurs coordonnees. Par exemple, c = x + iy est le complexe associe au point de coordonnees x,y
*   Pour chaque point de coordonnee c, on definit la suite Zn et on teste sa divergence
*   L'ensemble de mandelbrot est l'ensemble des points pour lesquels Zn ne diverge pas
*   Pour les points ou la suite diverge, on utilise un code couleur pour montrer la "vitesse" de divergence

Etape 1 : Calcul de l'ensemble de mandelbrot en python
------------------------------------------------------

### Calcul de la divergence de Zn

*   On va d'abord ecrire une fonction qui prend un complexe Cr + i Ci et test la divergence de la suite Zn.
*   La methode sera definie comme suit

def mandel(cr, ci):

*   Elle fera 100 iterations de Zn et retournera le premier n pour lequel on depasse 4, comme vu ci-dessus, ou -1 si on ne depasse pas 4 au bout de 100 iterations
*   Le fichier mandelExercise.py donne les bases de cette fonction

### Dessin de l'ensemble

*   la librairie matplotlib de python permet de creer une image a partir d'un tableau de chiffres a 2 dimensions, c'est a dire une liste de listes
*   Cette liste comprend une liste par ligne qui elles-meme comprennent une valeur par point de la ligne.
*   Ces valeurs sont calculees en utilisant la methode mandel definie precedemment
*   Ecrire un programme prepare ce tableau pour une portion de plan entre minx/maxx = -2/0.5 et miny/maxy = -1.0/1.0
*   
