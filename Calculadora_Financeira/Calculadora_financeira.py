def soma_despesas():
    total = 0
    for item in Listagem:
        total += item[1]
    return total

def exibir_despesas():
        for item in Listagem:
            print(f"{item[0]}: R${item[1]:.2f}")


Listagem = []
print('-' * 40)
print(f"{'Bem-vindo à Calculadora Financeira!':^40}")
print('-' * 40)
while True:
    despesas = str(input("Escreva a Despesa (Ex: Aluguel, Luz, Internet): "))
    valor = float(input("Escreva o Valor da Despesa: R$"))
    print('-' * 40)
    Listagem.append((despesas, valor))
    print("Despesa adicionada com sucesso!")
    print('-' * 40)
    result= soma_despesas()
    exibir = exibir_despesas
    print('Deseja adicionar mais alguma Despesa?')
    opção = str(input("Digite Sim ou Não: ")).upper().strip()[0]
    if opção == 's' :
        print("Continuando a adição de despesas...")
        print('-' * 40)
    elif opção == 'N':
        print("Finalizando a adição de despesas...")
        print('-' * 40)
        exibir_despesas()
        print('-' * 40)
        print(f"{'Resumo das Despesas':}")
        print(f"O resultado final é de R${result:.2f}")
        print('-' * 40)
        print("Obrigado por usar a Calculadora Financeira")
        break
    elif opção !='S' and opção != 'N':
        print("Opção inválida! Por favor, digite Sim ou Não.")
        opcao = str(input("Digite Sim ou Não: ")).upper().strip()[0]
        print('-' * 40)
