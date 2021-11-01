#Fatorial de um numero
'''
Crie um programa que ao receber um número,imprima o fatorial do mesmo.
#Método 5Qs para montar um algorítimo:
Analise criticamente o problema e descubra:
(Tente explicar esse problema pra vc mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)

1- Quais são os dados  de entrada necessários?
numero
2- O que devo fazer com esses dados?
Eu devo calcular o fatorial que for passado para meu preograma e o exibir na tela.
3- Quais são as restrições desse problema?
-o numero deve ser um valor positivo.
-o numero deve ser um valor inteiro
4- Qual resultado esperado?
-o resultado esperado é que o resultado do valor providenciado seja exibido. 
5- Qual é a sequência de passos  a ser feita para chegar ao resultado esperado? 

input numero
if numero > 0
if numero = inteiro
fatorial = 1
loop de 1 a numero
 fatorial = fatorial * numero
 print(fatorial)
 #int- coverte a string em número
'''
numero = int(input("Digite um número"))
if numero > 0:
  fatorial = 1
  for item in range(1,numero +1):
    fatorial = fatorial * item
  print(fatorial)

