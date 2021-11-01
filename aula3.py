#Laços de Repetição - Listas
# Problema 1a N - Imprima os valores de 1 a N.
'''
input numero maximo
valor inicial = 1
loop de valor_inicial a numero_maximo
  print valor
'''
valor_maximo = int(input('Digite valor maximo'))
valor_inicial = 1
for numero in range(valor_inicial,valor_maximo + 1):
  print(numero)
