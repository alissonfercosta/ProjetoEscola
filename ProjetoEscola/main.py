import os
from Utils.aprensetacoes import *
from Methods.menu import *

ExibeInicio()

menu = True
contador = 0

while(menu):
    ExibeOpcoesMenu()
    opcao = input("Digite uma Opção ou (0) para sair: ")
    menu = ExecutaMenu(opcao)
    contador = contador + 1

print(f"Foram executadas um total de {contador - 1} operações !")
input("enter para continuar ...")
os.system('cls')
