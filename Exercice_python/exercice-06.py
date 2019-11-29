liste_chiffre_romain = ["M", "CM", "D", "CD", "C", "XC", "L", "VL",
                        "XL", "X", "IX", "V", "IV", "I"]
liste_chiffre_arabe = [1000, 900, 500, 400, 100, 90, 50, 45, 40, 10, 9, 5, 4, 1]


def conversion(nombre):
    reste = nombre
    nombre_romain = ''
    for i in range(0, len(liste_chiffre_arabe)):
        while reste >= liste_chiffre_arabe[i]:
            nombre_romain = nombre_romain + liste_chiffre_romain[i]
            reste = reste - liste_chiffre_arabe[i]
    return print(nombre_romain)


n = 0
while n < 1 or n > 3999:
    n = int(input("Entrez un nombre entre 1 et 3999: "))

conversion(n)
