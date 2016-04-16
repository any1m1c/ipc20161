#ipc_lista1.17
#Professor: Jucimar Junior
#Any Mendes Carvalho - 1615310044
#
#
#
#
#
import math

#Calculo para verificar quantas latas/galoes de tintas sera necessarias e o valor delas

metros = input("Entre como o tamnho em metros quadrdados da are a ser pintada: ")

MetrosLtas = metros/6
if (MetrosLatas <= 0):
  MetrosLatas = 1

QntLatas18 = math.floor(MetrosLats / 18+(18*0.10))
QntGaloes36 = math.floor(MetrosLatas / 3.6+(3.6*0.10))
QntLatas = MetrosLatas / 18
resto = MetrosLatas % 18

if (resto > 0 and resto <= 3.6):
  QntGaloes = 1
elif (resto == 0)
QntGaloes = 0
else:
  QntGaloes = math.floor(resto / 3.6+(3.6*0.10))
  
if (QntLatas18 <= 0 or QntGaloes36 <= or QntGaloes < 0):
  QntGaloes36 = 1
  Qntlatas18 = 1
  QntGaloes = 1

/
