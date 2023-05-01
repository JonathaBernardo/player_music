def editor():
    while True:
        nome_arquivo = "playlist.txt"

        # Abrir o arquivo e carregar as músicas existentes em uma lista
        with open(nome_arquivo, "r") as arquivo:
            musicas = [linha.strip() for linha in arquivo]

        while True:
            # Exibir a lista de músicas existentes
            print("Músicas disponíveis:")
            for i, musica in enumerate(musicas):
                print(f"{i+1}. {musica}")

            # Solicitar ao usuário a música a ser editada
            opcao = input("Digite o número da música que deseja editar (ou 'fim' para sair): ")
            if opcao == "fim":
                break


            indice = int(opcao) -1
            musica_editada = musicas[indice]

            # Obter novas informações da música a ser editada
            nova_musica = input(f"Atual: {musica_editada}. Novo nome da música (ou 'manter'): ")
            novo_ano = input(f"Atual: {musica_editada}. Novo ano da música (ou 'manter'): ")
            novo_artista = input(f"Atual: {musica_editada}. Novo nome do artista (ou 'manter'): ")
            novo_genero = input(f"Atual: {musica_editada}. Novo genero do artista (ou 'manter'): ")
            novo_album = input(f"Atual: {musica_editada}. Novo nome do álbum (ou 'manter'): ")

            # Atualizar as informações da música na lista
            if nova_musica != "manter":
                musica_editada = musica_editada.split("; ")
                musica_editada[0] = nova_musica
                musica_editada = ", ".join(musica_editada)
            if novo_ano != "manter":
                musica_editada = musica_editada.split("; ")
                musica_editada[1] = novo_ano
                musica_editada = ", ".join(musica_editada)
            if novo_artista != "manter":
                musica_editada = musica_editada.split("; ")
                musica_editada[2] = novo_artista
                musica_editada = ", ".join(musica_editada)
            if novo_album != "manter":
                musica_editada = musica_editada.split("; ")
                musica_editada[3] = novo_genero
                musica_editada = ", ".join(musica_editada)
            if novo_album != "manter":
                musica_editada = musica_editada.split(". ")
                musica_editada[4] = novo_album
                musica_editada = ", ".join(musica_editada)

            # Atualizar a lista de músicas com a música editada
            musicas[indice] = musica_editada

            with open(nome_arquivo, "w") as arquivo:
                for musica in musicas:
                    arquivo.write(f"{musica}\n")

                    print(f"A música '{musica_editada}' foi editada com sucesso!")
                    break