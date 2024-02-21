# 2-  Escreva uma função que recebe um número n como 
# parâmetro e imprime se n é nulo, positivo ou negativo, 
# teste a função.

def numero(n):
  if n > 0:
    return 'positivo'
  elif n < 0:
    return 'negativo'
  else:
    return 'nulo'
  
# teste função

x = int(input("informe um valor: "))
print(f"o valor {x}, é {numero(x)}")
