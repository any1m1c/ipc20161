#Eduardo Maia Freire
vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []
x = 0
for x in range (5):
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))
    vetor1.append(idade)
    vetor2.append(altura)
    x = x + 1
y = len(vetor1) -1
while(y >= 0):
    vetor3.append(vetor1[y])
    vetor4.append(vetor2[y])
    y = y - 1
    
print("Vetor da Idade = ",vetor3)
print("Vetor da Altura = ",vetor4)