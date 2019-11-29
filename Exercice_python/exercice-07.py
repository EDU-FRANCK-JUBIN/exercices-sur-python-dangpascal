def maFonction(borneInf, borneSup, nbPas):
    tableau=[]
    tableau.append(["x","y"])
    for i in range(borneInf, borneSup, nbPas):
        resultat = 2 * i ** 3 + i - 5
        tableau.append([i,resultat])

    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            print(tableau[i][j], end=' ')
        print()

maFonction(0, 10, 1)

