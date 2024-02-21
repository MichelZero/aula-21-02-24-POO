# 1 -  Escreva uma função que recebe dois parâmetros 
# e imprime o menor dos dois. 
# Se eles forem iguais, imprima 
# que eles são iguais, teste a função.

# exemplo de função
import math

def potencia(x, y):
  """
  Purpose: recebe x e y, retorna x^y
  """
  # return x**y
  return math.pow(x,y)
# end def

""" x = int(input("informe o valor de X: "))
y = int(input("informe o valor de y: "))
print(f"x^y = {potencia(x,y)}") """


# função encontrar menor ou iguais
def menor2(x, y):
  """
  Args:
      x (int): valor inteiro
      y (int): valor inteiro

  Returns:
      int: retorna o menor valor, ou a 
      string "Os números são iguais"
  """
  
  if x < y:
      return x
  elif y < x:
      return y
  else:
      return 'Os números são iguais'
    

x = int(input("informe o valor de X: "))
y = int(input("informe o valor de y: "))
print(menor2(x,y))