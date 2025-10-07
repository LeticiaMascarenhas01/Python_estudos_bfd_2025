distancia = float(input("Quantos quilometros deseja viajar? "))
if distancia <= 200:
    valor = distancia * 0.50
    print("Você fará ma viajem de {} KMs que custará R$ {:.2f}.".format(distancia, valor))
else:
    valor = distancia * 0.45
    print("Você fará ma viajem de {} KMs que custará R$ {:.2f}.".format(distancia, valor))
print("Ótima viagem!")

#de forma mais resumida, "bem escrita"
distancia2 = float(input("Quantos quilometros deseja viajar? "))
print("Você fará ma viajem de {} KMs".format(distancia2))
preco = distancia2 * 0.80 if distancia2 <= 200 else distancia2 * 0.75
print("Sua viagem de {}KMs custará R${:.2f}.".format(distancia2, preco))