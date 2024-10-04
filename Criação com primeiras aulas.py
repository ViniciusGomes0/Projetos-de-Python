inicio = input('Olá 👋, podemos começar? ')
nome= input('Primeiramente, fale seu nome, por favor?')
print('Prazer {}'.format(nome))
aniversario = input('Iremos perguntar sua data de aniversário, pode me falar?')
print('Então você nasceu no dia {}. Correto?'.format (aniversario))
idade = input ('Agora iremos você fazer uma soma, do seu aniversário de hoje com o do ano passado, exemplo 31+33, ok?')
n1= int (input ('Digite um número do seu aniversário deste ano, exemplo 33:'))
n2 = int(input('Ótimo, agora digite o numero do ano passado, exemplo 32:'))
s=n1+n2
print('A soma vale',s)
n3= int(input ('Um valor:'))
n4= int(input (' Outro valor:'))
n5 = int(input ('Mais um:'))
n6 = int(input ('Ultimo:'))
a=n3+n4
m=n5*n6
print ('A soma vale {} e a multiplicação vale {}'. format(a, m))
import math
num = float(input('Vamos calcular agora uma algoritimo como seu dobro, triplo e raiz quadrada, ok? Digite um número:'))
print ('A raiz quadrada de seu número é {}'.format(num))
frase = 'Aprendendo programar'
print (frase[3:12])






