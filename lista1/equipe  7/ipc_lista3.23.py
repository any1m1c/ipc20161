"""
#lista de repeti��o

#Antonio Rodrigues de Souza Neto --- matr�cula ----1615310028
#Gabriel Machado Moreira --- matr�cula ----1615310034
#Luiz Gustavo de Rocha Melo --- matr�cula ---- 1615310015
#Lucas Ferreira Soares --- 1615310014
#Calebe Roberto Chaves da Silva Rebello --- matr�cula---1615310043

"""

N = int(input("Digite um n�mero inteiro: "))

primo = 1
contador = 0
N1 = N/2

while primo <= N:
    if (N % primo==0):
        primo = primo + 1
        contador = contador + 1
    if (primo >= N1):
        primo = N
        primo = primo + 1
        contador = contador + 1
    else:
        primo = primo + 1
if contador==2:
    print("O n�mero de divis�es foi",contador)
else:
    print("O n�mero de divis�es foi",contador)
