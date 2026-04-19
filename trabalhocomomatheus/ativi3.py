
num = int(input("escolha um numero"))

num2 = int(input("escolha outro numero"))

print("1)soma de 2 numero")

print("2)diferença entre 2 numeros")

print("3) produto entre 2 numero")

print("4)divisao entre 2 numero")

prince = input("digite o numero da opçao escolhida")

if  prince == "1":
    result = num + num2
    print("seu resultado",result)

elif prince == "2":
    result = num > num2
    print("seu resultado",result)

elif prince == "3":
    result = num * num2
    print("seu resultado",result)

elif prince == "4":
    if num2 != 0:
        result = num / num2
        print("seu Resultado:", result)
    else:
        print("nao e possivel dividir por zero")

else:
    print("Opcao invalida")





