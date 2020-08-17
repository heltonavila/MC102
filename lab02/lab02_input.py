# O programa criado pede como entrada 6 números inteiros. A partir desses números, é verificado se eles formam um triângulo mágico. Cada face do triângulo é formada por 3 desses números e são posicionados numa ordem pré-determinada pelo programa. Caso a soma dos números em cada face seja igual para as 3 faces do triângulo, o programa responde "sim", significando que os números inseridos formam um triângulo mágico. Caso contrário, a resposta dada pelo programa é "nao".

p1 = int(input())
p2 = int(input())
p3 = int(input())
p4 = int(input())
p5 = int(input())
p6 = int(input())
if (p1 + p2 + p3 == p3 + p4 + p5) and (p3 + p4 + p5 == p1 + p5 + p6):
  print("sim")
else: 
  print("nao")
  
