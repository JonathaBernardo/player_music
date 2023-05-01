playlist = open("playlist.txt", "r")

musicas = [linhas.strip() for linhas in playlist]

while True:
    print("Musicas na playslist: ")
    for num, musica in enumerate(musicas):
        print(f"{num + 1} . {musica}")

    musica_num = input("Digite o numero da musica a ser retirada(ou 'cancelar' para sair): ")
    if musica_num == "cancelar":
        break

    try:
        indice = int(musica_num) - 1
        musica_excluida = musicas.pop(indice)

        arquivo = open("playlist.txt", "w")
        for musica in musicas:
            arquivo.write(f"{musica}\n")

        print(f'A musica "{musica_excluida}" foi excluida!')
    except:
        print("Opção invalida. Insira um numero valido!!!")