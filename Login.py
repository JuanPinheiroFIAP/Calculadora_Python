#criar um menu com opções de (login, e cadastrar)

#caso o usuario ja tenha login realizar o login

#caso o usuario nao tenha fazer o cadastro 

#------------------------------------------------------------------------------------------------------------
escolha_cadastro = ""
users = []
print('''
[1] Login 
[2] Cadastro
''')
escolha_menu = int(input("Escolha uma opção: "))

#------------------------------------------------------------------------------------------------------------

while True:
    if escolha_menu == 1:
        n1 = input("Me informe o seu user: ")
        n2 = input("Me informe sua senha: ")

        for user, senha in users:
            if user == n1 and senha == n2:
                print(f"Seja bem vindo {n1}")
                user_encontrado = user_encontrado.upper(user_encontrado)
                break
        else:
            print("Usuario não encontrado!")
            escolha_cadastro = input("Desja realizar o cadastro? S/N")
            escolha_cadastro = escolha_cadastro.upper()


    if escolha_menu == 2 or escolha_cadastro =='S':
        print("Vamos realizar o seu cadastro!")
        user_novo = input("Digite um user novo:")
        print
        users.append(user_novo)
        for user, _ in users:
            if user_novo == user:
                print("Esse user já existe!")
                pass

            else:
                print("Otimo!")
                senha_nova = input("Digite sua senha nova: ")
                users.append(senha_nova)
                break

#------------------------------------------------------------------------------------------------------------