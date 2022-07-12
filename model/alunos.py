class Alunos():
    def __init__(self,id,nome,email,curso,media): # Aluno é um objeto, que contém atributos.
        self.id = id
        self.nome = nome
        self.email = email
        self.curso = curso
        self.media = media
    def listar_alunos(self):
        print(self.id, self.nome, self.email, self.curso, self.media)

