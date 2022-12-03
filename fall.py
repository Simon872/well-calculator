from math import *
# initialisation des valeurs
t = float(input("Entrez le temps (en seconde) de la chute chronomètré: "))
  # partie 1 (calcule)
g = 9.81
v = 340.0
  # partie 2 (boucle)
s=0
t2 = t

# clacule de le hauteur du puit
h_calcule1 = ((v**2)/(2*g))*(-1+sqrt(1+2*g*t/v))**2
print("\nla valeur calculer de la profondeur du puits est " + str(h_calcule1) + " m")

# approximation de la hauteur du puis par une boucle
print("\nles valeurs approchées par boucle sont:")
for i in range(45):
  h = (9.81*(t2)**2)/2
  t2 = t - (h/340)
  print(str(h) + " m")