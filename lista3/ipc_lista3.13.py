"""
#lista de repeti��o

#Antonio Rodrigues de Souza Neto --- matr�cula ----1615310028
#Gabriel Machado Moreira --- matr�cula ----1615310034
#Luiz Gustavo de Rocha Melo --- matr�cula ---- 1615310015
#Lucas Ferreira Soares --- 1615310014
#Calebe Roberto Chaves da Silva Rebello --- matr�cula---1615310043

"""

base=int(input("Digite o valor da base:"))
expoente=int(input("Digite o valor do expoente:"))

cont=0
produto=1
while cont < expoente:
    produto=produto*base
    cont=cont+1

print(base, "elevado a", expoente, "=", produto)    