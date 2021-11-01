#Coleções(listas)
preco_1 = 20
preco_2 = 50
preco_3 = 200
#lista
preco = [20,50,200]
#         0, 1,  2
print(preco[0])
#descubrindo o índece através do ítem desejado.
print(preco.index(200))
#Lista
diversidades = [15, 'Jhonatan', True]
print(diversidades[0])
print(diversidades[1])
print(diversidades[2])
#uso de laço de repetição
for preco in preco:
  print(preco)
  '''
  Exemplo: Some os valores
  Dados uma coleção de dados'idades'[15,42,75,34,26], imprima na tela a soma desses valores.
  idades = [15,42,75,34,26]
  total = 0
  loop idades em dados
  total = total + idades
  print total
  '''
  idades = [15,42,75,34,26]
  total = 0
  for idade in idades:
    total = total + idade
    print(total)
