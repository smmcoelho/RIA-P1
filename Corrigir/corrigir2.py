
def soma(a, b):
    return a + b

def subtraccao(a, b):
    return b - a

def multiplicacao(a, b):
    return b * b

def divisao(a, b):
    return a / b

def menu() -> int:
    print("1 - Adicionar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair do programa.")
    i = int(input('Introduza uma operacao: '))
    return i

def menuAdicionarProduto():
    a = int(input('Insira um numero: '))
    b = input('Insira outro numero: ')
    return a, b

if __name__ == '__main__':
    r = 0
    while r < 4:
        opcao = menu()
        a, b = menuAdicionarProduto()
        if opcao == 1:
            r = soma(a, b)
        elif opcao == 2:
            r = subtraccao(a, b)
        elif opcao == 3:
            r = multiplicacao(a, b)
        elif opcao == 4:
            pass
        elif opcao == 5:
            print('Sair do programa')
            break

        print(f"o resultado da operacao 'e : {r}")
