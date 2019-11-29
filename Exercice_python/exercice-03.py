from math import factorial

n = 0
while n <= 50:
    n = int(input("Entrez un nombre strictement supérieur à 50: "))

valeur_exacte = 2.7182812845904523536
valeur_approchee = 0
tableau = []

for i in range(0, n+1):
    valeur_approchee = valeur_approchee+(1/factorial(i))

tableau.append(valeur_approchee)
tableau.append(abs(valeur_approchee - valeur_exacte))
print(tableau[0:2])