"""
lista 4 questao 8:
Fa�a um Programa que pe�a a idade e a altura de 5 pessoas, 
armazene cada informa��o no seu respectivo vetor. 
Imprima a idade e a altura na ordem inversa a ordem lida.
"""
#Luiz Gustavo Rocha Melo - 1615310015
altura = []
alturainv = []
idade = []
idadeinv = []
v = 5
c1 = 1
c2 = 0

while (c2 < v):
    x = int(input("A idade da pessoa: "))
    idade.append(x)
    y = float(input("O tamnaho da pessoa: "))
    altura.append(y)
    c1 += 1
    c2 += 1
    
while (v > 0):
    v -= 1
    w = idade[v]
    z = altura [v]
    
    idadeinv.append(w)
    alturainv.append(z)

print("A ordem inversa da idade",idadeinv)
print("A ordem inversa da altura",alturainv)