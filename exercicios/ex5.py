rodadas = 5
acertos = 0
lista_principal = [['.', '.', '.', '.', '.'],
                   ['.', '.', '.', '.', '.'],
                   ['.', '.', '.', '.', '.'],
                   ['.', '.', '.', '.', '.'],
                   ['.', '.', '.', '.', '.']]

lista_principal02 = [['t', 't', 't', 'a', 'a'],
                    ['a', 'a', 'a', 'a', 't'],
                    ['a', 'a', 'a', 'a', 't'],
                    ['a', 'a', 'a', 'a', 'a'],
                    ['a', 'a', 't', 'a', 't']]




print(f"""            0    1   2   3   4
         0 | {lista_principal[0][0]} | {lista_principal[0][1]} | {lista_principal[0][2]} | {lista_principal[0][3]} | {lista_principal[0][4]} | \n
         1 | {lista_principal[1][0]} | {lista_principal[1][1]} | {lista_principal[1][2]} | {lista_principal[1][3]} | {lista_principal[1][4]} | \n
         2 | {lista_principal[2][0]} | {lista_principal[2][1]} | {lista_principal[2][2]} | {lista_principal[2][3]} | {lista_principal[2][4]} | \n
         3 | {lista_principal[3][0]} | {lista_principal[3][1]} | {lista_principal[3][2]} | {lista_principal[3][3]} | {lista_principal[3][4]} | \n
         4 | {lista_principal[4][0]} | {lista_principal[4][1]} | {lista_principal[4][2]} | {lista_principal[4][3]} | {lista_principal[4][4]} |

""")


def jogar(lista_navios, lista_tiros):
  global acertos, rodadas
  hoz = lista_tiros[0]
  ver = lista_tiros[1]
  lista_principal[hoz][ver] = lista_navios[hoz][ver]
  if lista_principal02[hoz][ver] == 't':
    print("Parabéns você acertou um navio!")
  if lista_principal02[hoz][ver] == 'a':
    rodadas = rodadas - 1
    print("Você errou!")
  if lista_principal[4][2] == 't':
    acertos = acertos + 1
    lista_principal[4][2] = 'x'
    lista_principal[4][1] = 'a'
    lista_principal[4][3] = 'a'
    lista_principal[3][2] = 'a'
    lista_principal[3][3] = 'a'
    lista_principal[3][1] = 'a'
  elif lista_principal[1][4] == 't' and lista_principal[2][4] == 't':
    acertos = acertos + 1
    lista_principal[1][4] = 'x'
    lista_principal[2][4] = 'x'

    lista_principal[0][4] = 'a'
    lista_principal[0][3] = 'a'

    lista_principal[1][3] = 'a'
    lista_principal[2][3] = 'a'

    lista_principal[3][3] = 'a'
    lista_principal[3][4] = 'a'
  elif lista_principal[0][0] == 't' and lista_principal[0][1] == 't' and lista_principal[0][2] == 't':
    acertos = acertos + 1
    lista_principal[0][0] = 'x'
    lista_principal[0][1] = 'x'
    lista_principal[0][2] = 'x'

    lista_principal[0][3] = 'a'
    lista_principal[1][0] = 'a'
    lista_principal[1][1] = 'a'
    lista_principal[1][2] = 'a'
    lista_principal[1][3] = 'a'
  elif lista_principal[4][4] == 't':
    acertos = acertos + 1
    lista_principal[4][4] = 'x'
    lista_principal[4][3] = 'a'
    lista_principal[3][3] = 'a'
    lista_principal[3][4] = 'a'

  print(f"""            0    1   2   3   4
         0 | {lista_principal[0][0]} | {lista_principal[0][1]} | {lista_principal[0][2]} | {lista_principal[0][3]} | {lista_principal[0][4]} | \n
         1 | {lista_principal[1][0]} | {lista_principal[1][1]} | {lista_principal[1][2]} | {lista_principal[1][3]} | {lista_principal[1][4]} | \n
         2 | {lista_principal[2][0]} | {lista_principal[2][1]} | {lista_principal[2][2]} | {lista_principal[2][3]} | {lista_principal[2][4]} | \n
         3 | {lista_principal[3][0]} | {lista_principal[3][1]} | {lista_principal[3][2]} | {lista_principal[3][3]} | {lista_principal[3][4]} | \n
         4 | {lista_principal[4][0]} | {lista_principal[4][1]} | {lista_principal[4][2]} | {lista_principal[4][3]} | {lista_principal[4][4]} |

  """)

# x = horizontal, y = vertical
print('RODADAS: ', rodadas)
h1 = int(input('Digite a cordenada horizontal: '))
v1 = int(input('Digite a cordenada vertical: '))
lista_tiros1 = [h1, v1]
jogar(lista_principal02, lista_tiros1)

print('RODADAS: ', rodadas)
h2 = int(input('Digite a cordenada horizontal: '))
v2 = int(input('Digite a cordenada vertical: '))
lista_tiros2 = [h2, v2]
jogar(lista_principal02, lista_tiros2)

print('RODADAS: ', rodadas)
h3 = int(input('Digite a cordenada horizontal: '))
v3 = int(input('Digite a cordenada vertical: '))
lista_tiros3 = [h3, v3]
jogar(lista_principal02, lista_tiros3)

print('RODADAS: ', rodadas)
h4 = int(input('Digite a cordenada horizontal: '))
v4 = int(input('Digite a cordenada vertical: '))
lista_tiros4 = [h4, v4]
jogar(lista_principal02, lista_tiros4)


print('RODADAS: ', rodadas)
h5 = int(input('Digite a cordenada horizontal: '))
v5 = int(input('Digite a cordenada vertical: '))
lista_tiros5 = [h5, v5]
jogar(lista_principal02, lista_tiros5)


if rodadas > 0 and rodadas <= 5:
  print('RODADAS: ', rodadas)
  h6 = int(input('Digite a cordenada horizontal: '))
  v6 = int(input('Digite a cordenada vertical: '))
  lista_tiros6 = [h6, v6]
  jogar(lista_principal02, lista_tiros6)

  print('RODADAS: ', rodadas)
  h7 = int(input('Digite a cordenada horizontal: '))
  v7 = int(input('Digite a cordenada vertical: '))
  lista_tiros7 = [h7, v7]
  jogar(lista_principal02, lista_tiros7)


  print('RODADAS: ', rodadas)
  h7 = int(input('Digite a cordenada horizontal: '))
  v7 = int(input('Digite a cordenada vertical: '))
  lista_tiros7 = [h7, v7]
  jogar(lista_principal02, lista_tiros7)


  if acertos == 4:
    print(f'rodadas: {rodadas}, acertos: {acertos}')
    print("Parabéns você ganhou!")
elif rodadas == 0:
  print('Você perdeu!')
  print(f'rodadas: {rodadas}, acertos: {acertos}')
  print(f"""            0    1   2   3   4
         0 | {lista_principal02[0][0]} | {lista_principal02[0][1]} | {lista_principal02[0][2]} | {lista_principal02[0][3]} | {lista_principal02[0][4]} | \n
         1 | {lista_principal02[1][0]} | {lista_principal02[1][1]} | {lista_principal02[1][2]} | {lista_principal02[1][3]} | {lista_principal02[1][4]} | \n
         2 | {lista_principal02[2][0]} | {lista_principal02[2][1]} | {lista_principal02[2][2]} | {lista_principal02[2][3]} | {lista_principal02[2][4]} | \n
         3 | {lista_principal02[3][0]} | {lista_principal02[3][1]} | {lista_principal02[3][2]} | {lista_principal02[3][3]} | {lista_principal02[3][4]} | \n
         4 | {lista_principal02[4][0]} | {lista_principal02[4][1]} | {lista_principal02[4][2]} | {lista_principal02[4][3]} | {lista_principal02[4][4]} |

  """)
