import os
from Methods.Operacoes import *
from Models.Aluno import *
from Models.Escola import *
import Methods.AlunoClass
import Methods.EscolaClass

Alunos = []
Escolas = []

def ExecutaMenu(opcao):
    if(int(opcao) == 1):
            tempAluno = Methods.AlunoClass.CadastraAluno()
            Alunos.append(tempAluno)
            
    elif(int(opcao) == 2):
        if len(Alunos) > 0:
            Methods.AlunoClass.ListaAlunoCadastrados(Alunos)
        else:
            print("Não existe alunos cadastrados !")
            input("enter para continuar ...")
            os.system('cls')
            
    elif(int(opcao) == 3):
        tempEscola = Methods.EscolaClass.CadastraEscola()
        Escolas.append(tempEscola)    
    
    elif(int(opcao) == 4):
        if len(Escolas) > 0:
            tempEscola = Methods.EscolaClass.ListaEscolasCadastradas()
        else:
            print("Não existe escolas cadastradas !")
            input("enter para continuar ...")
            os.system('cls')
    
    elif(int(opcao) == 5):
        CalculoMedia()
    
    elif(int(opcao) > 5):
        print("Opção invalida!!")
        
    elif(int(opcao) == 0):
        os.system('cls')
        return False
    
    return True