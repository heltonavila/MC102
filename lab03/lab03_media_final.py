# O programa criado tem como objetivo calcular a média final dos alunos de MC102. Primeiramente, pede-se como entrada os valores da prova 1, prova 2 e média dos laboratórios realizados. Como saída, são dadas a média das provas, a média antes da realização do exame e a média final. Caso a média antes do exame esteja entre 2.5 e 5.0, o programa ainda pede a inserção da nota do exame para o cálculo da média final antes de imprimir os 3 valores que estão expressos na saída. 

p1 = float(input())
p2 = float(input())
ml = float(input())

mp = (2*p1 + 3*p2)/5

if (ml == 0) and (mp == 0): 
  med = 0
else:
  med = (3*mp*ml)/(mp + 2*ml)

if (2.5 <= med < 5): #Caso a média esteja entre 2.5 e 5 é pedida a  nota do exame e é feito o cálculo da média final. 
  ex = float(input())
  f = (med + ex)/2
  if (f >= 5): #Caso a média final seja maior que 5, a nota final do aluno é reduzida a 5.
    f = 5
else: #Sendo a média final menor que 5, o aluno é reprovado e sua nota final é a própria média final.
  f = med

print("%.1f" %mp)
print("%.1f" %med)
print("%.1f" %f) 




