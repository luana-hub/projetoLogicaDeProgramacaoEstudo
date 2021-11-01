#Projeto chute o número
'''
Escreva uma programa que ao inciar gera um valor aleatório de 1 a 10 e permite que o usuário chute um número até que o valor  aleatório gerado no início do programa seja chutado corretamente.

O programa deve informar se o chute foi acima, abaixo ou igual ao valor  aleatório gerado no inicio do programa.

# Método 5Q' para montar algorítimo:
Analise criticamente o problema e descubra:
(Tente explicar o problema em voz alta para sí mesmo e peça mais informações/ investigue mais até você compreender complemente o problema.)

1- Quais são os dados de entrada necessários?
-valor aleatório de 1 a 10
-chute do usuário
2- O que devo fazer com esse dados?
-eu devo comparar o chute do usuário com o valor aleatório gerado no início do programa e dizer se o chute foi maior , menor ou igual ao que foi gerado no inicio do programa.
3- Quais são as restrições desse problema?
-valor gerado de 1 a 10.
4- Qual é o resultado esperado?
-o programa deve informar se o chute foi maior, menor ou agual ao valor aleatório gerado no inicio do programa.
5- Qual é a sequência de passos  a ser feita para chegar ao resultado esperado?
input  valor_aleatorio de 1 a 10
input  chute
if chute > valor_aleatorio:
  print'chute foi maior que o valor gerado'
if chute < valor_aleatorio:
  print'chute foi menor que valor gerado'
if chute = valor_aleatorio:
  print'Parabéns você acertou'

'''
import random
# while-é uma condição exemplo: enquando a variável acertou for falsa o programa vai seguir rodando.

valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
  chute = int(input('Chute uma valor de 1 a 10:'))
  if chute > valor_aleatorio:
    print('Chute foi maior que o valor gerado.')
  elif chute < valor_aleatorio:
    print('Chute menor que valor gerado.')
  elif chute == valor_aleatorio:
    acertou = True
    print('Parabéns você acertou!')
