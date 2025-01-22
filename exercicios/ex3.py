import random

nome = input('Qual o seu nome? ')

pergunta1 = f'Responda sim ou não, {nome}: 2 + 2 = 4? '
pergunta2 = f'Responda sim ou não, {nome}: 2 * 2 = 5? '
pergunta3 = f'Responda sim ou não, {nome}: 2 / 2 = 1? '

gabarito = [['SIM', 'NÃO', pergunta1],
            ['NÃO', 'SIM', pergunta2],
            ['SIM', 'NÃO', pergunta3]]

ponto1 = 0
ponto2 = 0
ponto3 = 0
ponto4 = 0

perguntas_sorteadas = random.sample(gabarito, k=3)


def imprime_resultado(resposta, resposta_certa, resposta_errada):
  if resposta == resposta_certa:
    print('Acertou, ganhou 1 ponto')
  elif resposta == resposta_errada:
    print('errou, ganhou 0 pontos')
  else:
    print('Resposta inválida')

p1 = (input(perguntas_sorteadas[0][2])).upper()
if p1 == perguntas_sorteadas[0][0]:
  ponto1 = 1

imprime_resultado(p1, perguntas_sorteadas[0][0], perguntas_sorteadas[0][1])
print(ponto1)


p2 = (input(perguntas_sorteadas[1][2])).upper()

if p2 == perguntas_sorteadas[1][0]:
  ponto2 = 1
imprime_resultado(p2, perguntas_sorteadas[1][0], perguntas_sorteadas[1][1])

p3 = (input(perguntas_sorteadas[2][2])).upper()

if p3 == perguntas_sorteadas[2][0]:
  ponto3 = 1
imprime_resultado(p3, perguntas_sorteadas[2][0], perguntas_sorteadas[2][1])

escolha_usuario = input('Deseja criar a última pergunta? Digite sim ou não: ').upper()
if escolha_usuario == 'SIM':
  pergunta_usuario = input('Digite sua pergunta: ')
  resposta_sim = input('Digite a resposta certa: ')
  resposta_nao = input('Digite a resposta errada: ')

  gabarito_usuario = [
      f'{resposta_sim}', 'SIM', f'{resposta_nao}', 'NÃO',
      pergunta_usuario
  ]
  perguntas_sorteadas.append(gabarito_usuario)

  resposta_usuario = input(f'Responda sim ou não, {nome}: {perguntas_sorteadas[3][4]} ').upper()

  if resposta_usuario == perguntas_sorteadas[3][1]:
    ponto4 = 1
  imprime_resultado(resposta_usuario, perguntas_sorteadas[3][1], perguntas_sorteadas[3][3])

def calcula_pontos(p1, p2, p3, p4):
  pots_tts = p1 + p2 + p3 + p4
  return pots_tts

def calcula_metade(pot_tot, lista_perguntas):
  met = pot_tot / len(lista_perguntas)
  return met

pontos_totais = calcula_pontos(ponto1, ponto2, ponto3, ponto4)
metade = calcula_metade(pontos_totais, perguntas_sorteadas)


if pontos_totais == 0:
  print('Você não acertou nenhuma pergunta')
elif pontos_totais > 0 and pontos_totais < metade:
  print('Você acertou menos da metade das perguntas')
elif pontos_totais > metade and pontos_totais < len(perguntas_sorteadas):
  print('Você acertou mais da metade!')
elif pontos_totais == len(perguntas_sorteadas):
  print('Você acertou todas as perguntas!')

print(f'Obrigada por participar!')
