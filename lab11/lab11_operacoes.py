# O programa criado consiste em realizar, a partir de um conjunto, operações como
# adição, subtração e verificação da existência de elementos em tal conjunto.
# Além disso, o programa é capaz de realizar operações entre dois conjuntos,
# como intersecção, união e diferença, podendo também verificar se um conjunto
# está contido no outro. As funções contidas nesse laboratório são importadas
# para outro que simplifica a maneira de como a entrada e saída funcionarão.

# Funcao: pertence
#
# Parametros:
#   conj: vetor contendo o conjunto de entrada
#    num: elemento a ser verificado pertinencia
#
# Retorno:
#   True se num pertence a conj e False caso contrario
#

def pertence(conj, num):
      pert = False
      if (len(conj) == 0): # Se o conjunto é vazio, nenhum número pertence a ele
        pert = False
      else:
        for i in range(len(conj)): 
          if (num ==  conj[i]): # Se o número estiver no conjunto, a indicadora torna-se verdadeira
            pert = True
            break
          else: 
            pert = False
      return pert  

# Funcao: contido
#
# Parametros:
#   conj1: vetor contendo um conjunto de entrada
#   conj2: vetor contendo um conjunto de entrada
#
# Retorno:
#   True se conj1 esta contido em conj2 e False caso contrario
#


def contido(conj1, conj2):
  if (len(conj1) == 0): # Se o conjunto for vazio, ele está contido em qualquer conjunto
    cont = True
  else:
    for p in range(len(conj1)):    
      if (conj1[p] not in conj2): # Se um dos itens do conjunto não estiverem no outro a indicadora torna-se falsa
        cont = False
        break 
      else:
        cont = True
  return cont
       
    
# Funcoes: adicao e subtracao
#
# Parametros:
#   conj: vetor contendo o conjunto que tera incluso ou removido o elemento
#    num: elemento a ser adicionado ou removido
#
def adicao(conj, num):
  if num not in conj: # Se o número não estiver no conjunto ele é adicionado    
    conj.append(num)
  return conj

def subtracao(conj, num):
  if num in conj: # Se o número estiver no conjunto ele é removido
    conj.remove(num)
  return conj

# Funcoes: uniao, intersecao e diferenca
#
# Parametros:
#     conj1: vetor contendo o conjunto de entrada do primeiro operando
#     conj2: vetor contendo o conjunto de entrada do segundo operando
#
# Retorno:
#   Vetor contendo o conjunto de saida/resultado da operacao
#


def uniao(conj1, conj2):
    conju = conj1 + conj2 # Concatena os dois conjuntos
    conju = list(set(conju)) # Retira os números repetidos
    return conju

def intersecao(conj1, conj2):
    conji = [] # Cria lista vazia para armazenar a intersecção
    for i in range(len(conj1)): 
      for j in range(len(conj2)):
        if (conj1[i] == conj2[j]): # Se o número está no conjunto 1 e 2, é armazenado na intersecção
          conji.append(conj1[i])
          conji = list(set(conji)) # São retirados do conjunto os números repetidos
    return conji

def diferenca(conj1, conj2):
    conjd = [] # Cria lista vazia para armazenar a diferença
    for i in range(len(conj1)):
      if conj1[i] not in conj2: # Se um número do conjunto 1 não está no conjunto 2, é armazenado na diferença
        conjd.append(conj1[i])
    return conjd
