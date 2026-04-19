sexo = input("Digite o seu sexo (M/F): ")
idade = int(input("Digite a sua idade: "))

sexo = sexo.lower()

if idade < 10 or idade > 65:
    valor = 0.50

elif idade <= 17:

    valor = 4.28

elif sexo == "f":

    valor = 5.50

else:

    valor = 8.25

print("Valor a pagar: R$", valor)