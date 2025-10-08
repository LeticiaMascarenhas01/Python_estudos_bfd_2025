num = int(input("Digite um número inteiro: "))
print('''Escolha uma das bases para conversão:
[1] Binário
[2] OCTAL  
[3] HEXADECIMAL''')


# BINÁRIO (base 2): usa apenas 0 e 1. É a linguagem dos computadores.
#   Ex: 5 → 101, 10 → 1010
# OCTAL (base 8): usa os dígitos de 0 a 7. Cada dígito = 3 bits binários.
#   Ex: 8 → 10, 64 → 100
# HEXADECIMAL (base 16): usa 0–9 e A–F (A=10, F=15). Muito usada em cores e endereços de memória.

escolha = int(input("Digite sua escolha: "))
if escolha == 1:
    print("{} convertido em BINÁRIO é igual a {}".format(num, bin(num)[2:]))
elif escolha == 2:
    print("{} convertido em OCTAL é igual a {}".format(num, oct(num)[2:]))
elif escolha == 3:
    print("{} convertido em HEXADECIMAL é igual a {}".format(num, hex(num)[2:]))
else:
    print("Opção inválida, tente ovamente!")