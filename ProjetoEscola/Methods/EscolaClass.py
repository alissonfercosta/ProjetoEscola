from Models.Escola import *

def CadastraEscola():
    
    escolaNome = input("Digite o nome do escola:")
    escolaLogradouro = input("Digite o logradouro:")
    escolaNumero = input("Digite numero da escola:")
    escolaBairro = input("Digite qual o bairro da escola:")
    escolaCapacidade = input("Digite a capacidade maxima da escola:")
    
    print("Cadastro de escola Efetuado com sucesso !!")
    
    return Escola(escolaNome, escolaLogradouro, escolaNumero, escolaBairro, escolaCapacidade)
    
def ListaEscolasCadastradas(Escolas):
    for escola in Escolas:
        print(f"\nNome escola: {escola.NomeEscola}, Logradouro: {escola.Logradouro}, Numero: {escola.Numero}, Bairro: {escola.Bairro}, Capacidade: {escola.Capacidade}\n")      
    input("enter para continuar ...")    