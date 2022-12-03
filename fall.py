t = float(input("entrer le temps (en seconde) de la chute persu: "))
s=0
t2 = t
for i in range(1000):
  h = float((9.81*(t2)**2)/2)
  t2 = t - (h/340)
  print(str(h) + " m")
