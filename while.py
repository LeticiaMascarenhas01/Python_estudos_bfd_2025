# WHILE = ENQUANTO
# testa todas as condições enquanto for verdade
# quando for falso o programa para de rodar

n = 1
while n != 0:
    n = int(input("Digite um número qualquer: "))
print("Isso é tudo pessoal!")

num = "S"
while num == "S":
    resposta = int(input("Digite um número: "))
    num = str(input("Deseja continuar? [S/N]")).upper()
print("Isso é tudo pessoal!")

numero = 1
while num >= 1000 or num <=100:
    resposta1 = int(input("Digite um número qualquer: "))
    print("Está correto! O número que vc falou é dentro do intervalo 100 e 1000")
