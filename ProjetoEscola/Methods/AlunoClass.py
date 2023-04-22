from Models.Aluno import *

def CadastraAluno():
    
    alunoNome = input("Digite o nome do aluno: ")
    alunoIdade = input("Digite a idade do aluno: ")
    alunoMatricula = input("Digite a matricula do aluno: ")
    alunoSerie = input("Digite a serie do aluno: ")
    
    print("Cadastro de aluno Efetuado com sucesso !!")
    
    return Aluno(alunoNome, alunoIdade, alunoMatricula, alunoSerie)

def ListaAlunoCadastrados(Alunos):
    for aluno in Alunos:
        print(f"\nNome aluno: {aluno.Nome}, Idade: {aluno.Idade}, Matricula: {aluno.Matricula}, Serie: {aluno.Serie}\n")      
    input("enter para continuar ...")