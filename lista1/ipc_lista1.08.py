#ipc_lista1.8
#Professor: Jucimar Junior
#Any Mendes Carvalho - 1615310044
#
#
#
#
#Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês.

QntHora = input("Entre com o valor de seu rendimento por hora: ")
hT = input("Entre com a quantidade de horas trabalhadas no mês: )

Salario = round(QntHora*hT,2)

print("\n Você ganhou %.2f reais neste mês") % *Salario)
