'''
FIXO - \033[ Style ; Text ; Back m
   ex: \033[0;33;44m

Style
0 None      / Sem estilo
1 Bold      / Negrito
4 Underline / Sublinhado
7 Negative  / Inverte o fundo e a letra

Text
30 Branco
31 Vermelho
32 Verde
33 Amarelo
34 Azul
35 Magenta
36 Ciano
37 Cinza

Back
40 Branco
41 Vermelho
42 Verde
43 Amarelo
44 Azul
45 Magenta
46 Ciano
47 Cinza

se quiser fundo branco e letra preta, usa o negative do style
\033[7;30m

# print Olá, Mundo! com fundo lilás, sublinhado e com letra branca
print('\033[4;30;45mOlá Mundo!\033[m')
obs: depois do ola mundo as letras vão sair no padrão por causa do comando no final "\033[m"
'''