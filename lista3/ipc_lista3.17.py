"""
#lista de repeti��o

#Antonio Rodrigues de Souza Neto --- matr�cula ----1615310028
#Gabriel Machado Moreira --- matr�cula ----1615310034
#Luiz Gustavo de Rocha Melo --- matr�cula ---- 1615310015
#Lucas Ferreira Soares --- 1615310014
#Calebe Roberto Chaves da Silva Rebello --- matr�cula---1615310043

"""
n = int(input("Digite o valor de n: "))

produto = n
contador =  n-1

while contador > 1:
    produto = produto*contador
    contador = contador - 1

print(n, "!=", produto)
