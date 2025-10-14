# programa que lê o sexo da pessoa em F ou M
# e me dê a palavra correspondente

sexo = str(input("Qual seu sexo? [F, M ]")).strip().upper()

while sexo != "F" and sexo != "M":
    print("Alternativa inexistente, tente novamente.")
    sexo = str(input("Qual seu sexo? [F, M ]")).strip().upper()

if sexo == "F":
    print("Seu sexo é o FEMININO!")
else:
    print("Você é do sexo MASCULINO!")
print("Tchau Mundo")