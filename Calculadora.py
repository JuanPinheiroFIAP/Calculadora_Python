import math
from os import system, name
from time import sleep

def bhaskara():
    raiz = math.sqrt(delta)
    print(raiz)
    result = -b + delta 2* a * c

def função(a,b,c):
    return(b*b - 4*a*c)


def clean():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')

print("Sejá bem vindo a minha calculadora!")
print("Vamos calcular!")
print("Ok vamos lá!")
while True:
    print('''
            [1] - Adição
            [2] - Subtração
            [3] - Divisão
            [4] - Multiplicação
            [5] - Funções
            [6] - Exit''')
    menu = input("Qual a opção que você quer escolher? ")

    if menu in ('1', '2' , '3' , '4',):
        num1 = int(input("digite seu primeiro número: "))
        num2 = int(input("digite seu segundo número: "))

    elif menu in '6':
        print("Tchau!")
        break

    match menu:
        case '1':
            resultado = num1 + num2
            print(f"O resultado da sua adição foi {resultado}")
            sleep(3)
            clean()
        case '2':
            resultado = num1 - num2
            print(f"O resultado da sua subtração foi {resultado}")
            sleep(3)
            clean()
        case '3':
            if num2 != 0:
                 print("Não é possivel fazer uma divisão por zero")
                 sleep(3)
                 clean()
            else:
                resultado = num1 / num2
                print(f"O resultado da sua divisão foi de {resultado}")
                sleep(3)
                clean()
        case '4':
            resultado = num1 * num2
            print(f"O resultado da sua multiplicação foi de {resultado}")
            sleep(3)
            clean()
        case '5':
            print('''
            Funções:
            [1] - Primeiro Grau
            [2] - Segundo Grau
            ''')
            escolha = input('Qual função você quer calcular?')

            if escolha == '1':
                a = int(input('Qual é o valor do seu "a"? '))
                b = int(input('Qual é o valor do seu "b"?'))

                delta = b*b - 4*a
                print(delta)

            elif escolha == "2":
                a = int(input('Qual é o valor do seu "a"? '))
                b = int(input('Qual é o valor do seu "b"?'))
                c = int(input('Qual é o valor do seu "c"?'))
                delta = função(a,b,c)



        case _:
            print("Opção invalida!")
            sleep(3)
            clean()