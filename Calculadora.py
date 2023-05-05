import math
from os import system, name
from time import sleep

#-----------------------------------------------------------------------------------------------------------------

def clean():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')

#-----------------------------------------------------------------------------------------------------------------

print("Sejá bem vindo a minha calculadora!")
print("Vamos calcular!")
print("Ok vamos lá!")

#-----------------------------------------------------------------------------------------------------------------

while True:
    print("----"*20)
    print('''
            [1] - Adição
            [2] - Subtração
            [3] - Divisão
            [4] - Multiplicação
            [5] - Função
            [6] - Exit''')
    print()
    print("----"*20)
    menu = input("Qual a opção que você quer escolher? ")

#-----------------------------------------------------------------------------------------------------------------

    if menu in ('1', '2' , '3' , '4',):
        print("----"*20)
        num1 = int(input("digite seu primeiro número: "))
        num2 = int(input("digite seu segundo número: "))
        print("----"*20)

    elif menu in '6':
        print("----"*20)
        print()
        print("Até mais!")
        print(9
        )
        print("----"*20)
        break
    
#-----------------------------------------------------------------------------------------------------------------

    match menu:
        case '1':
            resultado = num1 + num2
            print("----"*20)
            print(f"O resultado da sua adição foi {resultado}")
            print("----"*20)
            sleep(3)
            clean()
            
        case '2':
            resultado = num1 - num2
            print("----"*20)
            print(f"O resultado da sua subtração foi {resultado}")
            print("----"*20)
            sleep(3)
            clean()

        case '3':
            if num2 != 0:
                 print("Não é possivel fazer uma divisão por zero")
                 sleep(3)
                 clean()
            else:
                resultado = num1 / num2
                print("----"*20)
                print(f"O resultado da sua divisão foi de {resultado}")
                print("----"*20)
                sleep(3)
                clean()

        case '4':
            resultado = num1 * num2
            print("----"*20)
            print(f"O resultado da sua multiplicação foi de {resultado}")
            print("----"*20)
            sleep(3)
            clean()

        case '5':
            print("Vamos calcular sua função do segundo grau!")
            a = int(input('Qual é o valor do seu "a"? '))
            b = int(input('Qual é o valor do seu "b"?'))
            c = int(input('Qual é o valor do seu "c"?'))
            delta = (b**2)-(4*a*c)

            if delta < 0:
                print("Não será possivel calcular quando o delta for negativo")
                exit()
                sleep(3)
                clean()

            else :
                x=math.sqrt(delta)
                x1=(-b+x)/(2*a)
                x2=(-b-x)/(2*a)
                print("----"*20)
                print(f"O valor do seu x1 é ==>{x1}") 
                print(f"O valor do seu x2 é ==>{x2}")
                print("----"*20)
                sleep(3)
                clean()
        case _:
            print("Opção invalida!")
            sleep(2)
            clean()

#-----------------------------------------------------------------------------------------------------------------