# O programa criado tem como objetivo realizar uma simulação do jogo
# Street Fighter Avançado. Inicialmente, deve­se inserir os números positivos do
# 1o round e sua soma será computada como os pontos do jogador Ryu.
# Sendo assim, ao inserir números negativos no jogo, começa a contagem
# de pontos do jogador Ken também sendo somados para marcar a pontuação
# final do 1o round. Nesse caso, os golpes tanto positivos quanto negativos
# quando inseridos, são multiplicados por 3 caso o número inserido seja perfeito
# e caso seja triangular e não perfeito é multiplicado por 2.
# Quando inserido outro número positivo, sabe­se que
# teve inicio o 2o round. Desta forma, os pontos acumulados no 1o round
# são somados e caso esse resultado seja positivo, 1 ponto em outra
# variável que representa o Ryu é armazenado. Caso contrário, o ponto
# vai pro Ken, assim como se for 0 não soma nada a nenhuma das
# variáveis. Essa estrutura se repete até que tenha a inserção do número
# 0, que para o programa e confere quem venceu mais rounds e anuncia o
# vencedor do jogo.

n = 1
ken = 0
ryu = 0
somr = 0
somk = 0
neg = False

while(n != 0): # Enquanto o número inserido for diferente de 0, o programa roda
  n = int(input())
  
  if (neg == True) and (n > 0):
    total = somr + somk 
    somr = 0
    somk = 0
    neg = False  # retorna como falsa a variável indicadora de n negativo. 
    if (total > 0):
      ryu = ryu + 1 # Acréscimo de 1 pt a quem ganhou o round
      total = 0
    elif (total < 0):
      ken = ken + 1
      total = 0
    

  if (n > 0):  # Para números positivos, o programa verifica:
    tot = 0
    pft = False
    for i in range(1, n): # 1) Se o número é perfeito.
        if (n%i == 0):
          tot = tot + i
          if (tot == n):
            pft = True 

    som = 0
    i = 1
    tri = False
    while(som <= n):  # 2) Se o número é triangular.
      som = som + i
      i = i + 1 
      if (som == n):
        tri = True
   
    
    if (pft == True):  # Caso perfeito, multiplica-se por 3.
      somr = somr + 3*n   
    if (tri == True) and (pft == False): # Caso triangular (x2).
      somr = somr + 2*n
    if (pft == False) and (tri == False):
      somr = somr + n


  if (n < 0):   # Para números negativos, o programa verifica:
    neg = True  # Assinala como verdadeira a variável indicadora de n negativo.
    tot = 0
    pft = False
    for i in range(1, -n):  # 1) Se o número é perfeito.
      if (n%i == 0):
        tot = tot + i
        if (tot == -n):
          pft = True 

    som = 0
    i = 1
    tri = False
    while(som <= -n):  # 2) Se o número é triangular.
      som = som + i
      i = i + 1 
      if (som == -n):
        tri = True

    
    if (pft == True):  # Caso perfeito, multiplica-se por 3.
      somk = somk + 3*n   
    if (tri == True) and (pft == False):  # Caso triangular (x2).
      somk = somk + 2*n
    if (pft == False) and (tri == False):
      somk = somk + n


  if (n == 0):  # Caso a entrada seja 0, o programa para e dá o resultado.
    break

total = somr + somk  # Esse processo deve ser realizado novamente para computar
if (total > 0):      # o último round. 
  ryu = ryu + 1 
elif (total < 0):
  ken = ken + 1

if (ryu > ken):  # Conferência de quem venceu o jogo.
  print("Ryu venceu")
elif (ryu < ken):
  print("Ken venceu")
else:
  print("empatou")	

