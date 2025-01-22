import random

# navio1 = ['n']
# navio2 = ['n']
# navio3 = ['n', 'n']
# navio4 = ['n', 'n', 'n']

lista_principal01 = [[['n'], ['a'], ['a'], ['a'], ['a']],
                    [['a'], ['a'], ['a'], ['a'], ['n']],
                    [['a'], ['a'], ['a'], ['a'], ['n']],
                    [['n'], ['a'], ['a'], ['a'], ['n']],
                    [['a'], ['a'], ['a'], ['a'], ['a']]]


numeros_colunas = [0, 1, 2, 3, 4]
numeros_linhas = [0, 1, 2, 3, 4]
colunas_aleatorio = random.sample(numeros_colunas, k=5)
linhas_aleatorio = random.sample(numeros_linhas, k=5)
print(colunas_aleatorio)
# um navio 1 parte
navio1 = lista_principal01[0][0]
# linha 0
a1 = lista_principal01[0][1]
a2 = lista_principal01[0][2]
a3 = lista_principal01[0][3]
a4 = lista_principal01[0][4]

# um navio 1 parte
navio2 = lista_principal01[1][4]
# linha 1
a5 = lista_principal01[1][0]
a6 = lista_principal01[1][1]
a7 = lista_principal01[1][2]
a8 = lista_principal01[1][3]



# tres navios na vertical
navio3 = lista_principal01[1][4]
navio4 = lista_principal01[2][4]
# linha 2
a9 = lista_principal01[2][0]
a10 = lista_principal01[2][1]
a11 = lista_principal01[2][2]
a12 = lista_principal01[2][3]
navio5 = lista_principal01[3][4]

# dois navios na horizontal
navio9 = lista_principal01[3][0]
navio10 = lista_principal01[3][1]
# linha 3
a13 = lista_principal01[3][1]
a14 = lista_principal01[3][2]
a15 = lista_principal01[3][3]

# linha 4
a16 = lista_principal01[4][0]
a17 = lista_principal01[4][1]
a18 = lista_principal01[4][2]
a19 = lista_principal01[4][3]
a20 = lista_principal01[4][4]



lista_principal02 = [[['n'], ['n'], ['n'], ['.'], ['.']],
                    [['.'], ['.'], ['.'], ['.'], ['n']],
                    [['.'], ['.'], ['.'], ['.'], ['n']],
                    [['.'], ['n'], ['.'], ['.'], ['.']],
                    [['.'], ['.'], ['n'], ['.'], ['.']]]

# um navio 2 parte
navio01 = lista_principal02[3][1]

# um navio 2 parte
navio02 = lista_principal02[4][2]


# tres navios na horizontal
navio03 = lista_principal02[0][0]
navio04 = lista_principal02[0][1]
navio05 = lista_principal02[0][2]

# dois navios na vertical
navio06 = lista_principal02[1][4]
navio07 = lista_principal02[2][4]









navios1 = ['t', 't', 't', 't', 't', 't', 't', 't', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']

lista_principal = [[['.'], ['.'], ['.'], ['.'], ['.']],
                   [['.'], ['.'], ['.'], ['.'], ['.']],
                   [['.'], ['.'], ['.'], ['.'], ['.']],
                   [['.'], ['.'], ['.'], ['.'], ['.']],
                   [['.'], ['.'], ['.'], ['.'], ['.']]]

print(f"""            0    1   2   3   4
         0 | {lista_principal[0][0][0]} | {lista_principal[0][1][0]} | {lista_principal[0][2][0]} | {lista_principal[0][3][0]} | {lista_principal[0][4][0]} | \n
         1 | {lista_principal[1][0][0]} | {lista_principal[1][1][0]} | {lista_principal[1][2][0]} | {lista_principal[1][3][0]} | {lista_principal[1][4][0]} | \n
         2 | {lista_principal[2][0][0]} | {lista_principal[2][1][0]} | {lista_principal[2][2][0]} | {lista_principal[2][3][0]} | {lista_principal[2][4][0]} | \n
         3 | {lista_principal[3][0][0]} | {lista_principal[3][1][0]} | {lista_principal[3][2][0]} | {lista_principal[3][3][0]} | {lista_principal[3][4][0]} | \n
         4 | {lista_principal[4][0][0]} | {lista_principal[4][1][0]} | {lista_principal[4][2][0]} | {lista_principal[4][3][0]} | {lista_principal[4][4][0]} |

""")

def jogar(navios, tiros):
  hoz = tiros[0]
  ver = tiros[1]
  lista_principal[hoz][ver] = navios
  print(f"""            0    1   2   3   4
         0 | {lista_principal[0][0][0]} | {lista_principal[0][1][0]} | {lista_principal[0][2][0]} | {lista_principal[0][3][0]} | {lista_principal[0][4][0]} | \n
         1 | {lista_principal[1][0][0]} | {lista_principal[1][1][0]} | {lista_principal[1][2][0]} | {lista_principal[1][3][0]} | {lista_principal[1][4][0]} | \n
         2 | {lista_principal[2][0][0]} | {lista_principal[2][1][0]} | {lista_principal[2][2][0]} | {lista_principal[2][3][0]} | {lista_principal[2][4][0]} | \n
         3 | {lista_principal[3][0][0]} | {lista_principal[3][1][0]} | {lista_principal[3][2][0]} | {lista_principal[3][3][0]} | {lista_principal[3][4][0]} | \n
         4 | {lista_principal[4][0][0]} | {lista_principal[4][1][0]} | {lista_principal[4][2][0]} | {lista_principal[4][3][0]} | {lista_principal[4][4][0]} |

  """)

# x = horizontal, y = vertical
h1 = int(input('Digite a cordenada horizontal: '))
v1 = int(input('Digite a cordenada vertical: '))
lista_tiros1 = [h1, v1]
navios = random.sample(navios1, k=1)
jogar(navios, lista_tiros1)


h2 = int(input('Digite a cordenada horizontal: '))
v2 = int(input('Digite a cordenada vertical: '))
lista_tiros2 = [h2, v2]
navios = random.sample(navios1, k=1)
jogar(navios, lista_tiros2)




h3 = int(input('Digite a cordenada horizontal: '))
v3 = int(input('Digite a cordenada vertical: '))
lista_tiros3 = [h3, v3]
navios = random.sample(navios1, k=1)
jogar(navios, lista_tiros3)


h4 = int(input('Digite a cordenada horizontal: '))
v4 = int(input('Digite a cordenada vertical: '))
lista_tiros4 = [h4, v4]
navios = random.sample(navios1, k=1)
jogar(navios, lista_tiros4)



h5 = int(input('Digite a cordenada horizontal: '))
v5 = int(input('Digite a cordenada vertical: '))
lista_tiros5 = [h5, v5]
navios = random.sample(navios1, k=1)
jogar(navios, lista_tiros5)



