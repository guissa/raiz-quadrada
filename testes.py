#produto = float(input('Digite o preço do produto: R$ '))
#produto_desconto = produto - (produto * 5/100)
#print('o seu produto era {:.2f} com desconto ele ficou {:.2f}'.format(produto,produto_desconto))

#salario_funcionario = float(input('Digite o salario do seu funcionario: R$ '))
#novo_salario = salario_funcionario + (salario_funcionario * 15 / 100)
# print('o salario do funcinario era {:.2f}, com o aumento de 15% foi para {:.2f}'.format(salario_funcionario, novo_salario))

#c = float(input('informe a temperatura em °c: '))
#f = 9 + c / 5 + 32
#print('a temperatura de {} °C, corresponde a {} °F'.format(c, f)

#km = float(input('Quantos km percorreu com o carro: '))
#dias = int(input('Quantos dias ficou com o carro: '))
#pago = (dias * 60) + (km * 0.15)
#print(pago)

#import math
#numero = int(input('Digite um numero: '))
#raiz = math.sqrt(numero)
#print('a raiz quadra de {}, é igual a {}'.format(numero, math.ceil(raiz)))

#from math import trunc
#num = float(input('Digite um valor: R$ '))
#print('O valor digitado foi {}, e sua porpoção inteira é {}'.format(num, trunc(num)))

#num = float(input('Digite um numero: '))
#print('O valor digitado foi {}, e a sua porpoção inteira é {}'.format(num, int(num)))   

#from math import hypot
#co = float(input('Digite o comprimento do cateto oposto: '))
#ca = float(input('Digite o comprinmento do cateto adjacente : '))
#hi = hypot(co, ca)
#print('A hipotenusa vai medir {:.2f}'.format(hi))

#import math 
#angulo = float(input('Digite o numero: '))
#seno = math.sin(math.radians(angulo))
#print('O angulo de {:.2f}, tem o seno de {:.2f}'. format(angulo, seno))
#cosseno = math.cos(math.radians(angulo))
#print('O angulo de {:.2f}, tem o cosseno de {:.2f}'.format(angulo, cosseno))
#tangente = math.tan(math.radians(angulo))
#print('O angulo de {:.2f}, tem a tangente de {:.2f}'.format(angulo, tangente))

#from math import radians, sin, cos, tan
#angulo = float(input('Digite o numero: '))
#seno = sin(radians(angulo))
#print('O angulo de {:.2f}, tem o seno de {:.2f}'. format(angulo, seno))
#cosseno = cos(radians(angulo))
#print('O angulo de {:.2f}, tem o cosseno de {:.2f}'.format(angulo, cosseno))
#tangente = tan(radians(angulo))
#print('O angulo de {:.2f}, tem a tangente de {:.2f}'.format(angulo, tangente))

#from math import sqrt
#numero = float(input('Digite um valor: R$ '))
#raiz_numero = sqrt(numero)
#print('O numero digitado foi {}, e a raiz quadrade {}'.format(numero, raiz_numero))

#import random
#nome1 = str(input('Digite seu nome: '))
#nome2 = str(input('Digite seu nome: '))
#nome3 = str(input('Digite seu nome: '))
#nome4 = str(input('Digite seu nome: '))
#lista = [nome1, nome2, nome3, nome4]
#escolhido = random.choice(lista)
#print('O nome sorteado foi {}'.format(escolhido)) 

#from random import shuffle 
#a1 = str(input('Primeiro aluno: '))
#a2 = str(input('Segundo aluno: '))
#a3 = str(input('Terceiro aluno: '))
#a4 = str(input('Quarto aluno: '))
#lista = [a1, a2, a3, a4]
#shuffle(lista)
#print('A ordem sorteada foi: ')
#print(lista)

#nome = str(input('Digite seu nome: ')).strip()
#print('Seu nome em maiusculo é {}'.format(nome.upper()))
#print('Seu nome em minusculo é {}'.format(nome.lower()))
#print('O seu nome tem o total de {} letra'.format(len(nome) - nome.count(' ')))

#number = int(input('number information: '))
#u = number // 1 % 10   
#d = number // 10 % 10
#c = number // 100 % 10
#m = number // 1000 % 10 
#print('analyst namber {}'.format(number))
#print('unidade {}'.format(u))
#print('dezena {}'.format(d))
#print('centena {}'.format(c))
#print('milhar {}'.format(m))

#city = str(input('Digite a cidade que você nasceu: ')).strip()
#print(city[:5].upper() == 'SANTO')

#nome = str(input('Digite seu nome completo: ')).strip()
#print('Seu nome tem silva? {}'.format('silva' in nome.lower()))
 
#frase = str(input('Digite um frase: ')).upper().strip()
#print('A letra A aparece {} vezes'.format(frase.count('A')))
#print('A primeira letra A aparece na posição {}'.format(frase.find('A')))
#print('A ultima letra A aparece na posição {}'.format(frase.rfind('A')))

#nome = str(input('Digite seu nome completo: ')).strip()
#n = nome.split()
#print('Prazer em te conhecer!!')
#print('O seu primeiro nome é {}'.format(n[0]))
#print('O seu ultimo nome é {}'.format(n[len(n)-1]))

#tempo = int(input('Quantos anos tem seu carro? '))
#if tempo <=3:
#    print('Carro velho')
#else: 
#    print('Carro novo')
#print('--FIM--')

#tempo = int(input('Quantos anos tem seu carro? '))
#print('carro novo' if tempo <=3 else'Carro velho')
#print('--FIM--')

#nome = str(input('Digite seu nome: '))
#if nome == 'Guilherme':
#    print('Que nome lindo que voce tem!')
#print('Bom dia {}!'.format(nome))

#n1 = float(input('Digite a primeira nota: '))
#n2 = float(input('Digite a segunda nota: '))
#m = (n1+n2)/2
#print('A sua méda foi {:.1f}'.format(m))
#if m >= 6.0:
#    print('A média foi boa!! PARABÉNS')
#else: 
#    print('A sua média foi ruim!! ESTUDE MAIS')

#import random
#numero = random.randrange(0, 5) 
#usuario = str(input('Descubra o numero entre 0 a 5: '))
#if usuario == numero:
#    print('Você acertou!')
#else: 
#    print('Você errou!') * 7)) 
#else: 
#    print('Tudo certo')
 
#numero = int(input('Digite um numero: ')) 
#if (numero%2) == 0:
#    print('Par')
#else: 
#    print('Impar')

#distancia = int(input('Digite a distancia da viagem: Km/h '))
#if distancia == 200:
#    print('O valor da passagem ficou R${:.2f}'.format(distancia * 0.50))
#else: 
#    print('O valor da passagem ficou R${:.2f}'.format(distancia * 0.45))

#prod = str(input('Qual o nome do produto: '))
#valorprod = int(input('Qual o valor do produto: R$ '))
#limitecart = 4500
#dinheiro = 6000
#if valorprod == limitecart:
#    print('Compra aprovada cartão')
#else:
#    valorprod == dinheiro
#    print('Compra aprovada dinheiro')

#from random import randint
#computador = randint(0, 5) #faz computador "pensar em um numero"
#print('-==' * 20)
#print('Vou pensar em um numero entre 0 & 5, tente adivinhar...')
#print('-=-' * 20)
#jogador = int(input('Em que numero eu pensei? ')) #jogador tenta adivinhar 
#if jogador == computador:    #se 
#    print('PARABÉNS, você acertou!! ')
#else:       #senao 
#   print('ERROU, o numero que eu pensei foi {}'.format(computador))

#from datetime import date
#ano = int(input('Qual ano que analisar? Coloque 0 para saber o ano atul: '))
#if ano == 0:
#    ano = date.today().year
#if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#    print('O ano {} é BISSEXTO'.format(ano))
#else: 
#    print('O ano {} não é BISSEXTO'.format(ano))

#a = int(int(input('Primeiro valor: ')))
#b = int(input('Segundo valor: '))
#c = int(input('Terceiro velor: '))
#menor = a 
#if b<a and b<c:
#    menor = b
#if c<a and c<b:
#    menor = c 
#maior = b 
#if a>b and a>c:
#    maior = a
#if c>b and c>a:
#    maior = c
#print('O menor valor digitado foi {}'.format(menor))
#print('O maior valor digitado foi {}'.format(maior))
 
#funcionario = float(input('Qual o valor do salario: R$ '))
#if funcionario <= 2500:
#    print('O salario com aumento ficou {:.2f}'.format(funcionario + (funcionario * 10 / 100)))
#else: 
#    funcionario > 2500
#    print('O salario com aumento ficou {:.2f}'.format(funcionario + (funcionario * 15 / 100)))

#print('*' * 20)
#print('Analisador...')
#r1 = float(input('Priemiro segmento: '))
#r2 = float(input('Segundo segmento: '))
#r3 = float(input('Terceiro segmento: '))
#if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#    print('O segmento acima podem formar um triangulo')
#else:
#    print('O segmento acima nao podem formar um triangulo')

#emprestimo = int(input('Qual o valor do emprestimo: R$ '))
#pagamento = int(input('Quantos anos para quitar a divida: '))
#valor_salario = int(input('Digite o valor do seu salario: R$ '))
#banco = emprestimo / pagamento
#if banco >= valor_salario:
#    print('O valor do seu emprestimo ficou R${:.2f}, porém você recebe R${:.2f}, \ne por esse motivo não foi autorizado'.format(banco, valor_salario))
#else:
#    print('Emprestimo APROVADO! O valor mensal ficou R${:.2f}, ele é compativel com sua renda de R$ {:.2f}'.format(banco, valor_salario))


#salario = int(input('Digite o valor do seu salario: R$ '))
#nv = salario - 30 / 10
#print(nv)

#numero = int(input('Digite um numero: '))
    #print('analisando o valor {}, o seu antecessor é {} e o seu sucessor é {}'.format(numero, (numero-1), (numero+1)))

    #numero = int(input('Digite um valor: '))
    #print('O dobro de {}, vale {}'.format(numero, (numero*2)))
    #print('O triplo de {} vale {}. \n A raiz quadrade de {} é igual a {:.2f}'.format(numero, (numero*3), numero, (numero**(1/2))))

    #n1 = float(input('Primeira nota do aluno: '))
    #n2 = float(input('Segunda nota do aluno: '))
    #média = (n1 + n2) / 2
    #print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, média))

    #frase = str(input('Digite uma frase: ')).strip().upper()
#palavras = frase.split()
#junto = ''.join(palavras)
#inverso = ''
#for letra in range(len(junto) -1, -1, -1):
#    inverso += junto[letra]
#    print('O inverso de {} é {}'.format(junto, inverso))
#if inverso == junto:
#    print('Temos um palíndromo')
#else:
#    print('A frase digitada não é um palíndromo')

#from datetime import date
#atual = date.today().year
#totmaior = 0 
#totmenor = 0
#for pess in range(1, 8):
#    nasc = int(input('Em que ano a {}º pessoa nasceu: '.format(pess)))
#    idade = atual - nasc 
#    if idade >= 18:
#        totmaior += 1 
#    else:
#        totmenor += 1
#print('Ao todo tivemos {} pessoas maior de idade'.format(totmaior))
#print('E tivemos também {} pessoas menor de idade'.format(totmenor))

#maior = 0
#menor = 0 
#for pess in range(1, 6):
#    peso = float(input('Qual o peso da {}º pessoa: '.format(pess)))
#    if pess == 1:
#       maior = peso
#        menor = peso
#    else:
#        if peso > maior:
#            maior = peso
#        if peso < menor:
#            menor = peso
#print('O maior peso lido foi {}Kg'.format(maior))
#print('O menor peso lido foi {}Kg'.format(menor))

#soma = 0
#media = 0
#mhomem = 0
#nvelho = '' 
#totmulher20 = 0
#for p in range(1, 5):
#    print('----{}º PESSOA-----'.format(p))
#    nome = str(input('Nome: ')).strip()
#    idade = int(input('Idade: '))
#    sexo = str(input('Sexo [F/M]: ')).strip()
#    soma += idade
#    if p == 1 and sexo in 'Mm':
#        mhomem = idade
#    nvelho = nome
#    if sexo in 'Mm' and idade > mhomem:
#        mhomem = idade
#        nvelho = nome
#    if sexo in 'Ff' and idade < 20:
#        totmulher20 += 1  

#media = soma / 4 
#print('A média de idade do grupo é de {} anos'.format(media))
#print('O homem mais velho do grupo tem {} anos e se chama {}'.format(mhomem, nvelho))
#print('Total de mulheres com menos de 20 anos é {}'.format(totmulher20))































