# -*- coding: utf8 -*-
from turtle import *

print("exercice de la tortue")


##https://docs.python.org/3.3/library/turtle.html
##forward(PAS)
##pendown()
##penup()
##right(DEGRES)
##left(DEGRES)
##color('red', 'yellow')

## utiliser speed(0) pour aller le plus rapidement possible

##********** Dessin avec la turtle niveau 1
##lettres et mot.  I L T          TILT

## Dessiner un rectangle creux
## Dessiner un rectangle plein
##* * * * * * *			* * * * * * *
##* * * * * * *			*           *
##* * * * * * *			*           *
##* * * * * * *			* * * * * * *

##Faire une procédure pour dessiner un triangles isocèle
##rectangle de hauteur h (exemple 5)
##* * * * * 
##* * * * 
##* * * 
##* * 
##*

##Faire deux procédures pour dessiner des triangles isocèles
##rectangle de hauteur h (exemple 5)
##* * * * * 
##  * * * * 
##    * * * 
##      * * 
##        * 
##de longueur l (exemple 9)
##* * * * * * * * * 
##  * * * * * * * 
##    * * * * * 
##      * * * 
##        * 

##Faire deux procédures qui dessinent un carré plein ou un carré creux
##(réutilisez votre travail).

##Dessiner un losange selon sa largeur (ici 6 ou 7 à gauche, 8 ou 9 à droite)
##   *         *
##  ***       ***
## *****     *****
##*******   *******
## *****   *********
##  ***     *******
##   *       *****
##            ***
##             *

## Dessiner un cercle selon son périmètre, en n'utilisant que forward et right

##BONUS : Dessiner un sapin (marron et vert ?)
##    exemple hauteur = 4
##      hauteur du pied et d'un bloc : 40
##      hauteur du sommet : 40
##      nombre de blocs : 4
##
##        *
##       ***
##      *****      dessinerBloc(XXXXX)
##     *******     largeur = 70
##       ***
##      *****
##     *******     dessinerBloc(XXXXX)
##    *********    largeur = 90
##      *****
##     *******
##    *********    dessinerBloc(XXXXX)
##   ***********   largeur = 110
##     *******
##    *********
##   ***********   dessinerBloc(XXXXX)
##  *************  largeur = 130
##      *****
##      *****      dessinerTronc(hauteur)
##      *****      largeur = 50 (ou vous pouvez prendre d'autres proportions)
##      *****

##    exemple hauteur = 3
##      hauteur du pied et d'un bloc : 30
##      hauteur du sommet : 30
##      nombre de blocs : 3
##
##        *
##       ***
##      *****      dessinerBloc(XXXXX)  largeur = 50
##       ***
##      *****
##     *******     dessinerBloc(XXXXX)  largeur = 70
##      *****
##     *******
##    *********    dessinerBloc(XXXXX) largeur = 90
##       *** 
##       ***       dessinerTronc(hauteur)
##       ***       largeur = 30

##    exemple hauteur = 2
##      hauteur du pied et d'un bloc : 20
##      hauteur du sommet : 20
##      nombre de blocs : 2
##
##        *
##       ***       dessinerBloc(XXXXX)  largeur = 30
##       ***
##      *****      dessinerBloc(XXXXX)  largeur = 50
##        *        dessinerTronc(hauteur) largeur = 10

def bougeLaTortuePourVerifierLeDessin():
    penup()
    forward(100)


bougeLaTortuePourVerifierLeDessin()
