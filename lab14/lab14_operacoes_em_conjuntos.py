#!/usr/bin/env python3

# O programa criado consiste em realizar, a partir de um conjunto, operações como adição, subtração e verificação da existência de elementos em tal conjunto. Além disso, o programa é capaz de realizar operações entre dois conjuntos, como intersecção, união e diferença, podendo também verificar se um conjunto está contido no outro. As funções contidas nesse laboratório são importadas para outro que simplifica a maneira de como a entrada e saída funcionarão. Desta vez, o programa opera por meio de classes.

class conjunto:
    def __init__(self):
      self.numeros = []
      self.elementos = 0

# Funcao: novo_conjunto
#
# Cria uma nova instancia da classe conjunto, e inicializa os valores de numeros e elementos.
# A nova instancia deve ser retornada.
#
# Retorno:
#   Nova instancia da classe conjunto com 0 elementos e uma lista vazia

def novo_conjunto():
    novo_conjunto = conjunto()
    novo_conjunto.numeros = []
    novo_conjunto.elementos = 0
    return novo_conjunto

# Funcao: pertence
#
# Verifica se o conjunto instanciado em conj possui o elemento num.
# O conjunto nao deve ser modificado.
#
# Parametros:
#   conj: instancia do conjunto de entrada
#    num: elemento a ser verificado pertinencia
#
# Retorno:
#   True se o elemento num pertence a conj e False caso contrario
#
def pertence(conj, num):
    if num in conj.numeros:
        return True  # Se o número está no conjunto retorna True
    else:   # Se o número não está no conjunto retorna False
        return False

# Funcao: contido
#
# Verifica se o conjunto instanciado em conj1 esta contido no conjunto instanciado em conj2.
# Os conjuntos nao devem ser modificados.
#
# Parametros:
#   conj1: instancia do conjunto de entrada que sera o primeiro operando
#   conj2: instancia do conjunto de entrada que sera o segundo operando
#
# Retorno:
#   True se conj1 esta contido em conj2 e False caso contrario
#

def contido(conj1, conj2):
    cont = True
    for i in range(conj1.elementos):
        if conj1.numeros[i] not in conj2.numeros:
            cont = False # Se um dos números do conj1 não estiver no conj2 a variável indicadora torna-se falsa e dá um break.
            break
        else: # Se todos os números estiverem no outro conjunto, a variável fica verdadeira.
            cont = True
    return cont # Retorna variável indicadora. 

# Funcoes: adicao e subtracao
#
# Realiza a acao do nome da funcao para o conjunto instanciado em conj com o elemento num.
#
# Parametros:
#   conj: instancia do conjunto que tera incluso ou removido o elemento
#    num: elemento a ser adicionado ou removido
#
#    Deve-se atualizar o valor do campo elementos caso um elemento seja removido
#    ou adicionado.

def adicao(conj, num):
    if not pertence(conj, num): # Caso não esteja no conjunto, ele é adicionado
        conj.numeros.append(num)
        conj.elementos = conj.elementos + 1 # Aumenta em 1 o número de elementos do conjunto
    return None

def subtracao(conj, num):
    if pertence(conj, num): # Caso esteja no conjunto ele é removido
        conj.numeros.remove(num)
        conj.elementos = conj.elementos - 1 # Diminui em 1 o número de elementos do conjunto
    return None

# Funcoes: uniao, intersecao e diferenca
#
# Realiza a operacao do nome da funcao entre o conjunto conj1 e o conj2, respectivamente.
# O resultado deve ser armazenado num novo conjunto instanciado para esta finalidade.
# Os conjuntos conj1 e conj2 nao devem ser modificados.
#
# Parametros:
#     conj1: instancia do conjunto de entrada que sera o primeiro operando
#     conj2: instancia do conjunto de entrada que sera o segundo operando
#
# Retorno:
#   Instancia de um novo conjunto que contem o resultado da operacao
#
def uniao(conj1, conj2):
    conju = novo_conjunto() # Cria o conjunto da união   
    for p in range(conj1.elementos): # Adiciona os números do conj1 no conju (conjunto da união)
      adicao(conju, conj1.numeros[p])
    for i in range(conj2.elementos):
      if conj2.numeros[i] not in conju.numeros: # Busca os números do conj2 que ainda não estão no conju e os adiciona
        adicao(conju, conj2.numeros[i])
    return conju
      

def intersecao(conj1, conj2):
    conji = novo_conjunto() # Cria o conjunto da intersecção
    for i in range(conj1.elementos):
        if conj1.numeros[i] in conj2.numeros: # Busca os números do conj1 que estão no conj2 e os adiciona a conji
            adicao(conji, conj1.numeros[i])
    return conji

def diferenca(conj1, conj2):
    conjd = novo_conjunto() # Cria o conjunto da diferença
    for i in range(conj1.elementos):
      if conj1.numeros[i] not in conj2.numeros: # Busca os números que estão no conj1 e não estão no conj2 e os adiciona a conjd
        adicao(conjd, conj1.numeros[i])
    return conjd
