# programa que leia os numeros de 1 a 50
# e me de apenas aqueles que são pares

for num in range(2, 51, 2):
    if num % 2 == 0:
        print(num, end=" ")
    else:
        print("O número não é par!")
print("Isso é tudo pessoal!")

#de uma forma mais resumida e sem muita enrolação
for n in range(2, 51, 2):
    print(n,end=" ")
print("Acabou!")