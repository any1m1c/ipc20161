#professor jucimar junior
#Bruno de Oliveira freire - 1615310030
#Felipe Henrique Bastos Costa -1615310032
#Caio de OLiveira Martins-1615310031
#Samuel Silva de França- 1615310049
#Eduardo Maia Freire-1615310003
#lista de Repetição
num_turma = float(input("Informe o numero de turmas:\n"))
cond = 1
x1 = 0
alunos_t = 0

while(cond <= num_turma):
    x1 += 1
    num_alunos = float(input("Informe o numero de alunos da %dº turma:\n"%x1))
    
    if( num_alunos <= 40 ):
        alunos_t += num_alunos
        media = alunos_t/num_turma
        cond += 1
        
    else:
        x1 -= 1
        cond = 1
        
print("A media de alunos por turma e de %.2f alunos"%media)
