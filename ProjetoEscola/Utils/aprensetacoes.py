import os

def ExibeInicio():
    os.system('cls')
    print("Bem vindo ao sistema Escola! pressione enter para continuar\n")
    input("enter para continuar ...")
    os.system('cls')
    
def ExibeOpcoesMenu():
    print("- Aperte (1) para Cadastrar um aluno")
    print("- Aperte (2) para listar os alunos cadastrados")
    print("- Aperte (3) para Cadastrar um Escola")
    print("- Aperte (4) para listar todos as Escola") 
    print("- Aperte (5) para calcular media de notas") 
    print("- Aperte (6) para importar alunos por arquivo CSV") 
    print("- Aperte (7) para exportar alunos para arquivo CSV") 
    print("- Aperte (8) para importar alunos para arquivo JSON")
    print("- Aperte (9) para exportar alunos para arquivo JSON\n")