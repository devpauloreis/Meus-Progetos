tabela = ('Botafogo', 'Palmeiras', 'Flamengo', 'Grêmio',
          'Fluminense', 'Athletico-PR', 'Atlético-MG',
          'São Paulo', 'Fortaleza', 'Internacional',
          'Corinthians', 'Cruzeiro', 'Cuiabá', 'Goiás',
          'Bahia', 'Santos', 'Vasco da Gama', 'Coritiba',
          'América-MG', 'Chapecoense')
print('-='*20)
print(f'Lista de times do Brasileirão: {tabela}')
print('-='*20)
print(f'Os primeiros 5 colocados foram: {tabela[:5]}')
print('-='*20)
print(f'Os últimos 4 colocados foram: {tabela[-4:]}')
print('-='*20)
print(f'Os times em ordem alfabética são: {sorted(tabela)}')
print('-='*20)
print(f'O time Chapecoence esta na {tabela.index("Chapecoense")+1}ª posição ')