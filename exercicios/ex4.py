lista_principal = [['.', '.', '.', '.', '.'],
                   ['.', '.', '.', '.', '.'],
                   ['.', '.', '.', '.', '.'],
                   ['.', '.', '.', '.', '.'],
                   ['.', '.', '.', '.', '.']]

lista_principal02 = [['t', 't', 't', 'a', 'a'],
                    ['a', 'a', 'a', 'a', 't'],
                    ['a', 'a', 'a', 'a', 't'],
                    ['a', 't', 'a', 'a', 'a'],
                    ['a', 'a', 't', 'a', 'a']]

print(f"""            0    1   2   3   4
         0 | {lista_principal[0][0]} | {lista_principal[0][1]} | {lista_principal[0][2]} | {lista_principal[0][3]} | {lista_principal[0][4]} | \n
         1 | {lista_principal[1][0]} | {lista_principal[1][1]} | {lista_principal[1][2]} | {lista_principal[1][3]} | {lista_principal[1][4]} | \n
         2 | {lista_principal[2][0]} | {lista_principal[2][1]} | {lista_principal[2][2]} | {lista_principal[2][3]} | {lista_principal[2][4]} | \n
         3 | {lista_principal[3][0]} | {lista_principal[3][1]} | {lista_principal[3][2]} | {lista_principal[3][3]} | {lista_principal[3][4]} | \n
         4 | {lista_principal[4][0]} | {lista_principal[4][1]} | {lista_principal[4][2]} | {lista_principal[4][3]} | {lista_principal[4][4]} |

""")

def jogar(lista_navios, lista_tiros):
  hoz = lista_tiros[0]
  ver = lista_tiros[1]
  lista_principal[hoz][ver] = lista_navios[hoz][ver]
  print(f"""            0    1   2   3   4
         0 | {lista_principal[0][0]} | {lista_principal[0][1]} | {lista_principal[0][2]} | {lista_principal[0][3]} | {lista_principal[0][4]} | \n
         1 | {lista_principal[1][0]} | {lista_principal[1][1]} | {lista_principal[1][2]} | {lista_principal[1][3]} | {lista_principal[1][4]} | \n
         2 | {lista_principal[2][0]} | {lista_principal[2][1]} | {lista_principal[2][2]} | {lista_principal[2][3]} | {lista_principal[2][4]} | \n
         3 | {lista_principal[3][0]} | {lista_principal[3][1]} | {lista_principal[3][2]} | {lista_principal[3][3]} | {lista_principal[3][4]} | \n
         4 | {lista_principal[4][0]} | {lista_principal[4][1]} | {lista_principal[4][2]} | {lista_principal[4][3]} | {lista_principal[4][4]} |

  """)

# x = horizontal, y = vertical
h1 = int(input('Digite a cordenada horizontal: '))
v1 = int(input('Digite a cordenada vertical: '))
lista_tiros1 = [h1, v1]
jogar(lista_principal02, lista_tiros1)


h2 = int(input('Digite a cordenada horizontal: '))
v2 = int(input('Digite a cordenada vertical: '))
lista_tiros2 = [h2, v2]
jogar(lista_principal02, lista_tiros2)




h3 = int(input('Digite a cordenada horizontal: '))
v3 = int(input('Digite a cordenada vertical: '))
lista_tiros3 = [h3, v3]
jogar(lista_principal02, lista_tiros3)


h4 = int(input('Digite a cordenada horizontal: '))
v4 = int(input('Digite a cordenada vertical: '))
lista_tiros4 = [h4, v4]
jogar(lista_principal02, lista_tiros4)



h5 = int(input('Digite a cordenada horizontal: '))
v5 = int(input('Digite a cordenada vertical: '))
lista_tiros5 = [h5, v5]
jogar(lista_principal02, lista_tiros5)
