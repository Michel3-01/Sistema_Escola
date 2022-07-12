from model.alunos import Alunos
import model.alunos_dao as funcoes_alunos


aluno01 = Alunos(0,"João","Joãosantos45@gmail.com","Programação",0)
aluno02 = Alunos(1,"Miguel fernando", "Miguel78@gmail.com","DBA",0)
funcoes_alunos.adicionar_alunos(aluno01)
funcoes_alunos.adicionar_alunos(aluno02)

funcoes_alunos.listar_alunos()

