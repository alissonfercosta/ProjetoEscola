import os

def ExibeInicio():
    os.system('cls')
    print("Bem vindo ao sistema Escola! pressione enter para continuar\n")
    input("enter para continuar ...")
    os.system('cls')
    
def ExibeOpcoesMenu():
    print("- Aperte (1) para Cadastrar um aluno\n")
    print("- Aperte (2) para listar os alunos cadastrados\n")
    print("- Aperte (3) para Cadastrar um Escola\n")
    print("- Aperte (4) para listar todos as Escola\n") 
    print("- Aperte (5) para calcular media de notas\n") 