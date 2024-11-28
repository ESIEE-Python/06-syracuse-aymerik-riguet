"""La fonction suivante permet de realiser la suite de syracuse sur des listes"""
#### Fonctions secondaires


# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """fonction qui permet d'afficher un graphe de l'évolution de la liste en parametre"""
    title = "Syracuse" + " (n = " + str(lsyr[0]) + ")"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = [ list(range(len(lsyr))) ]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """
    # votre code ici

    l = [n]
    while n !=1 :
        if n%2 == 0 :
            n = n//2
        else :
            n = n*3 +1
        l.append(n)
    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """
    # votre code ici
    tv = 0
    for elt in l:
        if elt == 1:
            tv = l.index(elt) + 1
    return tv

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """

    # votre code ici
    l0 = l[0]
    tva = 0
    access = True
    for elt in l:
        if l0 > elt and access is True:
            tva = l.index(elt)
            access = False
    return tva


def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """
    # votre code ici
    return max(l)


#### Fonction principale


def main():
    """Fonction qui test les différentes fonction crées"""
    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    #syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))

if __name__ == "__main__":
    main()
