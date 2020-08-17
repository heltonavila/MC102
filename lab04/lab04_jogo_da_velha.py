# O programa criado consiste num jogo da velha. Para a realização do mesmo é solicitado a entrada de 9 caracteres, sendo eles escolhidos entre 3 opções: X,O ou -.
# Sendo assim, é verificada a igualdade dos termos por linha, coluna e diagonal.
# Caso a igualdade seja verdadeira para os caracteres X ou O, o programa apresenta como saída o termo que torna válida essa igualdade, seguido da palavra "venceu".
# Caso não se confirme a igualdade, a saída do programa é a palavra "empate".

v1 = input()
v2 = input()
v3 = input()
v4 = input()
v5 = input()
v6 = input()
v7 = input()
v8 = input()
v9 = input()

if (v1 == v2 == v3) or (v1 == v5 == v9) or (v1 == v4 == v7): # Os comandos a seguir testam a igualdade dos termos por linha, coluna e diagonal.
    if (v1 == "X") or (v1 == "O"):
      print(str(v1) + " venceu") 
elif (v5 == v2 == v8) or (v5 == v4 == v6):
    if (v5 == "X") or (v5 == "O"):
      print(str(v5) + " venceu")
elif (v9 == v6 == v3) or (v9 == v8 == v7):
    if (v9 == "X") or (v9 == "O"):
      print(str(v9) + " venceu")
elif (v7 == v5 == v3):
    if (v7 == "X") or (v7 == "O"):
      print(str(v7) + " venceu")
else: # Caso a igualdade seja falsa, o programa imprime "empatou".
      print("empatou")
 
