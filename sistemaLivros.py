biblioteca = [['Dom Quixote', 'Miguel de Cervantes'], ["Harry Potter", "J. K. Rowling"], ["O Senhor dos Anéis", "J. R. R. Tolkien"]]


def init ():
    opcaoMenu = 0
    while opcaoMenu != 6:

        print ("""
        1.    Adicionar Livro
        2.    Remover Livro
        3.    Atualizar Livro
        4.    Listar Livros
        5.    Procurar Livro
        6.    Sair
        """)

        opcaoMenu = int(input("Escolha uma opção: "))

        if opcaoMenu == 1:
            adicionarLivro()

        elif opcaoMenu == 2:
            removerLivro()

        elif opcaoMenu == 3:
            atualizarLivro()

        elif opcaoMenu == 4:
            listarLivros()

        elif opcaoMenu == 5:
            procurarLivro()

        elif opcaoMenu == 6:
            break

        else:
            print("Opção inválida. Tente novamente")


def adicionarLivro():
    titulo = input("Qual o titulo do livro? ")
    autor = input("Qual o autor do livro? ")

    biblioteca.append([titulo, autor])

    sucesso("adicionado")
    return

def removerLivro():
    titulo = recebeTitulo("remover")

    for livro in biblioteca:
        if livro[0] == titulo:
            biblioteca.remove(livro)
            sucesso("removido")
            return
        
    erro404()
    return

def atualizarLivro():
    titulo = recebeTitulo("Atualizar")

    for livro in biblioteca:

        if livro[0] == titulo:
            novoTitulo = input("Qual o novo titulo do livro? ")
            novoAutor = input("Qual o novo autor do livro? ")
            [livro[0], livro[1]]  = [novoTitulo, novoAutor]
            sucesso("Atualizado")
            return

    erro404()
    return

def listarLivros():
    if len(biblioteca) == 0:
        print("Nenhum livro na biblioteca!")
    else:
        print(biblioteca)
    return

def procurarLivro():
    titulo = recebeTitulo("procurar")

    for livro in biblioteca:
        if livro[0] == titulo:
            print(livro)
            return

    erro404()
    return

def recebeTitulo(acao):
    return input(f"Qual o livro você deseja {acao}? ")


def sucesso(acao):
    print(f"Livro {acao} com sucesso!")
    return

def erro404():
    print("Livro não encontrado")
    return

init()