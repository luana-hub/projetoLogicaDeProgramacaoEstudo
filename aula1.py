#variáveis
#números
velocidade_internet = 10
print(velocidade_internet)
nota_filme = 8.5 #float
#valores boleanos
esta_aberto = True #ou False
#strings
nome_do_curso = "Lógica de Programação"#strig é a inserção de texto

#como variáveis seriam usadas em um programa real?
#Problema 1 Valor por hora
#escreva um programa que retorna o valor hora de um funcionário com base em seu salário mensal e horas trabalhadas por mês.
''''
input salario_mensal
input horas_trabalhadas_por_mes
valor_hora = salario_mensal / horas_trabalhadas_por_mes
print valor_hora
'''
salario_mensal = input('Qual é o seu salario mensal? ')
horas_trabalhadas_por_mes = input('Quantas horas trabalha por mês? ')
valor_hora = int(salario_mensal) / int(horas_trabalhadas_por_mes)
print(valor_hora)