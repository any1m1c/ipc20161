#Eduardo Maia Freire
vetor1 = [1,2,3,4,5,6,7,8,9,10]
vetor2 = []
vetor3 = []
v1 = len(vetor1)
v2 = len(vetor2)
v3 = len(vetor3)
x = 0
for x in range(v1) :
    if(vetor1[x]%2 == 0):
        vetor2.append(vetor1[x])
    else:
        vetor3.append(vetor1[x])
    print(vetor1)
print("Vetor 1 = ",vetor1)
print("Vetor 2 = ",vetor2)
print("Vetor 3 = ",vetor3)
    
    