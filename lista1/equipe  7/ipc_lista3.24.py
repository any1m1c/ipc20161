"""
#lista de repeti��o

#Antonio Rodrigues de Souza Neto --- matr�cula ----1615310028
#Gabriel Machado Moreira --- matr�cula ----1615310034
#Luiz Gustavo de Rocha Melo --- matr�cula ---- 1615310015
#Lucas Ferreira Soares --- 1615310014
#Calebe Roberto Chaves da Silva Rebello --- matr�cula---1615310043

"""

nota = float(input("Insira a nota (ZERO para sair): "))

cont = 0
soma = 0

while (nota != 0):
        cont += 1
        soma += nota
        nota = float(input("Insira a nota (ZERO para sair): "))
        
media = soma / cont

print("Sua m�dia � de:",media)