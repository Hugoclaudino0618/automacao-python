"""
Solicita ao usuário que insira seu nome e duas notas, calcula a média dessas notas e, 
em seguida, imprime uma mensagem contendo o nome do aluno e a média calculada. 

Vamos analisar cada parte do código:

    nome = input("Digite seu nome"): Solicita ao usuário que digite seu nome e 
    armazena o valor inserido na variável nome.

    nota1 = float(input("Digite a nota 1")): Solicita ao usuário que digite a 
    primeira nota, converte o valor inserido para um número de ponto flutuante usando 
    float(), e armazena o resultado na variável nota1.

    nota2 = float(input("Digite a nota 2")): Semelhante à linha anterior, solicita ao 
    usuário que digite a segunda nota, converte o valor inserido para um número de ponto 
    flutuante e armazena o resultado na variável nota2.

    media = (nota1 + nota2) / 2: Calcula a média das duas notas somando nota1 e nota2, e dividindo 
    o resultado por 2. A média é armazenada na variável media.

    print("Aluno ", nome, " Média: ", media): Imprime uma mensagem formatada contendo o nome do 
    aluno e a média calculada. A função print() pode receber vários argumentos separados 
    por vírgulas, e imprimirá cada um deles sequencialmente, separados por um espaço. 
    
    O resultado final combina os valores das variáveis nome e media com as strings 
    literais para criar a saída completa.

"""
#Exercicio 02 
# 1. Crie uma variavel chamada "nota1" e atribua o valor 7.5 à ela
nota1 = 7.5
# 1. Crie uma variavel chamada "nota1" e atribua o valor 8.2 à ela
nota2 = 8.3
# 1. Crie uma variavel chamada "nota1" e atribua o valor 6.9 à ela
nota3 = 6.9
# 1. Calcule a media das tres notas o resultado a uma variavel chamada "média"
media = (nota1 + nota2 + nota3) / 3
# 1. Imprima na tela o valor da variavel "média" formatada com duas casas decimais
print("A média é:", format(media, ".2f"))