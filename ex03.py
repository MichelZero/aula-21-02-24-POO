# 2. (3 pontos) Escreva uma função em Python que recebe 
# dois números inteiros como entrada e retorna o 
# maior divisor comum (MDC) desses números. 
# A função deve ser chamada mdc e deve ter a seguinte assinatura:
def mdc(a, b):
  """
  Retorna o máximo divisor comum de dois números.

  Argumentos:
    a: O primeiro número inteiro.
    b: O segundo número inteiro.

  Retorno:
    O MDC de 'a' e 'b'.
  """
  # Implemente a função
  
def mdc(a, b):
  """
    Retorna o máximo divisor comum de dois números.

    Argumentos:
      a: O primeiro número inteiro.
      b: O segundo número inteiro.

    Retorno:
      O MDC de `a` e `b`.
  """
  while b > 0:
    print(f"{a}, {b}")
    a, b = b, a % b
  return a

a = int(input("informe o valor de A: "))
b = int(input("informe o valor de B: "))
print(mdc(a,b))