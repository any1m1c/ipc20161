"""
#lista de repeti��o

#Antonio Rodrigues de Souza Neto --- matr�cula ----1615310028
#Gabriel Machado Moreira --- matr�cula ----1615310034
#Luiz Gustavo de Rocha Melo --- matr�cula ---- 1615310015
#Lucas Ferreira Soares --- 1615310014
#Calebe Roberto Chaves da Silva Rebello --- matr�cula---1615310043

"""
entrada = int(input("Digite um n�mero positivo inteiro: "))

primo = 1
contador = 0

entrada1 = entrada/2

while primo <= entrada:
    if entrada % primo==0:
        primo = primo+1
        contador = contador+1
    if primo >= entrada1:
        primo = entrada
        primo = primo + 1
        contador = contador + 1
    else:
        primo = primo + 1
if contador==2:
    print("O n�mero requisitado � primo!")
else:
    print("O n�mero requisitado n�o � primo!")
