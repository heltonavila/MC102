# O programa criado consiste no cálculo da circunferência de um planeta qualquer baseado na distância entre duas localidades (em estádios) e no ângulo formado entre elas em relação ao centro do planeta. A partir dos dados inseridos, o programa dá como saída dois resultados, sendo eles a circunferência do tal planeta em estádios e em quilômetros. 

dist = float(input())
ang = float(input())

estad = (360/ang)*dist
kilom = (176.4*estad)/1000

print("%.1f"%estad)
print("%.1f"%kilom)
