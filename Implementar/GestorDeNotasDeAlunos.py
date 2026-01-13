# fazer um print com texto em verde
def PrintVerde(input):
    print(f"\033[92m {input} \033[00m")

# fazer um print com texto em azul
def PrintAzul(input):
    print(f"\033[94m {input} \033[00m")


# Adicionar um novo aluno e nota.
def adicionarNovoAluno(d : dict, nome: str, nota: int) -> None:
    #TODO
    return

# Atualizar a nota de um aluno existente.
def atualizarNota(d: dict, nome: str, nota: int) -> None:
    #TODO
    return

# Exibir todos os alunos e notas (por ordem alfabética ou nota decrescente)
def exibirAlunos(d: dict) -> None:
    #TODO
    return

def exibirAlunosRevertido(d: dict) -> None:
    #TODO
    return

# Mostrar o aluno com a maior nota.
def exibirMelhor(d: dict) -> None:
    #TODO
    return

# Mostrar aluno com menor nota
def exibirPior(d: dict) -> None:
    #TODO
    return

def menu() -> int:
    PrintAzul("1 - Adicionar um novo aluno e nota.")
    PrintAzul("2 - Atualizar a nota de um aluno existente.")
    PrintAzul("3 - Exibir todos os alunos e notas")
    PrintAzul("4 - Mostrar o aluno com a maior nota.")
    PrintAzul("5 - Mostrar aluno com menor nota")
    PrintAzul("6 - Sair do programa.")
    i = int(input('\033[96m Introduza uma opcao: \033[00m'))
    return i

def menuAdicionarAluno():
    nome = input('Insira o nome: ')
    nota = int(input('Insira a nota: '))
    return nome, nota

if __name__ == '__main__':
    d = dict()
    while True:
        opcao = menu()
        match opcao :
            case 1:
                nome, nota = menuAdicionarAluno()
                adicionarNovoAluno(d, nome, nota)
            case 2:
                nome, nota = menuAdicionarAluno()
                atualizarNota(d, nome, nota)
            case 3:
                exibirAlunos(d)
                # exibirAlunosRevertido(d)
            case 4:
                exibirMelhor(d)
            case 5:
                exibirPior(d)
            case 6:
                print('\t Sair do programa')
                break
