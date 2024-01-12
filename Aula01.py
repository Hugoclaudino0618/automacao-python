#Aula 01 do curso de automação por python

#Exercicios 01 e 02 são referentes a essa aula

#este é um exemplo para que possa ser visto a variavel e seu tipo
#type é o responsavel pela denominação doo tipo de variavel
#Já no caso dos numeros decimais format(variavel, ".xf") 
#format é o responsavel pela alteração e ".xf" com x representando a quantidades de casas apos a virgula

#Variaveis (Programa01)
nome = "Hugo Paulo Claudino\n"
idade = 22
cpf = "462.305.628-71\n"
nascimento = "10/07/2001\n"

#Atribuindo em sequência (Programa02)
teste1, teste2, teste3, teste4, teste5 = "teste 1\n", "teste 2\n", "teste 3\n", "teste 4\n", "teste 5 \n"

#Atribuindo o mesmo valor em variaveis diferentes (Programa03)
var1 = var2 = var3 = var4 = var5= "\nSou a original, confia\n"

#Descompactação de variaveis (Programa04)
Exemplo = "Primeiro\n", "Segundo\n", "Terceiro\n", "Quarta\n", "Último\n"
p1, p2, p3, p4, p5 = Exemplo

#Delimitando casas decimais (Programa05)
n1 = 3
n2 = 2
soma = (n1 + n2) / 3

#Programa1
print("Teste de exibição:", " \n", type(nome),"Nome completo: ", nome,
      type(idade), "Idade: ", idade,
      "\n", type(cpf), "CPF: ",cpf, 
      type(nascimento), "Nascido em: ", nascimento)

#Programa2
print("\nSequência de variáveis\n", 
      type(teste1), teste1,
      type(teste2), teste2,
      type(teste3), teste3,
      type(teste4), teste4,
      type(teste5), teste5)

#Programa3
print("Me diga agora quem é a original \n Var 1 diz:", var1,
      "Var 2 diz:", var2,
      "Var 3 diz:", var3,   
      "Var 4 diz:", var4,
      "Var 5 diz:", var5,)

#Programa4
print("Descompactação de variáveis:\n", p1, p2, p3, p4, p5)

#Programa5
print("Delimitação das casas decimais 3 + 2\n",
    "A soma com 1 casa é:", format(soma, ".1f" ), "\n",
    "A soma com 2 casas é:", format(soma, ".2f"), "\n",
    "A soma com 3 casas é:", format(soma, ".3f"), "\n",
    "A soma sem nenhuma casa é:", format(soma, ".0f"),)
