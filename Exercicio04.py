"""

Exercício: Tabuada Personalizada

Escreva um programa que solicite ao usuário um número inteiro e exiba a tabuada desse número, do 1 ao 10.

Entrada:

    Um número inteiro n, representando o número do qual você deseja ver a tabuada.

Saída:

    O programa deve imprimir dez linhas, mostrando o resultado da multiplicação do 
    número digitado com os números de 1 a 10, no formato n * i = resultado, onde n é o número 
    digitado pelo usuário e i varia de 1 a 10.
"""
#essa é a minha versão
base = int(input("Digite o numero que deseja saber a tabuada: "))
b1 = base * 1
b2 = base * 2
b3 = base * 3
b4 = base * 4
b5 = base * 5
b6 = base * 6
b7 = base * 7
b8 = base * 8
b9 = base * 9
b10 = base * 10
print(f"\nA tabuada numero {base} é: \n")
print(f"{base} X 1 = {b}")
print(f"{base} X 2 = {b2}")
print(f"{base} X 3 = {b3}")
print(f"{base} X 4 = {b4}")
print(f"{base} X 5 = {b5}")
print(f"{base} X 6 = {b6}")
print(f"{base} X 7 = {b7}")
print(f"{base} X 8 = {b8}")
print(f"{base} X 9 = {b9}")
print(f"{base} X 10 = {b10}")

"""Codigo da aula:
nDigitado = int(input("A tabuada de qual número você deseja ver? "))
print(nDigitado, "* 1 =", nDigitado * 1)
print(nDigitado, "* 2 =", nDigitado * 2)
print(nDigitado, "* 3 =", nDigitado * 3)
print(nDigitado, "* 4 =", nDigitado * 4)
print(nDigitado, "* 5 =", nDigitado * 5)
print(nDigitado, "* 6 =", nDigitado * 6)
print(nDigitado, "* 7 =", nDigitado * 7)
print(nDigitado, "* 8 =", nDigitado * 8)
print(nDigitado, "* 9 =", nDigitado * 9)
print(nDigitado, "* 10 =", nDigitado * 10)
"""