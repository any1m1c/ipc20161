#ipc_lista1.18
#Professor: Jucimar Junior
#Any Mendes Carvalho - 1615310044
#
#
#
#
#Faça um programa que peça o tamanho de um arquivo para download(em MB) e a velocidade de um link de internet (em Mbps), calcule e informe o tempo aproximado de downloado do arquivo usando este link (em minutos).

arquivo = input("Informe o tamanho do arquivo para download (em MB): ")
print
velocidade = input("Informe a velocidade de sua internet (em Mbps): ")
tempo = arquivo / velocidade
minuto = tempo / 60.0
print
print " O tempo aproximado para download do arquivo usando este link e de: %.2f minutos" %minuto
