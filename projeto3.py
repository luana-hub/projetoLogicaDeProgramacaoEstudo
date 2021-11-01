'''
Projeto- Medidor de velocidade
2- O que devo fazer com esses dados?
Levando em consideração a velocidade máxima de 80km em uma determinada rua.Crie uma programa que recebe do usuário uma valor que representa a velocidade e com base nessa velocidade diga se ela tomou uma multa grave,leve ou gravíssima.Levando em consideração que se  a pessoa estiver abaixo da velocidade máxima permitida seu programa de ve exibir'não houve multa',se estiver 10km acima da velocidade  máxima permitida deve exibir' levou multa leve',se estiver entre 11 e 20km acima da velocidade máxima permitida deve exibir' levou multa grave' e se etiver acima de 20km da velocidade máxima permitida deve exibir' levou mukta gravíssima'

MÉTODO 5Q's

Analise críticamente o problema e descubra:
(Explique o problema para sí mesmo em voz alta,peça mais informações/investigue até que vc tenha a completa compreenção do problema.)
1- Quais os dados de entrada necessários?
-velocidade
2-O que devo fazer com esses dados?
-caso a velocidade seja abaixo da máxima permitida devo exibir'não houve multa'.
-caso a velocidade seja 10km acima da máxima permitida devo exibir' levou multa leve'.
-caso a velocidade seja entre 11 e 20km devo exibir'levou multa grave'.
se for acima de 20km da máxima permitida devo exibir' levou multa gravíssima'.
3- Quais são as restrições do problema?

4- Qual é o resultado esperado?
o resultado esperado é exibir a mensagem  que corresponde ao nível multa recebida pelo condutor.(abaixo da maxima: não houve multa,10km acima da máxima: levou multa leve,entre 11 e20 km acima da máxima: levou multa grave,20km acima da máxima: levou multa gravíssima.)
5- Qual é a sequencia de passos a ser feita para chegar ao resultado esperado?

input velocidade
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
  print 'não houve multa'
if velocidade > velocidade_maxima e  velocidade <= velocidade_maxima +10:
print 'levou multa leve'
if velocidade > velocidade_maxima +11 e velocidade <= velocidade_maxima +20:
  print 'levou multa grave'
if velocidade < velocidade_maxima +20:
  print' levou multa gravísssima'
'''

velocidade = int(input('Digite sua velocidade: '))
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
  print('Não houve multa')
elif velocidade > velocidade_maxima and velocidade<= velocidade_maxima +10:
  print('Levou multa leve')
elif velocidade >= velocidade_maxima + 11  and velocidade <= velocidade_maxima +20:
  print('Levou multa grave')
elif velocidade > velocidade_maxima +20:
  print('Levou multa gravíssima')