n = 0
while n <= 1:
    n = int(input("Entrez un nombre strictement supérieur à 1: "))

i = 2
fin_boucle = n / 2
nombre_diviseurs = 0
diviseur = []

while i <= fin_boucle:
    if n % i == 0:
        nombre_diviseurs = i + 1
        diviseur.append(i)
    i = i + 1

if nombre_diviseurs == 0:
    print("Le nombre " + str(n) + "n'a pas de diviseur")
else:
    print("La liste des diviseurs de " + str(n) + " est " + str(diviseur[0:len(diviseur)]))
