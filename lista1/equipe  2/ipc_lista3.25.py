#professor jucimar junior
#Bruno de Oliveira freire - 1615310030
#Felipe Henrique Bastos Costa -1615310032
#Caio de OLiveira Martins-1615310031
#Samuel Silva de França- 1615310049
#Eduardo Maia Freire-1615310003
#lista de Repetição

n = int(input("Informe quantos alunos existem na turma:\n"))

soma = 0
x = 1
x1 = 0

while( x <= n ):
    x1 = x1 + 1
    idade = int(input("Informe a idade do %dº aluno:\n"%x1))
    x = x + 1
    soma = soma + idade
    media = (soma)/n    

if(media >= 0 and media <= 25):
    t = "E uma turma jovem"
elif(media >= 26 and media <= 60):
    t = "E uma turma adulta"
elif(media > 60):
    t = "E uma turma idosa"

print("A media da turma e %d anos\n%s"%(media,t))
