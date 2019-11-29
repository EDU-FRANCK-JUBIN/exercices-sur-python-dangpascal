X = ["a", "b", "c", "d"]
Y = ["s", "b", "d"]


def test_appartenance(liste, caractere):
    test = False
    for i in range(0, len(liste)):
        if liste[i] == caractere:
            test = True
            break
    if test:
        print("Le caractère " + str(caractere) + " appartient à la liste " + str(liste))
    else:
        print("Le caractère " + str(caractere) + " n'appartient pas à la liste " + str(liste))


print("Affichage des ensembles X et Y\n")
print(X)
print(Y)
print("\n")
test_appartenance(X, "c")
test_appartenance(Y, "a")
