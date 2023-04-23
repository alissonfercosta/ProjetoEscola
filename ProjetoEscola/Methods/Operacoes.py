from datetime import datetime
import os
from Models.Aluno import *
import json

def CalculoMedia():
    os.system('cls')
    qtdNotas = input("Digite quantas notas serão calculadas para fazer a media: ")
    listaNotas = []
    media = 0
    
    for i in range(int(qtdNotas)):
        tempNota = int(input(f"Digite a {i+1} nota: "))
        listaNotas.append(tempNota)
        
    for i in range(len(listaNotas)):
        media = media + listaNotas[i]
    
    media = media / int(len(listaNotas))
    
    print(f"Media do aluno é: {media}")
    
    input("enter para continuar ...")
    
    
def ImportaAlunosCSV():
    arquivo = open(r"C:\Users\Alisson\Documents\Codigos\_AUX\CSV\listaAlunos.csv", "r")

    next(arquivo)   
    
    Alunos = []
    contador = 0
    
    for aluno in arquivo:
        splitAluno = aluno.split(";")
        tempAluno = Aluno(splitAluno[0],int(splitAluno[1]),int(splitAluno[2]),splitAluno[3].replace("\n",""))
        Alunos.append(tempAluno)
        contador += 1
    
    arquivo.close()
    
    print(f"\nFoi importado {contador} alunos !!\n")
    input("enter para continuar ...")
    os.system('cls')
    return Alunos


def ExportaAlunosCSV(Alunos):    
    print("Iniciando exportação de Alunos para CSV. . .")
    
    contador = 0
    dateTime = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    nomeArquivo = fr"C:\Users\Alisson\Documents\Codigos\_AUX\CSV\Export\exportacao_alunos_{dateTime}.csv"
    
    novoArquivo = open(nomeArquivo, "x")
    novoArquivo.write("Nome;Idade;Matricula;Serie\n")
    
    for aluno in Alunos:
        novoArquivo.write(f"{aluno.Nome};{aluno.Idade};{aluno.Matricula};{aluno.Serie}\n")
        contador += 1
    
    novoArquivo.close()
    print(f"\nFoi exportado no caminho {nomeArquivo}, um total de {contador} alunos !!\n")
    input("enter para continuar ...")
    os.system('cls')
    
    
def ImportaAlunosJSON():
    arquivo = open(r"C:\Users\Alisson\Documents\Codigos\_AUX\JSON\listaAlunos.json", "r").read()
    
    arquivoJson = json.loads(arquivo)
    
    Alunos = []
    contador = 0
    
    for aluno in arquivoJson:
        tempAluno = Aluno(aluno["Nome"],int(aluno["Idade"]),int(aluno["Matricula"]),aluno["Serie"])
        Alunos.append(tempAluno)
        contador += 1
    
    print(f"\nFoi importado {contador} alunos !!\n")    
    input("enter para continuar ...")
    os.system('cls')
    return Alunos    


def ExportaAlunosJSON(Alunos):
    print("\nIniciando exportação de Alunos para CSV. . .\n")
    
    contador = 0
    dateTime = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    nomeArquivo = fr"C:\Users\Alisson\Documents\Codigos\_AUX\JSON\Export\exportacao_alunos_{dateTime}.json"
    novoArquivo = open(nomeArquivo, "x")
    
    novoArquivo.write("[\n")
    for aluno in Alunos:
        tmpAluno = json.dumps(aluno.__dict__)
        novoArquivo.write(f"    {tmpAluno}, \n")
        contador += 1
        
    novoArquivo.write("\n]")
    novoArquivo.close()    
    print(f"\nFoi exportado no caminho {nomeArquivo}, um total de {contador} alunos !!\n")
    input("enter para continuar ...")
    os.system('cls')    
    