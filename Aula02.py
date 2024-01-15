#Input é a função que permite a entrada de dados na variável 
nome = input("Digite aqui seu nome: \n")
print(f"\nBem vindo a nossa calculadora de média, {nome} \n")
nota1 = input("Por favor insira sua primeira nota final do semestre: \n")
nota2 = input("Por favor insira sua segunda nota final do semestre: ")

#Input retorna como string, desse modo abaixo podemos formata-lo para utilizar contas com as variaveis
media = (float(nota1) + float(nota2)) / 2 
#ou podemos utilizar a float da seguinte maneira:
#nota1= float(input""Por favor insira sua primeira nota final do semestre: \n""))

#usando uma f-string (f) podemos facilitar a escrita das diferentes variaveis
#na aula foi ensinado a utilizar float mas foi de minha preferencia usar f-string

#if e else precisam de ":" em python
if media >= 7.0:
    print(f"\nParabéns você foi aprovado com a nota final de : {media}")
else:
    print(f"\nQue pena, infelizmente você foi reprovado com a nota final de :  {media} \n")