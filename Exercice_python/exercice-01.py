import math


def volume_cone():
    rayon = int(input("Entrer le rayon du cône:\n"))
    hauteur = int(input("Entrer la hauteur du cône:\n"))
    volume = (math.pi * rayon ** 2 * hauteur) / 3
    return print("Le volume du cône est " + str(volume) + " cm3")


volume_cone()
