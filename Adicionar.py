#### ADICIONAR MUSICA

l = open("playlist.txt", "a")

from datetime import datetime
dados = {}
externo = {}
externo['nome'] = str(input('Digite o nome da musica: '))
real_nome = externo['nome']


while True:
  try:
      dados['ano'] = int(input('Digite o ano da musica: '))
      break
  except ValueError:
    print("coloque um número inteiro")
while dados['ano'] < 1800 or dados['ano'] > datetime.now().year:
  print('ano inválido, tente novamente!')
  while True:
    try:
      dados['ano'] = int(input('Digite o ano da música: '))
      break
    except ValueError:
      print("coloque um número inteiro")
dados['genero'] = str(input('Digite o gênero da música: '))
dados['artista'] = str(input('Digite o artista da música: '))
dados['album'] = str(input('Digite o álbum da música: '))

str(dados["ano"])

externo = {externo['nome']:dados}

escrever = ""
for k in dados.keys():
  escrever += str(k) + ": " + str(dados[k]) + "; "
escrever += ":"
escrever = escrever.replace("; :"," . ")

l.write(real_nome + "; ")
l.write(str(escrever + "\n"))
l.close()