#concertar

import math
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
hipotenuza = math.hypot(cateto_oposto,cateto_adjacente)
print("A hipotenuza é igual a {}.".format(hipotenuza))