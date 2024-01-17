"""
Exercício

Crie um algoritmo que solicite o ano de nascimento do usuário e 
com base no ano corrente imprima a idade

"""

ano_atual = 2023
ano_nascimento = int(input("Digite o ano de nascimento: "))

idade = ano_atual - ano_nascimento

print("Sua idade é:", idade)