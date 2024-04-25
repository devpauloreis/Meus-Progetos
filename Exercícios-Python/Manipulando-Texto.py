'''
                          FATIAMENTO

frase = C u r s o   e m   V í  d  e  o     P  y  t  h  o  n \n
        0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
frase[9]      == V
frase[9:13]   == Víde
frase[9:21]   == Vídeo Python
frase[9:21:2] == VdoPto
frase[:5]     == Curso
frase[15:]    == Python
frase[9::3]   == VePh
OBS: Quando não tem o número definido no inicio, supõe que é 0
     Quando não tem o número definido no final, é até o último caractere 

 ------------------------------------------------------------                           
                            
                            ANÁLISE

frase = C u r s o   e m   V í  d  e  o     P  y  t  h  o  n \n
        0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

len[frase] == 21        
Número de caracteres

frase.count('o') = 3
Quantidade de 'o' que aparecem na string

frase.count('o',0,13) == 1
Quantidade de 'o' que aparecem na string, entre o caractere 0 e 13
OBS: O cararactere 13 NÃO contabiliza

frase.find('deo') == 11
Em qual parte da string é encontrado o primeiro 'deo'

'Curso' in frase == True

------------------------------------------------------------

                        TRANFORMAÇÃO 

frase = C u r s o   e m   V í  d  e  o     P  y  t  h  o  n \n
        0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
                        
frase.replace('Python','Android') == Curso em Vídeo Android
Vai reposicionar/trocar 'Python' pela palavra 'Android'

frase.upper() == CURSO EM VÍDEO PYTHON
Transforma todas as letras minúsculas em maiúsculas

frase.lower() == curso em vídeo python
Transforma todas as letras maiúsculas em minúsculas

frase.capitalize() == Curso em vídeo python
Transforma todas as letras em minúsculas e depois coloca SOMENTE a primeira letra em maiúsculo

frase.title() == Curso Em Vídeo Python
Transforma toda primeira letra de uma palavra(após o espaço) em maiúscula

*** Outra string ***
frase = '   Aprenda Python  '

frase.strip() = 'Aprenda Python'
Remove todos os espaços inúteis no início e no final da string

frase.rstrip() == '   Aprenda Python'
Remove todos os espaços inúteis a direita da string e MANTÉM os da esquerda

frase.lstrip() == 'Aprenda Python  '
Remove todos os espaços inúteis a esqueda da string e MANTÉM os da direita

------------------------------------------------------------------

                             DIVISÃO

frase = C u r s o   e m   V í  d  e  o     P  y  t  h  o  n \n
        0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

frase.split() == ['Curso', 'em', 'Vídeo', 'Python']  
Vai dividir a string considerando os espaços, gera uma lista 

* JUNÇÃO
'-'.join(frase) == Curso-em-Vídeo-Python

print(frase.splite()[1][0]) == e
Para quando eu quiser retirar um caractere dentro de uma palavra em uma lista

------------------------------------------------------------------

DICA
print("""Tudo o que for escrito aqui vai ser mostrado no terminal como um único texto""")
'''