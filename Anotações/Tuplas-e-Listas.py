'''
====================================== TUPLAS ========================================

TUPLAS SÃO IMUTÁVEIS
Nas tuplas se usa os parênteses:
Lanche = ('Hambúrguer', 'Refri', 'Pizza', 'Pudim')
Não tem como adicionar/remover nada da tupla nem mudar nenhuma das suas variáveis



====================================== LISTAS =========================================

LISTAS SÃO MUTÁVEIS
Nas listas se usa os colchetes: 
Lanche = ['Hambúrguer', 'Refri', 'Pizza', 'Pudim']
Tem a possibilidade de adicionar/remover novas variaveis e também sobreescrever uma variável já existente

SOBREESCREVER
Lanche[3] = 'Picolé'
Resultado:
['Hambúrguer', 'Refri', 'Pizza', 'Picolé']

ADICIONAR NOVA STRING
Lanche.append('Biscoito')
Resultado: 
['Hambúrguer', 'Refri', 'Pizza', 'Picolé', 'Biscoito']

ADICIONAR EM LUGAR ESPECÍFICO
Lanche.insert(0, 'Cachorro quente')
Resultado: 
['Cachorro quente', 'Hambúrguer', 'Refri', 'Pizza', 'Picolé', 'Biscoito']

REMOVER UMA STRING
del Lanche[3]
lanche.pop(3)
lanche.remove('Pizza')
Resultado de qualquer um deles:
['Cachorro quente', 'Hambúrguer', 'Refri', 'Picolé', 'Biscoito']




******
CRIAR UMA LISTA
valores = list(range(4, 11)) #obs: o 11 não conta no python
Resultado:
[4, 5, 6, 7, 8, 9, 10]

ORGANIZAR UMA LISTA
valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort()
Resultado:
[0, 2, 3, 4, 5, 8, 9]
valores.sort(reverse=True)
Resultado:
[9, 8, 5, 4, 3, 2, 0]

CONTAR QUANTOS ELEMENTOS TEM
len(valores)
Resultado:
7

'''