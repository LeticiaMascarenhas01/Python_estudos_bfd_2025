#programa que pergunta a quantidade em kms percorridas por um carro alugado
#e a quantidade de dias pelos quais foi alugado
#calcule o preço a pagar
#sabendo que o carro custa r$60/dia e r$0.15 por km rodado

quilometros_pecorridos = float(input("Quantos KMs foram percorridos?"))
dias = int(input("Quantos dias de aluguel? "))
preco = (dias * 60) + (quilometros_pecorridos * 0.15)
print("Como foram percorridos {} KMs em {} dias de aluguel, o valor final fica por R$ {}".format(quilometros_pecorridos,dias,preco))