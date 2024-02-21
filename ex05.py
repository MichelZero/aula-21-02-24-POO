# 3 - Escreva um aplicativo calculadora, ele 
# deve solicitar ao usuário as entradas de valores e 
# qual a operação a realizar.

# funções
def somar(a, b):
  return a + b

def subtrair(a, b):
  return a - b

def multiplicar(a, b):
  return a * b

def dividir(a, b):
  if b <= 0:
    return "erro: divisão por zero!"
  else:
    return a / b
  
x = int(input("informe o valor de X: "))
y = int(input("informe o valor de Y: "))
  
while True:
  print("1 - somar")
  print("2 - subtrair")
  print("3 - multiplicar")
  print("4 - dividir")
  print("5 - Sair")
  print("escolha a operação (1..5)")
  valor = int(input(": "))
  
  if valor == 1:
    print(f"{x} + {y} = {somar(x,y)}")
    
  elif valor == 5:
    break
  else:
    print("informe um opção de 1 a 5: ")