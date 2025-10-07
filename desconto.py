# programa que pede o valor de um produto
# e me de o novo valor desse produto com 5% de desconto

preco = float(input("Valor do produto: "))
print("Atualmente seu produto custa R$ {}".format(preco))
desconto = preco - (preco * 5/100)
print("O valor do seu produto com o desconto é igual a {}".format(desconto))