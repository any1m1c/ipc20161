#ipc_lista1.13
#Professor: Jucimar Junior
#Any Mendes Carvalho - 1615310044
#
#
#
#
#Tendo como dados de entrada a altura e o sexo de uma pessoa, constru um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7 (h = altura)
#Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.

h = input("Entre com sua altura: ")
sexo = str(raw_input(Sexo M ou F: "))
peso - input("Qual seu peso: ")

if ("F" == sexo):
  resultado = (62.1*h) - 44.7
else:
  resultado = (72.7*h) - 58

if(peso > resultado):
  print "Você está acima do peso, seu peso ideal e %.1f kg" % (resultado)
else:
  print "Voce está abaxio do peso, seu peso ideal e %.1f kg" % (resultado)
  
