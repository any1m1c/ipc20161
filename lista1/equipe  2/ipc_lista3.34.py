#professor jucimar junior
#Bruno de Oliveira freire - 1615310030
#Felipe Henrique Bastos Costa -1615310032
#Caio de OLiveira Martins-1615310031
#Samuel Silva de França- 1615310049
#Eduardo Maia Freire-1615310003
#lista de Repetição
num = int(input("Informe o numero inteiro que deseja analisar:\n"))

i = 1
divisores = 0

while i <= num :
    if num%i==0 :
        divisores+=1    
    i+=1
if divisores > 2 or num == 1:
    print("Nao e primo!")
else:
    print("E primo!")
