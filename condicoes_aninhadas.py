nome = str(input("Digite seu primeiro nome: "))
if nome.lower() == "Samara":
    print("Nome mais lindo do mundo!")
elif nome.lower() == "Mariaa" or nome.lower() == "João" or nome.lower() == "José":
    print("Seu nome é comum no Brasil")
else:
    print("Nome bastante normal")
print("Isso foi tudo pessoal")

# nome.lower() transforma tudo em minúsculo, então tanto “Letícia” quanto “LETÍCIA”
# ou “letícia” serão aceitos.