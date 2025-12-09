# programa que leia dois vlores e mostre um menu (presente no vídeo
# EXERCICIO PYTHON #059 - CIRANDO UM MENU DE OPÇÕES
# o programa deverá realizar a operação solicitada em cada caso

n1 = int(input("Digite um número: "))
n2 = int(input("Digite o segundo número: "))

opcao = 0
while opcao != 5:
    print('''    [1] SOMA
    [2] MULTIPLICAÇÃO
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    opcao = int(input("Digite a opção que deseja: "))
    if opcao == 1:
        soma = n1 + n2
        print("A soma de {} e {} resulta em {}".format(n1,n2,soma))
    elif opcao == 2:
        multiplicacao = n1 * n2
        print("O produto de {} e {} resulta em {}".format(n1,n2,multiplicacao))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
        print("Entre {} e {} o maior é o {}".format(n1,n2,maior ))
    elif opcao == 4:
        print("Digite novamente os números:")
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite os segundo número: "))
    elif opcao == 5:
        print("Finalizamos")
    else:
        print("Opção, inválida, tente novamente")
print("Fim do programa")


