# LAÇO DE REPETIÇÃO PARA QUANDO SABEMOS EXATAMENTE QUANTAS VEZES REPETIR ALGO

for star in range(0,10, 2): # Bom se iniciar em 0 para dar exatamente a contagem q desejo
    print("Star")

numero = int(input("Digite um numero inteiro qualquer: "))
for n in range(0, numero+1):
    print(n)

inicio = int(input("Digite o numero inicial: "))
final = int(input("Digite o numero final: "))
passo = int(input("Digite de quanto em quanto: "))
for c in range(inicio,final+1, passo):
    print(c)