# O programa criado tem como objetivo realizar uma simulação do jogo
# Street Fighter. Inicialmente, deve­se inserir os números positivos do
# 1o round e sua soma será computada como os pontos do jogador Ryu.
# Sendo assim, ao inserir números negativos no jogo, começa a contagem
# de pontos do jogador Ken também sendo somados para marcar a pontuação
# final do 1o round. Quando inserido outro número positivo, sabe­se que
# teve inicio o 2o round. Desta forma, os pontos acumulados no 1o round
# são somados e caso esse resultado seja positivo, 1 ponto em outra
# variável que representa o Ryu é armazenado. Caso contrário, o ponto
# vai pro Ken, assim como se for 0 não soma nada a nenhuma das
# variáveis. Essa estrutura se repete até que tenha a inserção do número
# 0, que para o programa e confere quem venceu mais rounds e anuncia o
# vencedor do jogo.

n = int(input())
a = 1
n2 = 1
ken = 0
ryu = 0

while(n != 0) and (n2 != 0): # Enquanto o número inserido for diferente de 0, o programa roda
	if (n > 0):
	  n = n + a 
	  a = int(input())
	  if (a < 0): 
	    b = a 
	    while (b < 0):
	      b = b + n2
	      n2 = int(input())
	      if (n2 == 0): # Se o número for 0, o programa para
	        break
	      if (n2 > 0): # Veriicação de quem ganhou o round
	        c = n + b
	        n = 1
	        b = 0
	        a = n2
	        n2 = 1
	        if (c > 0):
	      	  ryu = ryu + 1 # Acréscimo de 1 pt a quem ganhou o round
	        elif (c < 0):
	          ken = ken + 1
	          
c = n + b  # Esse processo se repete uma ultima vez quando o programa para pois é necessário computar também o ultimo round 
if (c > 0):
  ryu = ryu + 1
elif (c < 0):
  ken = ken + 1	          

if (ryu > ken):  #conferência de quem venceu o jogo.
  print("Ryu venceu")
elif (ryu < ken):
  print("Ken venceu")
else:
  print("empatou")	        
	          
