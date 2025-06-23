from time import sleep
def atribuicao_variavel():
    val1 = float(input('Digite o primeiro valor: '))
    val2 = float(input('Digite o segundo valor: '))
    return val1, val2
def soma():
    val1, val2 = atribuicao_variavel()
    return val1 + val2
def subtracao():
    val1, val2 = atribuicao_variavel()
    return val1 - val2
def multiplicacao():
    val1, val2 = atribuicao_variavel()
    return val1 * val2
def divisao():
    val1, val2 = atribuicao_variavel()
    if val2 == 0:
        print("Divisão por zero não é permitida.")
    else:
        return val1 / val2

def main():
    while True:
        sleep(1)
        print('-='*15)
        print('Bem-vindo a calculadora!')
        print('-='*15)
        print('Escolha uma operação:')
        print(''' \n 1. Soma \n 2. Subtração \n 3. Multiplicação \n 4. Divisão \n 5. Sair \n''')
        print('-='*15)
        opcao = int(input('Digite o número da operação: '))
        if opcao not in [1, 2, 3, 4, 5]:
            print('-='*15)
            print('Opção inválida. Tente novamente.')
            continue
        if opcao == 1:
            resultado = soma()
            print('-='*15)
            print(f'Resultado da soma: {resultado}')
        elif opcao == 2:
            resultado = subtracao()
            print('-='*15)
            print(f'Resultado da subtração: {resultado}')
        elif opcao == 3:
            resultado = multiplicacao()
            if resultado == 0:
                print('-='*15)
                print("Multiplicação por zero não é permitida.")
            else:
                print('-='*15)
                print(f'Resultado da multiplicação: {resultado}')
        elif opcao == 4:
            resultado = divisao()
            if resultado == 0:
                print('-='*15)
                print("Divisão por zero não é permitida.")
            else:
                print('-='*15)
                print(f'Resultado da divisão: {resultado}')
        elif opcao == 5:
            print('-='*15)
            print('Saindo da calculadora. Até logo!')
            print('-='*15)
            break
print(main())