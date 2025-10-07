#SEM USO DE LAÇO DE REPETIÇÃO, USANDO APENAS MATEMÁTICA

num = int(input("Digite um numero: "))
u = num // 1 % 10  # 1834 // 1 = 1834, depois 1834 % 10 = 4  ---  % 10 → pega o último dígito
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print("Analisando o numero {}".format(num))
print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))