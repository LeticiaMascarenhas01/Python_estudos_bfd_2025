#crie um programa que leia o nome de uma cidade
#e diga se ela começa com o nome "santo" ou não

cidade = str(input("Digite o nome da cidade: ")).strip() #tira os espaços da resposta
print(cidade[:5].upper() == "Santo") #upper() serve para o programa não fzr diferença se a etra tá mauiscula ou minuscula