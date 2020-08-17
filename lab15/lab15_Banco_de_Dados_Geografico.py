#!/usr/bin/env python3

import math

# Laboratorio 15 - Banco de Dados Geografico
# O programa criado consiste em realizar consultas baseadas na distância entre cidades a partir de um banco de dados fornecido na entrada. Podemos realizar a partir deste 4 consultas: Por CEP, cidades por raio, total de habitantes num raio e mediana da população. Tem como saída as respostas das tais consultas.

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Cidade:
    def __init__(self, coordenadas, inicioCEP, fimCEP, numHabitantes):
        self.coordenadas = coordenadas
        self.inicioCEP = inicioCEP
        self.fimCEP = fimCEP
        self.numHabitantes = numHabitantes

def ordem(vet):  # Função de ordenação de listas.
  for i in range(len(vet) - 1):
    min = i
    for j in range(i, len(vet)):
      if vet[min] > vet[j]:
        min = j
    vet[i], vet[min] = vet[min], vet[i]

def menor(vet, inicio): # Função que identifica o indice do menor elemento.
  min = inicio
  for j in range(inicio, len(vet)):
    if vet[min] > vet[j]:
      min = j
  return min

#
# Funcao: distancia
#
# Parametros:
#   a, b: pontos
#
# Retorno:
#   A distancia euclidiana entre a e b.
#
def distancia(c1, c2):
    return int(100 * math.sqrt((c1.x - c2.x)**2 + (c1.y - c2.y)**2)) / 100.0

# Funcao: consulta_cidade_por_cep
#
# Parametros:
#   cidades: lista de cidades (base de dados) 
#       cep: CEP desejado 
# 
# Retorno:
#   O indice da cidade que contem o CEP desejado ou None caso não haja tal cidade.   
#
def consulta_cidade_por_cep(cidades, cep): 
    for i in range(len(cidades)): # busca no banco de dados
      if cep > cidades[i].inicioCEP and cep < cidades[i].fimCEP:
        return i  # retorna indice da cidade que apresenta o cep no intervalo dado    
    return None # retorno vazio caso não haja cep no intervalo

# Funcao: consulta_cidades_por_raio
#
# Parametros:
#            cidades: lista de cidades (base de dados) 
#   cidadeReferencia: indice da cidade referencia (centro da circunferencia)
#               raio: raio da busca
#
# Retorno:
#   Lista dos indices das cidades que estao contidas no raio de busca (incluindo
#   a cidade referencia) *ordenados pelas respectivas distancias da cidade referencia*.
#
def consulta_cidades_por_raio(cidades, cidadeReferencia, raio): 
    listar = [] # lista de distancias de todas as cidades
    listrai = [] # lista de indices em ordem de distancia
    for Cidade in cidades:
      dist = distancia(Cidade.coordenadas, cidades[cidadeReferencia].coordenadas) # calcula as distancias
      listar.append(dist)
    for i in range(len(listar)):
        p = menor(listar, 0) # procura indice do menor elemento
        if listar[p] <= raio:
          listrai.append(p) # se for menor que o raio é adicionado a outra lista o indice
          listar[p] = 10000000000000000 # substitui o menor valor por um numero grande
    return listrai # retorna lista dos indices

# Funcao: populacao_total
#
# Parametros:
#            cidades: lista de cidades (base de dados) 
#   cidadeReferencia: indice da cidade referencia (centro da circunferencia)
#               raio: raio da busca
#          
# Retorno:
#   O numero de habitantes das cidades que estao contidas no raio de busca
#
def populacao_total(cidades, cidadeReferencia, raio):
    numhab = 0 # soma dos habitantes
    for Cidade in cidades:
      dist = distancia(Cidade.coordenadas, cidades[cidadeReferencia].coordenadas)
      if (dist <= raio): # se a distancia for menor que o raio, o numero de hab é adicionado ao total
         numhab = numhab + Cidade.numHabitantes
    return numhab # retorna total de hab

# Funcao: mediana_da_populacao
#
# Parametros:
#            cidades: lista de cidades (base de dados) 
#   cidadeReferencia: indice da cidade referencia (centro da circunferencia)
#               raio: raio da busca
#
# Retorno:
#   Mediana do numero de habitantes das cidades que estao contidas no raio de busca
#
def mediana_da_populacao(cidades, cidadeReferencia, raio): 
    listmed = [] # lista de numero de habitantes
    for Cidade in cidades:
      dist = distancia(Cidade.coordenadas, cidades[cidadeReferencia].coordenadas)
      if (dist <= raio): # adiciona numero de hab a lista caso a distancia seja menor que o raio
        listmed.append(Cidade.numHabitantes)
    ordem(listmed) # ordena a lista de hab
    if (len(listmed) % 2 != 0): # se a lista for de tamanho impar o centro é dado da seguinte forma:
      centro = len(listmed)//2 
      return listmed[centro] 
    else: # se for par é calculada a média dos termos centrais
      media = (listmed[len(listmed)//2] + listmed[len(listmed)//2 - 1])/2
      return media


