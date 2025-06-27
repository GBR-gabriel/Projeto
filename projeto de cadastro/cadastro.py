def cadastro():
    # Cadastro de app ou site
    lista_de_usuario = {}
    dominios = ['@hotmail.com', '@outlook.com', '@gmail.com', '@yahoo.com']
    while True:
        try:
            print('==' * 24)
            print(f'{'Seja Bem Vindo a loja':^48}')
            print(f'{'Crie seu cadastro, para esta efetuando o login':^48}')
            print('==' * 24)
            nome = str(input('Digite seu nome: ')).upper()
            sobrenome = str(input('Digite seu sobrenome: ')).upper()
            idade = int(input('Digite sua idade: '))
            email = str(input('Digite seu email: ')).lower()
            while True:
                if not any(dominio in email for dominio in dominios):
                    print('email esta errado, por favor digite novamente')
                    email = str(input('Digite seu email: ')).lower
                else:
                    break
            while True:
                cpf = str(input('Digite seu CPF: '))
                if len(cpf) != 10 + 1:
                    print('Erro no CPF, digite novamente')
                else:
                    break
            senha = str(input('Crie sua senha, ela deve conter no minimo 7 caracters.\nDigite sua senha: '))
            while True:
                if len(senha) != 7:
                    print('Erro no senha, digite novamente')
                    senha = str(input('Digite sua senha: '))
                else:
                    break
            lista_de_usuario.update(
                {'nome': nome, 'sobrenome': sobrenome, 'idade': idade, 'email': email, 'cpf': cpf, 'senha': senha})
            print('Cadastro concluido com sucesso!')

            break
        except ValueError or TypeError or IndexError:
            print('O cadastro sera reiniado, por favor digite novamente!')
    return lista_de_usuario

#login da pagina
def login(lista_de_usuario):
    print('==' * 24)
    print(f'{'Seja Bem Vindo a loja':^48}')
    print(f'{'Efetue o login para continuar':^48}')
    print('==' * 24)
    while True:
        email = str(input('Digite seu email: '))
        senha = str(input('Digite sua senha: '))
        if email == lista_de_usuario['email'] and senha == lista_de_usuario['senha']:
            print('Login efetuado com sucesso!')
            break
        else:
            print('Email ou senha incorretos, tente novamente.')
    return True

print(login(cadastro()))
