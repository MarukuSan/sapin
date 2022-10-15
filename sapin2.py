#Calcule le nombre d'étoile à la base du sapin
def etoiles(n):
    if (n == 1):
        return (4, 7)
    else:
        a = etoiles(n-1)[0] + 1
        b = (etoiles(n-1)[1] - 2) + 2*(a-1)
        return (a, b)

#Dessine le sapin
def sapin(n):
    espace = int(etoiles(n)[1]/2)
    e = espace - 2
    etoile = 1
    niveau = 1
    ligne = 4
    count = 1
    
    while (niveau <= n):
        while (count <= ligne):
            print((espace*' ')+('*'*etoile))
            count += 1
            espace -= 1
            etoile += 2
        niveau += 1
        count = 1
        ligne += 1
        etoile -= 4
        espace += 2

    #Affiche les pieds du sapin
    while (count <= 5):
        count += 1
        print(e*' ' + 5*'|')


#Maruku2105