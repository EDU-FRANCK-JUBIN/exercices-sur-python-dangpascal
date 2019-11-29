def minMaxMoy(liste):
    resultat = []
    minimum = min(liste)
    maximum = max(liste)

    somme = 0
    for i in range(0, len(liste)):
        somme = somme + liste[i]
    moyenne = somme / len(liste)
    resultat.append(minimum)
    resultat.append(maximum)
    resultat.append(moyenne)
    print(resultat)
    print("Le minimum de la liste est " + str(resultat[0]))
    print("Le maximum de la liste est " + str(resultat[1]))
    print("La moyenne de la liste est " + str(resultat[2]))


liste = [10, 18, 14, 20, 12, 16]
minMaxMoy(liste)
