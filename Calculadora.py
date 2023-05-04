import math
print("Sejá bem vindo a minha calculadora!")
print("Vamos calcular!")
print("Ok vamos lá!")
while True:
    print('''
            [1] - Adição
            [2] - Subtração
            [3] - Divisão
            [4] - Multiplicação
            [5] - Exit''')
    menu = input("Qual a opção que você quer escolher? ")

    if menu in ('1', '2' , '3' , '4'):
        num1 = int(input("digite seu primeiro número: "))
        num2 = int(input("digite seu segundo número: "))

    elif menu in '5':
        print("Tchau!")
        break

    match menu:
        case '1':
            resultado = num1 + num2
            print(f"O resultado da sua adição foi {resultado}")
        case '2':
            resultado = num1 - num2
            print(f"O resultado da sua subtração foi {resultado}")
        case '3':
            if num2 != 0:
                 print("Não é possivel fazer uma divisão por zero")
            else:
                resultado = num1 / num2
                print(f"O resultado da sua divisão foi de {resultado}")
        case '4':
            resultado = num1 * num2
            print(f"O resultado da sua multiplicação foi de {resultado}")
        case _:
            print("Opção invalida!")