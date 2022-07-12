lista_alunos = [] #Lista que armazena os alunos.
def adicionar_alunos(novo_aluno):
    lista_alunos.append(novo_aluno)

def listar_alunos():
    for x in lista_alunos:
        print(x.nome)

