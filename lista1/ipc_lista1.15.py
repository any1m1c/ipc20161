#ipc_lista1.15
#Professor: Jucimar Junior
#Any Mendes Carvalho - 1615310044
#
#
#
#
##Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

    #salário bruto.
    #quanto pagou ao INSS.
    #quanto pagou ao sindicato.
    #o salário líquido.
    #calcule os descontos e o salário líquido, conforme a tabela abaixo:

    #+ Salário Bruto : R$
    #- IR (11%) : R$
    #- INSS (8%) : R$
    #- Sindicato ( 5%) : R$
    #= Salário Liquido : R$

    #Obs.: Salário Bruto - Descontos = Salário Líquido. 

qHora = input("Quanto você ganha por hora: ")
hT = input("Quantas horas você trabalhou: ")

SalBruto = qHora

ir = (11/100.0 * salBruto)
inss = (8/100.0m* SalBruto)
sindicato = (5/100.0 * SalBruto)

vT = ir + sindicato
SalLiq = SalBruto - vT

print "------------------------"
print "Seu salário bruto e: ",SalBruto

print '------------------------"
print "Valor dos impostos"
print "-------------------------"
print "IR: ",ir
print "INSS: ",inss
print"--------------------------"
print"Se salario liquido e: ",SalLiq
