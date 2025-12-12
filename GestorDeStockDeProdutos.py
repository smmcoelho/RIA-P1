def PrintVerde(input):
    print(f"\033[92m {input} \033[00m")

def PrintCinzento(input):
    print(f"\033[94m {input} \033[00m")

def PrintVermelho(input):
    print(f"\033[31m {input} \033[00m")

# Adicionar um novo aluno e nota.
def adicionarProduto(d : dict, nome: str, quantidade: int, preco: float) -> None:
    d[nome] = {'q': quantidade, 'p': preco}

# Atualizar a nota de um aluno existente.
def atualizarQuantidade(d: dict, nome: str, quantidade: int) -> None:
    if nome in d:
        preco = d[nome]['p']
        d[nome] = {'q': quantidade, 'p': preco}
    else:
        PrintVermelho(f"Produto {nome} nao existe")

def atualizarPreco(d: dict, nome: str, preco: float) -> None:
    if nome in d:
        quantidade = d[nome]['q']
        d[nome] = {'q': quantidade, 'p': preco}
    else:
        PrintVermelho(f"Produto {nome} nao existe")


def exibirProdutos(d: dict) -> None:
    for i in sorted(d.items()):
        PrintVerde(i)

def menu() -> int:
    PrintCinzento("1 - Adicionar novo produto.")
    PrintCinzento("2 - Atualizar quantidade de produto.")
    PrintCinzento("3 - Atualizar preco de produto")
    PrintCinzento("4 - Listar productos")
    PrintCinzento("5 - Mostrar valor de stock.")
    PrintCinzento("6 - Mostrar produto mais caro")
    PrintCinzento("7 - Mostrar o produtos com stock inferior a 10")
    PrintCinzento("8 - Remover um produto")
    PrintCinzento("9 - Sair do programa.")
    i = int(input('\033[96m Introduza uma opcao: \033[00m'))
    return i

def menuAdicionarProduto():
    nome = input('Insira o nome: ')
    quantidade = int(input('Insira a quantidade: '))
    preco = float(input('Insira o preco: '))
    return nome, quantidade, preco

def menuActualizarProduto(t):
    nome = input('Insira o nome: ')
    valor = int(input(f"Insira {t}: "))
    return nome, valor

if __name__ == '__main__':
    d = {'batatas': {'q': 10, 'p': 1.5}}
    while True:
        match menu() :
            case 1:
                n, q, p = menuAdicionarProduto()
                adicionarProduto(d, n, q, p)
            case 2:
                n, q = menuActualizarProduto('quantidade')
                atualizarQuantidade(d, n, q)
            case 3:
                n, p = menuActualizarProduto('preco')
                atualizarPreco(d, n, p)
            case 4:
                exibirProdutos(d)
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                print('Sair do programa')
                break
