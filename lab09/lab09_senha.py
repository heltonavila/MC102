# O programa consiste em analisar se a senha proposta pelo usuário está nos
# padrões necessários. De início, o programa pede um número n de palavras
# que serão adicionadas a uma lista que representa um dicionário. Logo depois,
# é requisitada a entrada de n palavras para esse dicionário, uma de cada vez.
# Por fim, é necessário entrar com a senha proposta e assim será analisado se
# a senha está nos padrões. Os padrões são: A senha deve conter pelo menos 8
# caracteres, 1 letra maiúscula, 1 minúscula, 1 número, 1 símbolo, não pode ser
# palíndromo e nem conter palavras reservadas do dicionário. Caso um dos padrões
# seja violado, o programa informa como saída quais foram violados. Caso
# contrário, é recebido como saída "ok".

n = int(input()) # número de palavras do dicionário
dic = [] # lista vazia para armazenar palavras 
alfaM = 'QWERTYUIOPASDFGHJKLZXCVBNM' # letras maiúsculas 
alfam = 'qwertyuiopasdfghjklzxcvbnm' # letras minúsculas
num = '1234567890' # números
simb = '!?#@$' # símbolos

for i in range(n): # adiciona as palavras digitadas ao dicionário
    a = input()
    dic.append(a)

senha = input() # pede a senha

# Deve conter pelo menos 8 caracteres

if(len(senha) < 8):
    print("A senha deve conter pelo menos 8 caracteres")

# Deve conter pelo menos uma letra maiúscula

nmai = 0 # variável para o número de letras maiusculas da senha

for i in range(len(senha)):
    for j in range(len(alfaM)):
        if (senha[i] == alfaM[j]):
            nmai = nmai + 1

if (nmai < 1): 
  print("A senha deve conter pelo menos uma letra maiuscula")

# Deve conter pelo menos uma letra minúscula

nmin = 0 # variável para o número de letras minusculas da senha

for i in range(len(senha)):
    for j in range(len(alfam)):
        if (senha[i] == alfam[j]):
            nmin = nmin + 1

if (nmin < 1):
  print("A senha deve conter pelo menos uma letra minuscula")
  
# Deve conter pelo menos um número

nnum = 0 # variável para o número de números da senha

for i in range(len(senha)):
    for j in range(len(num)):
        if (senha[i] == num[j]):
            nnum = nnum + 1

if (nnum < 1):
  print("A senha deve conter pelo menos um numero")
  
# Deve conter pelo menos um símbolo

nsim = 0 # variável para o número de simbolos da senha

for i in range(len(senha)):
    for j in range(len(simb)):
        if (senha[i] == simb[j]):
            nsim = nsim + 1

if (nsim < 1):
  print("A senha deve conter pelo menos um simbolo")
  
# Não pode ser um palíndromo

for i in range(len(senha)):
    palim = False 
    if (senha[i] == senha[-1 - i]): # Compara os termos da senha de fora pra dentro
        palim = True # Se os termos forem iguais, torna o indicador verdadeiro.
    else:
        palim = False
        break
            
if (palim == True):
    print("A senha e um palindromo")

# Não pode conter nenhuma palavra reservada de um dicionário

b = list(senha) # cria uma lista com os termos da senha

for p in range(len(senha)):  # verifica se há letras maiusculas 
    for m in range(len(alfaM)):
        if (b[p] == alfaM[m]):
            b[p] = alfam[m] # troca maiusculas por minusculas 

senhan = "".join(b) # junta os termos da lista de termos da senha

npal = 0 # variável para o número palavras do dicionario na senha

for g in range(len(senhan)): # verifica se há palavras do dicionário
  for i in range(n):
    if (senhan[g:g+len(dic[i])] == dic[i]):
        npal = npal + 1

if (npal >= 1):        
  print("A senha nao pode conter palavras reservadas")


if (npal < 1) and (palim == False) and (nsim >= 1) and (nnum >= 1) and (nmin >= 1) and (nmai >= 1) and (len(senha) > 8):
  print("ok") # Imprime ok se nenhum dos padrões foram quebrados

