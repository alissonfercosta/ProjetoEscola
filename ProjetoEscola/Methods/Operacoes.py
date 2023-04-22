import os

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